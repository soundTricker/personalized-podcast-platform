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
from typing import Optional
from zoneinfo import ZoneInfo

import aiohttp
from aiohttp import ClientTimeout
from google.adk.agents import Agent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from google.adk.planners import BuiltInPlanner
from google.genai import types
from pydantic import Field

from radio_station.constants import THINKING_MODEL
from radio_station.model.base_model import BaseModel
from radio_station.model.listener_program_segment import ListenerProgramWebSegment
from radio_station.state_keys import ResearcherState


class EntryResearchResult(BaseModel):
    url: str = Field(description="The url of the entry")
    summary: str = Field(description="The summary of the entry(item)")
    description: str = Field(description="The description of the entry(item)")


class WebResearchResult(BaseModel):
    summary: str = Field(description="The summary of the feed")
    description: str = Field(description="The description of the feed")
    entries: list[EntryResearchResult] = Field(description="The list of entries")


async def fetch(session, url):
    async with session.get(url) as response:
        return {"url": url, "response": await response.text()}


class WebResearchAgent(Agent):
    task_id: str = Field(description="The task id")
    segment: ListenerProgramWebSegment = Field(description="The url of the researching web site")

    def __init__(self, task_id: str, segment: ListenerProgramWebSegment, **kwargs):
        super().__init__(
            task_id=task_id,
            segment=segment,
            model=THINKING_MODEL,
            name=f"WebResearchAgent_{task_id}",
            instruction=f"""
            You are an AI Web Investigation Assistant specializing to make a radio program.

            Your tasks are:
            1. Read and analyze fetched HTML Contents in `<HTMLContents>{{HTML CONTENT LIST}}</HTMLContents>`.
                1-1. When HTML Contents included publish datetime/released datetime/updated datetime information, read/analyze only content after [Last Read Datetime].
            2. Make a investigation summary and investigation description of the contents.
                2-1. When HTML Contents included publish datetime/released datetime/updated datetime information, **DON'T** include the content before [Last Read Datetime].

            Output Format:
            JSON, Japanese.

            Output Schema:
            Make a JSON with below attributes.

            - 'summary': The short string summary of the feed
            - 'description': The description of the feed
            - 'entries':
                - 'url': The content url
                - 'summary': The short string summary of the entry(item)
                - 'description': The description of the feed

            [Current Datetime]
            {datetime.datetime.now(tz=ZoneInfo("Asia/Tokyo")).isoformat()}

            [Last Read Datetime]
            {datetime.datetime.fromtimestamp(segment.last_read_timestamp or 0).astimezone(ZoneInfo("Asia/Tokyo")).isoformat()}
        """,
            generate_content_config=types.GenerateContentConfig(frequency_penalty=-2.0),
            before_model_callback=self.fetch_contents,
            output_schema=WebResearchResult,
            output_key=ResearcherState.research_result(task_id),
            disallow_transfer_to_parent=True,
            include_contents="none",
            **kwargs,
        )

    async def fetch_contents(self, callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
        async with aiohttp.ClientSession(timeout=ClientTimeout(total=300)) as session:
            tasks = [fetch(session, url) for url in self.segment.urls]
            results = await asyncio.gather(*tasks)
            text = "<HTMLContents>"
            contents = []
            for result in results:
                contents.append(f"""
                <CONTENT>
                <URL>{result["url"]}</URL>
                <DATA><{result["response"]}]]</DATA>
                </CONTENT>
                """)
            llm_request.contents.append(types.Content(role="user", parts=[types.Part.from_text(text=text + "\n".join(contents) + "</HTMLContents>")]))


class FormatAgent(Agent):
    task_id: str | int = Field(description="The task id")

    def __init__(self, task_id, **kwargs):
        super().__init__(
            task_id=task_id,
            model=THINKING_MODEL,
            name=f"WebResearchResultFormatAgent_{task_id}",
            instruction=f"""
            You are an agent that formats the answers from WebResearchAgent_{task_id} agent.

            # Your task
            Read data from session state with key '{ResearcherState.research_result(task_id)}' and format'
            """,
            planner=BuiltInPlanner(thinking_config=types.ThinkingConfig(thinking_budget=0, include_thoughts=False)),
            output_schema=WebResearchResult,
            output_key=ResearcherState.research_result(task_id),
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
            **kwargs,
        )


class WebResearchFlowAgent(SequentialAgent):
    task_id: str | int = Field(description="The task id")
    task: ListenerProgramWebSegment = Field(description="my task")

    def __init__(self, task_id, task: ListenerProgramWebSegment, **kwargs):
        super().__init__(
            task_id=task_id,
            task=task,
            name=f"WebResearchFlowAgent_{task_id}",
            sub_agents=[
                WebResearchAgent(task_id=task_id, segment=task),
                FormatAgent(task_id=task_id),
            ],
            **kwargs,
        )
