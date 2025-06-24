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

from pydub import AudioSegment

from radio_station.utils.env import is_run_on_agent_engine


def convert_mp3(audio_segment: AudioSegment, bitrate="96k") -> bytes:
    out = io.BytesIO()
    if is_run_on_agent_engine():
        audio_segment.converter = "radio_station/ffmpeg-7.0.2-amd64-static/ffmpeg"

    audio_segment.export(out, format="mp3", bitrate=bitrate)
    return out.getvalue()


def export_wav(audio_segment: AudioSegment) -> bytes:
    out = io.BytesIO()
    if is_run_on_agent_engine():
        audio_segment.converter = "radio_station/ffmpeg-7.0.2-amd64-static/ffmpeg"

    audio_segment = audio_segment.set_frame_rate(22050)
    audio_segment.export(out, format="wav")
    return out.getvalue()
