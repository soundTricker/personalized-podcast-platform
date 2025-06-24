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

import logging
from typing import AsyncGenerator

from google.adk.agents import BaseAgent, ParallelAgent, SequentialAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.adk.sessions import Session
from google.genai import types

from radio_station.state_keys import GlobalState
from radio_station.sub_agents.composer.flow_agent import ComposerFlowAgent
from radio_station.sub_agents.mastering.agent import MasteringAgent
from radio_station.sub_agents.news_letter_writer.agent import NewsLetterWriterAgent
from radio_station.sub_agents.program_planner import ProgramPlannerAgent
from radio_station.sub_agents.recoder import RecordingFlowAgent
from radio_station.sub_agents.researcher import ResearchFlowAgent
from radio_station.sub_agents.writer import ProgramSegmentWriterFlowAgent

logger = logging.getLogger(__name__)


class GenerateRadioFlowAgent(BaseAgent):
    """
    ラジオ番組生成フロー a.k.a. DirectorAgent
    """

    def __init__(self, name="DirectorAgent", **kwargs):
        super().__init__(name=name, **kwargs)

    def validate_state(self, session: Session):
        state = session.state
        radio_casts = GlobalState.get_radio_casts(state)
        if not radio_casts:
            logger.error(f"Radio casts not found in state session_id:{session.id} user_id:{session.user_id} app_name:{session.app_name} state: {state} last_update:{session.last_update_time}")
            raise ValueError("Radio casts not found in state")

        listener_program = GlobalState.get_listener_program(state)
        if not listener_program:
            logger.error(f"Listener program not found in state session_id:{session.id} user_id:{session.user_id} app_name:{session.app_name} state: {state} last_update:{session.last_update_time}")
            raise ValueError("Listener program not found in state")

        listener_program_segments = GlobalState.get_listener_program_segments(state)
        if not listener_program_segments:
            logger.error(
                f"Listener program segments not found in state  session_id:{session.id} user_id:{session.user_id} app_name:{session.app_name} state: {state} last_update:{session.last_update_time}"
            )
            raise ValueError("Listener program segments not found in state")

        return True

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        try:
            self.validate_state(ctx.session)
            ctx.session.state.update({GlobalState.STATE: "running"})

            if GlobalState.DRY_RUN not in ctx.session.state:
                recording_news_letter_flow_agent = ParallelAgent(name="RecordingNewsLetterFlowAgent", sub_agents=[NewsLetterWriterAgent(), RecordingFlowAgent()])
                writer_recording_agent = SequentialAgent(name="WriterRecordingFlowAgent", sub_agents=[ProgramSegmentWriterFlowAgent(), recording_news_letter_flow_agent])
                writer_recording_composer_agent = ParallelAgent(name="WriterRecordingComposerFlowAgent", sub_agents=[writer_recording_agent, ComposerFlowAgent()])
                flow_agent = SequentialAgent(
                    name="GenerateRadioFlowSequentialAgent",
                    sub_agents=[ResearchFlowAgent(), ProgramPlannerAgent(), writer_recording_composer_agent, MasteringAgent()],
                )
            else:
                flow_agent = SequentialAgent(
                    name="DryRunGenerateRadioFlowSequentialAgent",
                    sub_agents=[ResearchFlowAgent(), ProgramPlannerAgent(), ProgramSegmentWriterFlowAgent(), NewsLetterWriterAgent()],
                )

            yield Event(invocation_id=ctx.invocation_id, author=self.name, content=types.Content(role="model", parts=[types.Part.from_text(text=f"start generate radio app_name:{ctx.app_name}")]))

            async for event in flow_agent.run_async(ctx):
                yield event

            ctx.session.state.update({GlobalState.STATE: "done"})

            yield Event(invocation_id=ctx.invocation_id, author=self.name, content=types.Content(role="model", parts=[types.Part.from_text(text="finish generate radio")]))
        except Exception as e:
            logger.exception("failed to generate radio")
            ctx.session.state.update({GlobalState.STATE: "failure"})
            yield Event(invocation_id=ctx.invocation_id, author=self.name, error_code="500", error_message=str(e))


# default agent instance
agent = GenerateRadioFlowAgent()
