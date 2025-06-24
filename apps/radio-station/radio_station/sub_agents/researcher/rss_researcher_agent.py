# Copyright 2025 Keisuke Tominaga a.k.a soundTricker
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import datetime
import json
import logging
from typing import Optional

import aiohttp
import feedparser
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from google.adk.planners import BuiltInPlanner
from google.genai import types
from pydantic import Field

from radio_station.constants import THINKING_MODEL
from radio_station.model.base_model import BaseModel
from radio_station.state_keys import ResearcherState

logger = logging.getLogger(__name__)


class EntryResearchResult(BaseModel):
    summary: str = Field(description="The summary of the entry(item)")
    description: str = Field(description="The description of the entry(item)")


class FeedResearchResult(BaseModel):
    summary: str = Field(description="The summary of the feed")
    description: str = Field(description="The description of the feed")
    entries: list[EntryResearchResult] = Field(description="The list of entries")


class RssFeedResearchAgent(Agent):
    task_id: str | int = Field(description="The task id")

    def __init__(self, task_id, **kwargs):
        super().__init__(
            task_id=task_id,
            model=THINKING_MODEL,
            name=f"RssFeedResearchAgent_{task_id}",
            instruction="""
                You are an AI Atom/RSS Investigation Assistant specializing to make a radio program.

                Your tasks are:
                1. Read and analyze fetched Atom/RSS feed in `Feed`.
                    - If fetched Atom/RSS feed does not found, return empty object.
                2. Make a investigation summary and investigation description of the feed.

                Output Format:
                JSON, Japanese.

                Output Schema:
                Make a JSON with below attributes.

                - 'summary': The short string summary of the feed
                - 'description': The description of the feed
                - 'entries':
                    - 'summary': The short string summary of the entry(item)

            """,
            generate_content_config=types.GenerateContentConfig(frequency_penalty=-2.0),
            planner=BuiltInPlanner(thinking_config=types.ThinkingConfig(thinking_budget=0, include_thoughts=False)),
            before_agent_callback=self.rss_feed_fetcher,
            before_model_callback=self.add_feed_to_instruction,
            output_schema=FeedResearchResult,
            output_key=ResearcherState.research_result(task_id),
            **kwargs,
        )

    async def rss_feed_fetcher(self, callback_context: CallbackContext) -> types.Content | None:
        task_info = ResearcherState.get_task_info(callback_context.state, self.task_id)
        last_read_timestamp = task_info.get("last_read_timestamp", 0) or 0
        last_read_datetime = datetime.datetime.fromtimestamp(last_read_timestamp, tz=datetime.timezone.utc)

        d = None
        retry = 0
        while d is None:
            try:
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as session, session.get(task_info["feed_url"]) as response:
                    response.raise_for_status()
                    d = feedparser.parse(await response.text())
            except Exception as e:
                retry += 1
                if retry > 5:
                    raise e
                logger.exception("Failed to fetch feed %s, retry", task_info["feed_url"])
                await asyncio.sleep(1)

        # published_parsedはtime.struct_timeなのでdatetimeに変換して比較
        logging.info(f"feed: {task_info['feed_url']} feed updated: {datetime.datetime(*d.feed.updated_parsed[:6], tzinfo=datetime.timezone.utc)} last_read_datetime: {last_read_datetime}")
        feed_published_datetime = datetime.datetime(*d.feed.updated_parsed[:6], tzinfo=datetime.timezone.utc)
        if feed_published_datetime <= last_read_datetime:
            return types.Content(parts=[types.Part(text=f"Agent {callback_context.agent_name} skipped. feed is not updated.")], role="model")

        entries = [
            {
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary,
                "description": entry.description,
                "updated": entry.updated,
            }
            for entry in d.entries
            if datetime.datetime(*entry.updated_parsed[:6], tzinfo=datetime.timezone.utc) >= last_read_datetime
        ]

        for entry in d.entries:
            logging.info(
                f"feed: {task_info['feed_url']} feed updated: {datetime.datetime(*entry.updated_parsed[:6], tzinfo=datetime.timezone.utc)} last_read_datetime: {last_read_datetime} {datetime.datetime(*entry.updated_parsed[:6], tzinfo=datetime.timezone.utc) >= last_read_datetime}"
            )

        if len(entries) == 0:
            return types.Content(parts=[types.Part(text=f"Agent {callback_context.agent_name} skipped. feed entry is not updated.")], role="model")

        callback_context.state.update(
            {
                ResearcherState.task_feed(self.task_id): {
                    "title": d.feed.title,
                    "subtitle": d.feed.get("subtitle", ""),
                    "link": d.feed.link,
                    "description": d.feed.get("description", ""),
                    "updated": d.feed.updated,
                    "entries": entries,
                }
            }
        )

        return None

    def add_feed_to_instruction(self, callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
        feed = callback_context.state.get(ResearcherState.task_feed(self.task_id))
        llm_request.contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part(
                        text=f"""
Feed:
{json.dumps(feed, ensure_ascii=False)}
"""
                    )
                ],
            )
        )
