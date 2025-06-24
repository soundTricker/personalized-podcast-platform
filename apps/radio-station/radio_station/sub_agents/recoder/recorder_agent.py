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
import os
import uuid
from typing import AsyncGenerator

import google
import google.api_core.exceptions
from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.cloud import storage, texttospeech
from google.genai import types
from pydantic import Field
from pydub import AudioSegment

from radio_station.model.radio_cast import RadioCast
from radio_station.model.talk_script import TalkScript
from radio_station.state_keys import RecorderState
from radio_station.utils.artifact import save_artifact

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SPLIT_LENGTH = 2000


class RecorderAgent(BaseAgent):
    task_id: str = Field(description="Unique identifier for this task")
    client: texttospeech.TextToSpeechLongAudioSynthesizeAsyncClient
    storage_client: storage.Client

    def __init__(self, task_id: str, client: texttospeech.TextToSpeechLongAudioSynthesizeAsyncClient = None, storage_client: storage.Client = None, **kwargs):
        client = client or texttospeech.TextToSpeechLongAudioSynthesizeAsyncClient()
        storage_client = storage_client or storage.Client()
        super().__init__(task_id=task_id, client=client, storage_client=storage_client, name=f"RecorderAgent_{task_id}", **kwargs)

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        radio_cast_dict = ctx.session.state.get(RecorderState.task_redio_cast(self.task_id))
        radio_cast = RadioCast(**radio_cast_dict)
        talk_script_dict = ctx.session.state.get(RecorderState.task_talk_script(self.task_id))
        talk_script = TalkScript(**talk_script_dict)

        # Use Vertex AI Text-to-Speech to create audio
        client = self.client

        talk_script.content = talk_script.content.replace("！", "！。").replace("？", "？。")
        # if talk_script.custom_pronunciations:
        #     for pronunc in talk_script.custom_pronunciations.pronunciations:
        #         talk_script.content = talk_script.content.replace(pronunc.phrase, pronunc.pronunciation)
        # if len(talk_script.content) > SPLIT_LENGTH:
        #
        #     contents = []
        #     i = SPLIT_LENGTH
        #     content = talk_script.content[:i]
        #
        #     while i < len(talk_script.content) - 1:
        #         c = talk_script.content[i]
        #         content = content + c
        #         if c == "。":
        #
        #             contents.append(content)
        #             content = talk_script.content[i+1:i+SPLIT_LENGTH]
        #             i += SPLIT_LENGTH
        #             continue
        #         i += 1
        #     contents.append(content)
        # else:
        #     contents = [talk_script.content]
        contents = [talk_script.content.replace("、", ",").replace("。", "...")]
        audio_segment = None
        for content in contents:
            audio_segment, creating = await self.tts(audio_segment, client, radio_cast, talk_script, [content])

        out = io.BytesIO()
        audio_segment.export(out, format="mp3", bitrate="192k")
        part = types.Part.from_bytes(data=out.getvalue(), mime_type="audio/mp3")

        await save_artifact(ctx, f"audio_{self.task_id}.mp3", part)

        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.Content(
                role="model",
                parts=[
                    types.Part(text=f"Generated audio for: {talk_script.content}"),
                ],
            ),
        )

    async def tts(self, audio_segment, client, radio_cast, talk_script, target_contents, retry=0):
        for target_content in target_contents:
            while True:
                try:
                    synthesis_input = texttospeech.SynthesisInput(text=target_content, custom_pronunciations=talk_script.to_tts_custom_pronunciations())

                    voice = texttospeech.VoiceSelectionParams(
                        language_code="ja-JP",  # or the appropriate language code
                        name=radio_cast.voice_name or "ja-JP-Chirp3-HD-Achird",
                    )

                    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16, speaking_rate=talk_script.speaking_rate, effects_profile_id=["headphone-class-device"])

                    parent = f"projects/{os.getenv('GOOGLE_CLOUD_PROJECT')}/locations/{os.getenv('GOOGLE_CLOUD_LOCATION')}"
                    filepath = f"{self.task_id}/audio_{uuid.uuid4().hex}.wav"
                    uri = f"gs://{os.getenv('GOOGLE_STORAGE_AUDIO_EXPORT_BUCKET')}/{filepath}"
                    request = texttospeech.SynthesizeLongAudioRequest(parent=parent, input=synthesis_input, voice=voice, audio_config=audio_config, output_gcs_uri=uri)

                    operation = await client.synthesize_long_audio(request=request)
                    while True:
                        try:
                            await operation.result(timeout=1200)
                            break
                        except google.api_core.exceptions.RetryError:
                            continue
                        except Exception as e:
                            raise e
                    bucket = self.storage_client.get_bucket(os.getenv("GOOGLE_STORAGE_AUDIO_EXPORT_BUCKET"))
                    blob = bucket.get_blob(filepath)

                    buf = io.BytesIO(blob.download_as_bytes())
                    if audio_segment is None:
                        audio_segment = AudioSegment.from_wav(buf)
                    else:
                        audio_segment += AudioSegment.from_wav(buf)
                    break
                except Exception as e:
                    logger.exception(f"failed to create audio from text {target_content}")

                    if retry >= 5:
                        raise e
                    if "Timeout" in str(e):
                        retry += 1
                        await asyncio.sleep(5)

                        continue

                    if "This request contains sentences that are too long" in str(e):
                        tcss = [tc.replace("、", ".") + "。." for tc in target_content.split("。")]
                        audio_segment, _ = await self.tts(audio_segment, client, radio_cast, talk_script, tcss, retry=retry + 1)
                        break
                    retry += 1
                    await asyncio.sleep(5)

        return audio_segment, False
