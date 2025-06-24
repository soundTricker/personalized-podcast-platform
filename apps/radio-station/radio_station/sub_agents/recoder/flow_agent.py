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

import itertools
import uuid
from typing import AsyncGenerator

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.cloud import texttospeech
from google.genai import types

from radio_station.model.talk_script import CustomPronunciations
from radio_station.state_keys import GlobalState, RecorderState, WriterState
from radio_station.sub_agents.recoder.llm_recorder_agent import LLMRecorderAgent
from radio_station.sub_agents.recoder.llm_tts_recorder_agent import LLMTTSRecorderAgent
from radio_station.sub_agents.recoder.recorder_agent import RecorderAgent
from radio_station.utils.artifact import load_artifact
from radio_station.utils.semaphore_parallel_agent import SemaphoreParallelAgent


class RecordingFlowAgent(BaseAgent):
    def __init__(self, name="RecordingFlowAgent", **kwargs):
        super().__init__(name=name, **kwargs)

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        if RecorderState.TASK_STATE in ctx.session.state and ctx.session.state.get(RecorderState.TASK_STATE) == "done" and RecorderState.TEMP_TASK_IDS in ctx.session.state:
            yield Event(invocation_id=ctx.invocation_id, author=self.name, content=types.ModelContent(parts=[types.Part.from_text(text="already finished this task")]))
            return

        radio_casts = GlobalState.get_radio_casts(ctx.session.state)
        talk_script_segments = WriterState.get_talk_script_segments(ctx.session.state)
        talk_scripts = list(itertools.chain.from_iterable([tss.scripts for tss in talk_script_segments]))
        pronunciations = list(itertools.chain.from_iterable([tss.custom_pronunciations.pronunciations for tss in talk_script_segments if tss.custom_pronunciations]))
        all_custom_pronunciations = CustomPronunciations(pronunciations=pronunciations)

        agents = []
        task_ids = []

        merged_talk_scripts = []
        ts = None

        yield Event(invocation_id=ctx.invocation_id, author=ctx.agent.name, branch=ctx.branch, content=types.Content(role="model", parts=[types.Part.from_text(text="start recoding")]))
        recording_mode = ctx.session.state.get("recording_mode", "llm-tts")
        if recording_mode != "llm-tts":
            for talk_script in talk_scripts:
                talk_script.id = uuid.uuid4().hex
                talk_script.custom_pronunciations = all_custom_pronunciations
                if ts is None:
                    ts = talk_script
                elif ts.radio_cast_id == talk_script.radio_cast_id and ts.speaking_rate == talk_script.speaking_rate:
                    ts.content += talk_script.content
                else:
                    merged_talk_scripts.append(ts)
                    task_ids.append(ts.id)
                    ts = talk_script
        else:
            for index, tss in enumerate(talk_script_segments):
                tss.id = str(index + 1)
                task_ids.append(tss.id)

        if ts is not None:
            merged_talk_scripts.append(ts)
            task_ids.append(ts.id)

        ctx.session.state.update({RecorderState.TEMP_TASK_IDS: task_ids})

        if recording_mode == "llm":
            for talk_script in merged_talk_scripts:
                radio_cast = next(radio_cast for radio_cast in radio_casts if radio_cast.id == talk_script.radio_cast_id)
                ctx.session.state.update({RecorderState.task_redio_cast(talk_script.id): radio_cast.model_dump(), RecorderState.task_talk_script(talk_script.id): talk_script.model_dump()})
                agents.append(LLMRecorderAgent(task_id=talk_script.id, talk_scripts=merged_talk_scripts, talk_script=talk_script, radio_cast=radio_cast))

            for recorder_agent in agents:
                async for event in recorder_agent.run_async(ctx):
                    yield event

        elif recording_mode == "llm-tts":
            for talk_script_segment in talk_script_segments:
                radio_cast_ids = {ts.radio_cast_id for ts in talk_script_segment.scripts}
                segment_radio_casts = [rc for rc in radio_casts if rc.id in radio_cast_ids]

                await load_artifact(ctx, f"voice_{talk_script_segment.id}.wav")

                agents.append(LLMTTSRecorderAgent(task_id=talk_script_segment.id, talk_script_segment=talk_script_segment, radio_casts=segment_radio_casts))

            async for event in SemaphoreParallelAgent(name="ParallelRecordingAgent", sub_agents=agents, concurrency=3).run_async(ctx):
                yield event
        else:
            client = texttospeech.TextToSpeechLongAudioSynthesizeAsyncClient()
            for talk_script in merged_talk_scripts:
                radio_cast = next(radio_cast for radio_cast in radio_casts if radio_cast.id == talk_script.radio_cast_id)
                ctx.session.state.update({RecorderState.task_redio_cast(talk_script.id): radio_cast.model_dump(), RecorderState.task_talk_script(talk_script.id): talk_script.model_dump()})
                agents.append(RecorderAgent(task_id=talk_script.id, client=client))

            for recorder_agent in agents:
                async for event in recorder_agent.run_async(ctx):
                    yield event

        ctx.session.state.update({RecorderState.TEMP_TASK_IDS: task_ids, WriterState.TALK_SCRIPT_SEGMENTS: [tss.model_dump() for tss in talk_script_segments], RecorderState.TASK_STATE: "done"})

        yield Event(
            invocation_id=ctx.invocation_id,
            author=ctx.agent.name,
            branch=ctx.branch,
            content=types.ModelContent(parts=[types.Part.from_text(text="finish recoding")]),
        )


# default agent instance
agent = RecordingFlowAgent()
