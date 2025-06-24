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
import logging
from typing import AsyncGenerator, List, Optional

from google.adk.agents import BaseAgent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event, EventActions
from google.genai import types

from radio_station.model.program_plan import SegmentType
from radio_station.model.talk_script import TalkScriptSegment
from radio_station.state_keys import GlobalState, ProgramPlannerState, ResearcherState, WriterState
from radio_station.sub_agents.writer.program_segment_writer_agent import (
    ProgramSegmentWriterAgent,
)

logger = logging.getLogger(__name__)


def after_writer_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    task_id = callback_context.agent_name.split("_", 1)[-1]
    if not task_id:
        raise ValueError("task_id is required")

    previous_talk_scripts = callback_context.state.get(WriterState.TALK_SCRIPT_SEGMENTS, [])
    current_talk_scripts = callback_context.state.get(WriterState.task_talk_script_segment(task_id))

    if not current_talk_scripts:
        return

    previous_talk_scripts.append(current_talk_scripts)

    callback_context.state.update({WriterState.TALK_SCRIPT_SEGMENTS: previous_talk_scripts})


class ProgramSegmentWriterFlowAgent(BaseAgent):
    """
    ProgramSegmentWriterフロー。
    """

    def __init__(self, name="ProgramSegmentWriterFlowAgent", **kwargs):
        super().__init__(name=name, **kwargs)

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        # 1. 必要な情報をStateから取得

        if ctx.session.state.get(WriterState.STATE, "") == "done":
            yield Event(invocation_id=ctx.invocation_id, author=self.name, content=types.ModelContent(parts=[types.Part.from_text(text="already finished this task")]))
            return

        program_plan = ProgramPlannerState.get_program_structure(ctx.session.state)
        if not program_plan:
            raise ValueError("Program plan not found in state.")
        research_results = ctx.session.state.get(ResearcherState.RESULTS, [])

        if not research_results:
            raise ValueError("Research results not found in state.")

        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            branch=ctx.branch,
            content=types.Content(role="model", parts=[types.Part.from_text(text="start writing")]),
            actions=EventActions(state_delta={WriterState.STATE: "running"}),
        )

        # 2. ProgramSegmentWriterAgentを初期化
        writer_agents: List[SequentialAgent] = []
        task_ids: List[str] = []
        for i, segment in enumerate(program_plan.segments):
            task_id = str(i + 1)  # 簡易的に連番をtask_idとする
            task_ids.append(task_id)

            ctx.session.state.update(
                {
                    WriterState.task_segment(task_id): segment.model_dump(),
                    WriterState.task_previous_segment(task_id): program_plan.segments[i - 1].model_dump() if i > 0 else None,
                    WriterState.task_next_segment(task_id): program_plan.segments[i + 1].model_dump() if i + 1 < len(program_plan.segments) else None,
                    WriterState.task_research_results(task_id): [rr for rr in research_results if rr["id"] in segment.program_segment_ids],
                }
            )

            writer_agents.append(self.make_writer(task_id))

        if not writer_agents:
            raise ValueError("program segments not found in state.")

        # 3. 各セグメントに対してProgramSegmentWriterAgentを順次実行
        talk_script_segments: list[dict] = []

        yield Event(invocation_id=ctx.invocation_id, author=self.name, branch=ctx.branch, content=types.Content(role="model", parts=[types.Part.from_text(text="start writing")]))

        for task_id, writer_agent in zip(task_ids, writer_agents, strict=False):
            retry = 0
            while True:
                try:
                    async for event in writer_agent.run_async(ctx):
                        yield event

                    segment = WriterState.get_segment(ctx.session.state, task_id)
                    # 各Agentの実行結果を収集
                    talk_script_segment_dict = ctx.session.state.get(WriterState.task_talk_script_segment(task_id))

                    if len(talk_script_segment_dict["scripts"]) == 0:
                        break

                    talk_script_segments.append(talk_script_segment_dict)
                    talk_script_segment = TalkScriptSegment(**talk_script_segment_dict)

                    while talk_script_segment.continue_segment and segment.segment_type == SegmentType.CONTENT:
                        ctx.session.state.update(
                            {
                                WriterState.task_continue_prev_segment(task_id): talk_script_segment.model_dump(),
                            }
                        )

                        wa = self.make_writer(task_id)
                        async for event in wa.run_async(ctx):
                            yield event
                        talk_script_segment_dict = ctx.session.state.get(WriterState.task_talk_script_segment(task_id))
                        talk_script_segments.append(talk_script_segment_dict)
                        talk_script_segment = TalkScriptSegment(**talk_script_segment_dict)
                    break
                except Exception as e:
                    retry += 1
                    if retry > 3:
                        raise e
                    logger.exception(f"failed to generate talk script {e}")
                    await asyncio.sleep(retry * 1)
                    continue

        if not talk_script_segments:
            raise ValueError("talk script segments not found in state.")

        radio_casts = GlobalState.get_radio_casts(ctx.session.state)
        talk_script = "\n".join([TalkScriptSegment(**tssd).to_talk_script_text(radio_casts) for tssd in talk_script_segments])

        # 4. 全てのセグメントの台本をまとめて返す
        parts = [
            types.Part(
                text=f"""
            [[Talk Script]]
            {talk_script}
            """
            )
        ]

        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.ModelContent(parts=parts),
            branch=ctx.branch,
            actions=EventActions(state_delta={WriterState.TALK_SCRIPT_SEGMENTS: talk_script_segments, WriterState.STATE: "done", GlobalState.TALK_SCRIPT: talk_script}),
        )

    def make_writer(self, task_id):
        writer_agent = ProgramSegmentWriterAgent(task_id=task_id)

        # todo critic does not make good advice ....
        # loop_agent = LoopAgent(
        #     name=f"CriticReviserLoop_{task_id}",
        #     sub_agents=[CriticAgent(task_id), ReviserAgent(task_id)],
        #     max_iterations=2
        # )
        writer_critic_reviser_agent = SequentialAgent(
            name=f"WriterCriticReviserLoopAgent_{task_id}",
            sub_agents=[
                writer_agent,
                # loop_agent
            ],
            after_agent_callback=after_writer_agent_callback,
        )
        return writer_critic_reviser_agent


# default agent instance
agent = ProgramSegmentWriterFlowAgent()
