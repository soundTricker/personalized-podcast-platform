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

from enum import Enum

from google.genai import types
from pydantic import Field

from .base_model import BaseModel


class RadioCastRole(str, Enum):
    RadioPersonality = "radio personality"
    Assistant = "assistant"
    Guest = "guest"


class RadioCast(BaseModel):
    id: str | int = Field(description="Radio Cast ID")
    name: str = Field(description="Radio Cast Name")
    role: RadioCastRole = Field(description="Radio Cast Role")
    personality: str = Field(description="Radio Cast Personality")

    voice_name: str | None = Field(description="Radio Cast Voice Name", default=None)

    def to_speaker_config(self) -> types.SpeakerVoiceConfig:
        return types.SpeakerVoiceConfig(
            speaker=self.name,
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name=self.voice_name.split("-")[-1],
                )
            ),
        )

    def to_llm_text(self):
        return f"""
        Radio Cast ID: {self.id}
        Radio Cast Name: {self.name}
        Role: {self.role.name}
        Personality: {self.personality}
        """
