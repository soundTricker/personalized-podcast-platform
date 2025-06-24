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

from pydantic import Field
from .base_model import BaseModel
from google.genai import types

class WeightedPrompt(BaseModel):

    text: str | None = Field(default=None, description="""Text prompt.""")
    weight: float | None = Field(
        default=None,
        description="""Weight of the prompt. The weight is used to control the relative
          importance of the prompt. Higher weights are more important than lower
          weights.

          Weight must not be 0. Weights of all weighted_prompts in this
          LiveMusicClientContent message will be normalized.""",
    )

class LiveMusicGenerationConfig(BaseModel):
    bpm: int = Field(description="Range: [60, 200]. Sets the Beats Per Minute you want for the generated music. You need to stop/play or reset the context for the model it take into account the new bpm.")
    density: float | None = Field(
        default=None, description="""Density of sounds. Range is [0.0, 1.0]. Controls the density of musical notes/sounds. Lower values produce sparser music; higher values produce "busier" music."""
    )
    brightness: float | None = Field(
        default=None,
        description="""Brightness of the music. Range is [0.0, 1.0]. Adjusts the tonal quality. Higher values produce "brighter" sounding audio, generally emphasizing higher frequencies.""",
    )
    scale: types.Scale | None = Field(
        default=None, description="""Scale of the generated music."""
    )
    mute_bass: bool | None = Field(
          default=None,
          description="""Whether the audio output should contain bass.""",
      )
    mute_drums: bool  | None = Field(
          default=None,
          description="""Whether the audio output should contain drums.""",
      )
    only_bass_and_drums: bool | None = Field(
          default=None,
          description="""Whether the audio output should contain only bass and drums.""",
      )
class MusicStanza(BaseModel):

    prompts: list[WeightedPrompt] = Field(description="prompt and weight list of this music stanza.")
    seconds: int = Field(description="this music stanza time length (seconds)")
    config: LiveMusicGenerationConfig = Field(description="music stanza config.")

    def to_gemini_prompts(self) -> list[types.WeightedPrompt]:
        return [types.WeightedPrompt(text=p.text, weight=p.weight) for p in self.prompts]

    def to_gemini_config(self) -> types.LiveMusicGenerationConfig:
        return types.LiveMusicGenerationConfig(bpm=self.config.bpm, density=self.config.density, brightness=self.config.brightness, scale=self.config.scale, mute_bass=self.config.mute_bass, mute_drums=self.config.mute_drums, only_bass_and_drums=self.config.only_bass_and_drums)

class MusicPlan(BaseModel):

    title: str = Field(description="music title.")
    stanzas: list[MusicStanza] = Field(description="music stanza list.")