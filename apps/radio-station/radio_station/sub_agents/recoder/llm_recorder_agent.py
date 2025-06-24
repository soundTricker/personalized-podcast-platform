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
import io
import logging
import wave
from typing import AsyncGenerator

from google.adk import Agent
from google.adk.agents import BaseAgent, LiveRequestQueue
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.genai import types
from pydantic import Field
from pydub import AudioSegment

from radio_station.model.radio_cast import RadioCast
from radio_station.model.talk_script import TalkScript
from radio_station.utils.artifact import save_artifact
from radio_station.utils.instruction_provider import secret_instruction

logger = logging.getLogger(__name__)


class LLMSpeakerAgent(Agent):
    task_id: str = Field(description="Unique identifier for this task")
    audio_byte_array: bytearray = Field(description="The audio byte array", default=bytearray())

    def __init__(self, task_id: str, talk_scripts: list[TalkScript], talk_script: TalkScript, radio_cast: RadioCast, **kwargs):
        super().__init__(
            task_id=task_id,
            include_contents="none",
            name=f"LLMSpeakerAgent_{task_id}",
            model="gemini-2.0-flash-live-preview-04-09",
            instruction=secret_instruction(
                "llm_tts_recorder_instruction",
                """You are a real-time native Japanese narrator for radio program.
Your job is narrate only the talk script that is provided below.
        """,
            ),
            generate_content_config=types.GenerateContentConfig(
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=radio_cast.voice_name.split("-")[-1] if radio_cast.voice_name else "Fenrir")),
                    language_code="ja-JP",
                ),
                response_modalities=["AUDIO"],
            ),
            **kwargs,
        )


class LLMRecorderAgent(BaseAgent):
    task_id: str = Field(description="Unique identifier for this task")
    talk_scripts: list[TalkScript]
    talk_script: TalkScript
    radio_cast: RadioCast
    audio_byte_array: bytearray = Field(description="The audio byte array", default=bytearray())

    def __init__(self, task_id: str, talk_scripts: list[TalkScript], talk_script: TalkScript, radio_cast: RadioCast, **kwargs):
        super().__init__(task_id=task_id, talk_scripts=talk_scripts, talk_script=talk_script, radio_cast=radio_cast, name=f"LLMRecorderAgent_{task_id}", **kwargs)

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        agent = LLMSpeakerAgent(task_id=self.task_id, talk_scripts=self.talk_scripts, talk_script=self.talk_script, radio_cast=self.radio_cast)

        logger.info(f"Agent task is say: {agent.instruction}")
        ctx.live_request_queue = LiveRequestQueue()
        ctx.live_request_queue.send_content(types.Content(role="user", parts=[types.Part(text="start")]))
        await asyncio.sleep(0)

        async for event in agent.run_live(ctx):
            yield event

            if not event.content or not event.content.parts[0].inline_data or not event.content.parts[0].inline_data.data:
                if event.turn_complete:
                    logger.info(f"[TURN COMPLETE] {event}")
                    break
                if event.interrupted:
                    logger.info(f"[INTERRUPTED] {event}")
                    break
                continue

            self.audio_byte_array.extend(event.content.parts[0].inline_data.data)

            if event.turn_complete:
                logger.info(f"[TURN COMPLETE] {event}")
                break

            if event.interrupted:
                logger.info(f"[INTERRUPTED] {event}")

        await self.save_audio(ctx)
        # yield Event(author=self.name, content=types.Content(role=self.name, parts=parts), actions=EventActions(state_delta={ResearcherState.TASK_IDS: task_ids, ResearcherState.RESULTS: results}))

    async def save_audio(self, ctx: InvocationContext) -> None:
        buf = io.BytesIO()

        with wave.open(buf, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(24000)
            wf.writeframes(self.audio_byte_array)

        buf.seek(0)
        audio_segment = AudioSegment.from_wav(buf)

        out = io.BytesIO()
        audio_segment.export(out, format="mp3", bitrate="192k")
        part = types.Part.from_bytes(data=out.getvalue(), mime_type="audio/mp3")

        await save_artifact(ctx, f"audio_{self.task_id}.mp3", part)
