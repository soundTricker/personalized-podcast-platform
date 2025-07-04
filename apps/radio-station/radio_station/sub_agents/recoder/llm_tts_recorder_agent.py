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
import json
import logging
import os
from typing import AsyncGenerator, Optional

import google.genai.errors
from google import genai
from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.genai import types
from pydantic import Field
from pydub import AudioSegment, silence

from radio_station.model.radio_cast import RadioCast
from radio_station.model.talk_script import TalkScriptSegment
from radio_station.state_keys import GlobalState, RecorderState
from radio_station.utils.artifact import list_artifact, save_artifact
from radio_station.utils.audio import export_wav
from radio_station.utils.instruction_provider import secret_instruction

logger = logging.getLogger(__name__)


class LLMTTSSpeakerAgent(BaseAgent):
    task_id: str = Field(description="Unique identifier for this task")
    talk_script_segment: TalkScriptSegment
    radio_casts: list[RadioCast] = Field(description="List of radio cast objects", default_factory=list)
    generate_content_config: types.GenerateContentConfig
    audio_byte_array: bytearray = Field(description="The audio byte array", default=bytearray())
    seed: Optional[int]

    def __init__(
        self,
        task_id: str,
        talk_script_segment: TalkScriptSegment,
        radio_casts: list[RadioCast],
        seed: Optional[int],
        **kwargs,
    ):
        speech_config = types.SpeechConfig(
            language_code="ja-JP",
        )

        if len(radio_casts) == 1:
            speech_config.voice_config = types.VoiceConfig(prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=radio_casts[0].voice_name.split("-")[-1]))
        else:
            speech_config.multi_speaker_voice_config = types.MultiSpeakerVoiceConfig(speaker_voice_configs=[rc.to_speaker_config() for rc in radio_casts])

        logger.info(f"Speech Config: {speech_config.model_dump_json()}")

        super().__init__(
            task_id=task_id,
            name=f"LLMTTSRecorderAgent_{task_id}",
            generate_content_config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=speech_config,
                temperature=0,
            ),
            talk_script_segment=talk_script_segment,
            radio_casts=radio_casts,
            seed=seed,
            **kwargs,
        )

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"), vertexai=False)
        retry = 0

        program = GlobalState.get_listener_program(ctx.session.state)

        model = "gemini-2.5-pro-preview-tts" if program.pro_mode else "gemini-2.5-flash-preview-tts"

        content = await secret_instruction(
            "llm_tts_recorder_instruction",
            """You are a real-time native Japanese narrator for radio program.
Your job is narrate only the talk script that is provided below.
        """,
        )(ctx)

        content = (
            content
            + f"""
        [Radio Casts]
        {"------\n".join([rc.to_llm_text() for rc in self.radio_casts])}

        [Pronunciation]
        {json.dumps(self.talk_script_segment.custom_pronunciations.model_dump(), ensure_ascii=False) if self.talk_script_segment.custom_pronunciations else ""}

        <Talk Scripts>
        {self.talk_script_segment.to_talk_script_text(radio_casts=self.radio_casts)}
        </Task Scripts>
        """
        )

        change_model = False

        while True:
            try:
                logger.info(f"Sending(task_id: {self.task_id}) instruction: {content}")
                response = await client.aio.models.generate_content(
                    model=model,
                    contents=content,
                    config=self.generate_content_config,
                )
                logger.info(f"Generated task_id: {self.task_id}")

                if response.candidates[-1].content is None:
                    msg = f"Candidate not found for task_id: {self.task_id} response: {response.model_dump_json()}"
                    logger.error(msg)
                    raise Exception(msg)

                result = response.candidates[-1].content.parts[0].inline_data.data
                if self.has_long_silence(AudioSegment.from_raw(io.BytesIO(result), channels=1, sample_width=2, frame_rate=24000)) and retry < 3:
                    # 2秒以上の無音がある場合、失敗している可能性が高いのでもう一度作り直しさせる
                    retry += 1
                    logger.warning(f"detect long silence for task_id: {self.task_id}, retry")
                    await asyncio.sleep(1 * retry)
                    continue

                self.audio_byte_array = bytearray(result)

                yield Event(
                    invocation_id=ctx.invocation_id,
                    author=self.name,
                    content=types.Content(role="model", parts=[types.Part.from_text(text=f"generated speech for {self.task_id}")]),
                )

                return

            except google.genai.errors.ClientError as e:
                if e.code == 429 or e.code == 500:
                    logger.exception(f"failed to create tts audio maybe RESOURCE_EXHAUSTED or INTERNAL SERVER ERROR, change the model({model}) once {e}")
                    retry += 1
                    if retry > 5:
                        raise e
                    if not change_model:
                        model = "gemini-2.5-pro-preview-tts" if model == "gemini-2.5-flash-preview-tts" else "gemini-2.5-flash-preview-tts"
                        change_model = True
                    await asyncio.sleep(1 * retry)
                    continue
                logger.exception(f"failed to create tts audio {e}")
                retry += 1
                if retry > 5:
                    raise e
                await asyncio.sleep(1 * retry)

            except Exception as e:
                logger.exception(f"failed to create tts audio {e}")
                retry += 1
                if retry > 5:
                    raise e
                await asyncio.sleep(1 * retry)

    def has_long_silence(self, audio: AudioSegment, silence_threshold=-50, chunk_size=2000):
        start_trim = silence.detect_leading_silence(audio, silence_threshold, chunk_size)
        end_trim = silence.detect_leading_silence(audio.reverse(), silence_threshold, chunk_size)

        return start_trim > 0 or end_trim > 0


