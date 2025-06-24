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
from typing import AsyncGenerator, List

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event, EventActions
from google.genai import types

from radio_station.state_keys import ComposerState, ProgramPlannerState
from radio_station.sub_agents.composer.agent import ComposerAgent
from radio_station.utils.semaphore_parallel_agent import SemaphoreParallelAgent

logger = logging.getLogger(__name__)


class ComposerFlowAgent(BaseAgent):
    """
    ComposerFlow。
    """

    def __init__(self, name="ComposerFlowAgent", **kwargs):
        super().__init__(name=name, **kwargs)

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        if ComposerState.TASK_IDS in ctx.session.state:
            yield Event(invocation_id=ctx.invocation_id, author=self.name, content=types.ModelContent(parts=[types.Part.from_text(text="already finished this task")]))
            return

        program_plan = ProgramPlannerState.get_program_structure(ctx.session.state)
        if not program_plan:
            raise ValueError("Program plan not found in state.")

        agents: list[ComposerAgent] = []
        task_ids: List[str] = []

        yield Event(
            invocation_id=ctx.invocation_id,
            author=ctx.agent.name,
            branch=ctx.branch,
            content=types.Content(role="model", parts=[types.Part.from_text(text="start generate musics")]),
        )

        for i, segment in enumerate(program_plan.segments):
            if not segment.is_music and segment.background_music is None:
                logger.info(f"background music not found in state. for segment: [{segment.title}]")
                continue

            logger.info(f"Create music plan for segment: {segment.title}")

            task_id = str(i + 1)  # 簡易的に連番をtask_idとする
            task_ids.append(task_id)

            if segment.is_music:
                music_plan = f"""
                Create stanzas according to the following rules to clearly define the beginning and end of the music.
                - The opening stanza should be either drums only, bass only, or neither drums nor bass.
                - The closing stanza should be either drums only, bass only, or neither drums nor bass.

                Title: {segment.title}
                Description: {segment.description}
                """
                agents.append(ComposerAgent(task_id=task_id, music_plan=music_plan, seconds=segment.segment_seconds))
            else:
                music_plan = f"""
                This music use for the background music on podcast talk show.
                Music Description: {segment.background_music}
                """
                agents.append(ComposerAgent(task_id=task_id, music_plan=music_plan, seconds=segment.segment_seconds))

                # TODO currently(2025/06/18), lyria realtime does not have a pricing.
                # agents.append(ShortComposerAgent(task_id=task_id, music_plan=music_plan, seconds=segment.segment_seconds))

        if not agents:
            raise ValueError("program segments not found in state.")

        parallel_agent = SemaphoreParallelAgent(name="ParallelComposerAgent", sub_agents=agents, concurrency=3)

        async for event in parallel_agent.run_async(ctx):
            yield event

        # Set bpm to calculate music length
        for i, segment in enumerate(program_plan.segments):
            task_id = str(i + 1)
            music_plan = ComposerState.get_music_plan(ctx.session.state, task_id)
            if music_plan:
                segment.music_bpm = sum([s.config.bpm for s in music_plan.stanzas]) / len(music_plan.stanzas)

        yield Event(
            author=self.name,
            invocation_id=ctx.invocation_id,
            content=types.Content(role=self.name, parts=[types.Part.from_text(text="music generated")]),
            actions=EventActions(state_delta={ComposerState.TASK_IDS: task_ids, ProgramPlannerState.PROGRAM_STRUCTURE: program_plan.model_dump()}),
        )


# default agent instance
agent = ComposerFlowAgent()
