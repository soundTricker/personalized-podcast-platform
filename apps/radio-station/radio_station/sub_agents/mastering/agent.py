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

import io
import logging
import math
from typing import AsyncGenerator

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.genai import types
from pydub import AudioSegment
from pydub.effects import compress_dynamic_range, normalize

from radio_station.model.program_plan import SegmentType
from radio_station.state_keys import ComposerState, ProgramPlannerState, RecorderState, WriterState
from radio_station.utils.artifact import list_artifact, load_artifact, save_artifact
from radio_station.utils.audio import convert_mp3
from radio_station.utils.env import is_run_on_agent_engine

logger = logging.getLogger(__name__)


# Agent to mastering the audio track by mixing recorded speech and background music.
class MasteringAgent(BaseAgent):
    def __init__(self, name="MasteringAgent", **kwargs):
        super().__init__(name=name, **kwargs)

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        if "audio.mp3" in await list_artifact(ctx):
            yield Event(
                invocation_id=ctx.invocation_id,
                author=self.name,
                content=types.ModelContent(
                    parts=[
                        types.Part(text="already finished this task"),
                    ],
                ),
            )
            return

        task_ids = ctx.session.state.get(RecorderState.TEMP_TASK_IDS)

        if not task_ids:
            raise ValueError("task_ids not found in state.")

        logger.info(f"start mixing {task_ids}")

        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.ModelContent(
                parts=[
                    types.Part(text=f"Start generating for: {task_ids}"),
                ],
            ),
        )
        mixed = await self.mixing(ctx)

        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.ModelContent(
                parts=[
                    types.Part(text=f"Finished mixing for: {task_ids}, next start mastering"),
                ],
            ),
        )

        track = await self.mastering(mixed)

        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.ModelContent(
                parts=[
                    types.Part(text=f"Finished mastering for: {task_ids}, next start convert to mp3"),
                ],
            ),
        )

        await save_artifact(ctx, "audio.mp3", types.Part.from_bytes(data=convert_mp3(track), mime_type="audio/mp3"))

        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.ModelContent(
                parts=[
                    types.Part(text=f"Generated merged audio for: {task_ids}"),
                ],
            ),
        )

    async def mixing(self, ctx):
        composer_task_ids = ctx.session.state.get(ComposerState.TASK_IDS, [])
        task_ids = ctx.session.state.get(RecorderState.TEMP_TASK_IDS)
        talk_script_segments = WriterState.get_talk_script_segments(ctx.session.state)

        program_plan = ProgramPlannerState.get_program_structure(ctx.session.state)
        logger.info(f"mixing composer: {composer_task_ids} recorder: {task_ids}")

        recoding_audios = []
        background_musics = []

        if is_run_on_agent_engine():
            AudioSegment.converter = "radio_station/ffmpeg-7.0.2-amd64-static/ffmpeg"

        for i, segment in enumerate(program_plan.segments):
            task_id = str(i + 1)
            tss_list = [tss for tss in talk_script_segments if tss.task_id == task_id]
            for tss in tss_list:
                recoding_artifact = await load_artifact(ctx, RecorderState.task_artifact_key(tss.id))
                logger.info(f"recoding_artifact: {RecorderState.task_artifact_key(tss.id)}({tss.id}) is None?: {recoding_artifact is None}")
                recoding_audio = AudioSegment.from_wav(io.BytesIO(recoding_artifact.inline_data.data))
                if task_id not in composer_task_ids:
                    logger.info(f"this segment does not have background music: {task_id}. {composer_task_ids}")
                    recoding_audios.append(recoding_audio)
                    background_musics.append(AudioSegment.silent(duration=len(recoding_audio) + 5000))
                    continue

                artifact_key = ComposerState.task_music_artifact_key(task_id)
                artifact = await load_artifact(ctx, artifact_key)
                music = AudioSegment.from_wav(io.BytesIO(artifact.inline_data.data))

                if segment.is_music:
                    origin_length = len(recoding_audio)
                    recoding_audio = recoding_audio + AudioSegment.silent(duration=100 + len(music))
                    recoding_audios.append(recoding_audio)
                    music = AudioSegment.silent(duration=origin_length + 100) + music
                    background_musics.append(music)
                    continue

                backend_music = music
                backend_music_gain = -10

                if segment.segment_type == SegmentType.OPENING:
                    # opening
                    opening_music_length = math.floor(4 * 4 / (segment.music_bpm / 60) * 1000) if segment.music_bpm is not None else 10000
                    recoding_audio = AudioSegment.silent(duration=opening_music_length) + recoding_audio
                    backend_music = backend_music * (int(math.ceil((len(recoding_audio) / len(backend_music)))) + 1)
                    backend_music = backend_music[: len(recoding_audio) + 2500].fade(
                        to_gain=recoding_audio.dBFS + backend_music_gain - backend_music.dBFS, start=opening_music_length - 1000, end=opening_music_length
                    )
                    background_musics.append(backend_music)
                    recoding_audios.append(recoding_audio)

                elif segment.segment_type == SegmentType.ENDING:
                    # closing
                    origin_db = backend_music.dBFS
                    backend_music = backend_music.apply_gain(recoding_audio.dBFS + backend_music_gain - origin_db)
                    origin_length = len(recoding_audio)
                    ending_music_length = math.floor(4 * 4 / (segment.music_bpm / 60) * 1000) if segment.music_bpm is not None else 10000
                    recoding_audio = recoding_audio + AudioSegment.silent(duration=ending_music_length)
                    backend_music = backend_music * (int(math.ceil((len(recoding_audio) / len(backend_music)))) + 1)
                    background_musics.append(
                        backend_music[: len(recoding_audio)].fade(to_gain=origin_db - backend_music.dBFS, start=origin_length, end=origin_length + 10).fade_out(ending_music_length)
                    )
                    recoding_audios.append(recoding_audio)

                else:
                    backend_music = backend_music.apply_gain(recoding_audio.dBFS + backend_music_gain - backend_music.dBFS)
                    backend_music = backend_music * (int(math.ceil((len(recoding_audio) / len(backend_music)))) + 1)
                    background_musics.append(backend_music[: len(recoding_audio) + 5000])
                    recoding_audios.append(recoding_audio)

        master_recoding_audio = None
        for recoding_audio in recoding_audios:
            if master_recoding_audio is None:
                master_recoding_audio = recoding_audio
            else:
                master_recoding_audio += recoding_audio

        master_background_music = None
        for background_music in background_musics:
            master_background_music = background_music if master_background_music is None else master_background_music.append(background_music, crossfade=2500)

        # マージ
        logger.info(f"merge audio: master_recoding_audio: len({len(master_recoding_audio)}), master_background_music: len({len(master_background_music)})")

        mixed = AudioSegment.silent(duration=len(master_background_music))
        return mixed.overlay(master_recoding_audio).overlay(master_background_music)

    async def mastering(self, mixed):
        # mastering
        logger.info("start mastering")
        ## Compression
        logger.info("compression")
        track = compress_dynamic_range(mixed, threshold=-20, ratio=2.5, attack=5, release=50)
        ## Limiting
        logger.info("Limiting")
        track = compress_dynamic_range(track, threshold=-1, ratio=20, attack=5, release=50)
        ## normalize
        logger.info("normalize")
        track = normalize(track)
        logger.info("finish mastering")
        return track