class LLMTTSRecorderAgent(BaseAgent):
    task_id: str = Field(description="Unique identifier for this task")
    talk_script_segment: TalkScriptSegment
    radio_casts: list[RadioCast]
    audio_byte_array: bytearray = Field(description="The audio byte array", default=bytearray())
    seed: Optional[int]

    def __init__(
        self,
        task_id: str,
        talk_script_segment: TalkScriptSegment,
        radio_casts: list[RadioCast],
        seed: Optional[int],
        **kwargs,
    ):
        super().__init__(
            task_id=task_id,
            talk_script_segment=talk_script_segment,
            radio_casts=radio_casts,
            name=f"LLMTTSRecorderAgent_{task_id}",
            seed=seed,
            **kwargs,
        )

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        if RecorderState.task_artifact_key(self.task_id) in await list_artifact(ctx):
            yield Event(
                invocation_id=ctx.invocation_id,
                author=self.name,
                branch=ctx.branch,
                content=types.Content(role="model", parts=[types.Part.from_text(text=f"generated speech for {self.task_id}")]),
            )
            return

        agent = LLMTTSSpeakerAgent(
            task_id=self.task_id,
            radio_casts=self.radio_casts,
            talk_script_segment=self.talk_script_segment,
            seed=self.seed,
        )
        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            branch=ctx.branch,
            content=types.Content(role="model", parts=[types.Part.from_text(text=f"generate tts audio for {RecorderState.task_artifact_key(self.task_id)}")]),
        )

        async for event in agent.run_async(ctx):
            yield event
        self.audio_byte_array = agent.audio_byte_array.copy()
        logger.info(f"generated content for {self.task_id}, start save the audio")
        await self.save_audio(ctx)
        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            branch=ctx.branch,
            content=types.Content(role="model", parts=[types.Part.from_text(text=f"generated tts audio for {RecorderState.task_artifact_key(self.task_id)}")]),
        )

    async def save_audio(self, ctx: InvocationContext) -> None:
        audio_segment = AudioSegment.from_raw(io.BytesIO(self.audio_byte_array), channels=1, sample_width=2, frame_rate=24000)
        part = types.Part.from_bytes(data=export_wav(audio_segment), mime_type="audio/wav")

        await save_artifact(ctx, RecorderState.task_artifact_key(self.task_id), part)
