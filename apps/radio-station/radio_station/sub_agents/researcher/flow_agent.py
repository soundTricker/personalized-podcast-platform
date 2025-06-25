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

import datetime
import json
import logging
import uuid
from typing import AsyncGenerator

from google.adk.agents import BaseAgent, ParallelAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event, EventActions
from google.genai import types

from radio_station.model.listener_program_segment import (
    ListenerProgramCalendarSegment,
    ListenerProgramSegment,
    ListenerProgramWebSegment,
    SegmentType,
)
from radio_station.state_keys import GlobalState, ResearcherState
from radio_station.sub_agents.researcher.calendar_researcher_agent import CalendarResearchFlowAgent
from radio_station.sub_agents.researcher.gmail_researcher_agent import GmailResearchAgent
from radio_station.sub_agents.researcher.rss_researcher_agent import (
    RssFeedResearchAgent,
)
from radio_station.sub_agents.researcher.web_researcher_agent import WebResearchAgent

logger = logging.getLogger(__name__)


class ResearchFlowAgent(BaseAgent):
    def __init__(self, name="ResearchFlowAgent", **kwargs):
        super().__init__(name=name, **kwargs)

    """
    ResearchFlowフロー、別名調査マネージャー。
    """

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        if ResearcherState.TASK_IDS in ctx.session.state and ResearcherState.RESULTS in ctx.session.state:
            yield Event(invocation_id=ctx.invocation_id, author=self.name, content=types.ModelContent(parts=[types.Part.from_text(text="already finished this task")]))
            return

        segments = ctx.session.state.get(GlobalState.LISTENER_PROGRAM_SEGMENTS)

        if not segments:
            raise ValueError("Listener program segments not found in state.")

        research_agents = []
        task_ids = []
        for segment in segments:
            seg = ListenerProgramSegment(**segment)
            task_id = str(seg.id) if seg.id else str(uuid.uuid4())
            task_ids.append(task_id)
            ctx.session.state[ResearcherState.task_info(task_id)] = segment
            logger.info(f"Make researcher for {seg.segment_type}")
            if seg.segment_type == SegmentType.RSS:
                research_agents.append(RssFeedResearchAgent(task_id))
            elif seg.segment_type == SegmentType.CALENDAR:
                research_agents.append(CalendarResearchFlowAgent(task_id, ListenerProgramCalendarSegment(**segment)))
            elif seg.segment_type == SegmentType.WEB:
                research_agents.append(WebResearchAgent(task_id, ListenerProgramWebSegment(**segment)))
            elif seg.segment_type == SegmentType.GMAIL:
                research_agents.append(GmailResearchAgent(task_id))

            # TODO CriticReviserLoop to make more good research

        parallel_agent = ParallelAgent(name="ParallelResearchAgent", sub_agents=research_agents)

        yield Event(invocation_id=ctx.invocation_id, author=ctx.agent.name, branch=ctx.branch, content=types.Content(role="model", parts=[types.Part.from_text(text="start research")]))

        async for event in parallel_agent.run_async(ctx):
            yield event

        parts = []
        results = []
        for task_id in task_ids:
            task_info = ListenerProgramSegment(**ctx.session.state.pop(ResearcherState.task_info(task_id)))
            research_result = ctx.session.state.get(ResearcherState.research_result(task_id))
            if not research_result:
                segment = {
                    "id": task_info.id,
                    "segment_title": task_info.title,
                    "segment_description": task_info.description,
                    "segment_constrains": task_info.constraints,
                    "investigation_result": {"summary": "No updated content", "description": "No updated content"},
                }
            else:
                segment = {
                    "id": task_info.id,
                    "segment_title": task_info.title,
                    "segment_description": task_info.description,
                    "segment_constrains": task_info.constraints,
                    "investigation_result": research_result,
                }
            results.append(segment)
            parts.append(
                types.Part(
                    text=f"""
            [[Investigation Result (Segment:{task_info.id})]]
            Segment ID: {task_info.id}
            Segment Title: {task_info.title}
            Segment Description: {task_info.description or ""}
            Investigation Result: {json.dumps(research_result, ensure_ascii=False)}
            """
                )
            )

        if not task_ids:
            raise ValueError("task_ids is empty")

        if not results:
            raise ValueError("results is empty")

        for segment in segments:
            segment["last_read_timestamp"] = datetime.datetime.now().timestamp()

        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.Content(role=self.name, parts=parts),
            actions=EventActions(state_delta={ResearcherState.TASK_IDS: task_ids, ResearcherState.RESULTS: results, GlobalState.LISTENER_PROGRAM_SEGMENTS: segments}),
        )


# default agent instance
agent = ResearchFlowAgent()
