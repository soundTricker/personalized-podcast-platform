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

from google.cloud import texttospeech
from pydantic import Field

from .base_model import BaseModel
from .radio_cast import RadioCast


class Pronunciation(BaseModel):
    phrase: str = Field(description="The phrase to which the customization is applied. The phrase can be multiple words, such as proper nouns, but shouldn't span the length of the sentence.")
    pronunciation: str = Field(description="The pronunciation of the phrase")


class CustomPronunciations(BaseModel):
    pronunciations: list[Pronunciation] = Field(description="The pronunciation customizations are applied", default_factory=lambda: [])


class TalkScript(BaseModel):
    """
    トークスクリプト
    """

    id: str | None = Field(default=None, description="Talk ID")
    radio_cast_id: str = Field(description="Radio Cast ID, not Radio Cast Name")
    speaking_rate: float = Field(description="The speaking speed with values ranging from 0.25x (very slow) to 2x (very fast)", default=1)
    content: str = Field(description="Talk contents, it can set less than 4000 characters")
    custom_pronunciations: CustomPronunciations | None = Field(description="Talk custom pronunciations", default=None)

    def to_tts_custom_pronunciations(self) -> texttospeech.CustomPronunciations | None:
        if self.custom_pronunciations is None:
            return None
        return texttospeech.CustomPronunciations(
            pronunciations=[
                texttospeech.CustomPronunciationParams(
                    phrase=p.phrase, pronunciation=p.pronunciation, phonetic_encoding=texttospeech.CustomPronunciationParams.PhoneticEncoding.PHONETIC_ENCODING_JAPANESE_YOMIGANA
                )
                for p in self.custom_pronunciations.pronunciations
            ]
        )


class TalkScriptSegment(BaseModel):
    id: str | None = Field(description="Talk script ID", default=None)
    task_id: str | None = Field(description="The ID of the current task")
    scripts: list[TalkScript] = Field(description="Talk scripts, when 1 radio cast, 1 long talk script, when multi radio casts, multiple scripts", default_factory=lambda: [])
    continue_segment: bool = Field(
        default=False,
        description="Continue current segment or not. When end of `scripts`(generated talk scripts) include the segment finish sentence, it should be 'false'. When current segment type is 'content' and when the generated scripts is over 4000 character and this segment have not finished yet, so you want to continue to create the talk script, you should stop to create the scripts and set `continue_segment` attribute `true`. Then AI Agent create a new task to generate remain talk script in current segment, otherwirse, it should be 'false'.",
    )
    hand_over: str | None = Field(
        default=None, description="When continue_segment is True, write a hand over message about what next writer agent should be write. When continue_segment is False, it is None."
    )
    custom_pronunciations: CustomPronunciations | None = Field(description="Talk custom pronunciations", default=None)

    def to_tts_custom_pronunciations(self) -> texttospeech.CustomPronunciations | None:
        if self.custom_pronunciations is None:
            return None
        return texttospeech.CustomPronunciations(
            pronunciations=[
                texttospeech.CustomPronunciationParams(
                    phrase=p.phrase, pronunciation=p.pronunciation, phonetic_encoding=texttospeech.CustomPronunciationParams.PhoneticEncoding.PHONETIC_ENCODING_JAPANESE_YOMIGANA
                )
                for p in self.custom_pronunciations.pronunciations
            ]
        )

    def to_talk_script_text(self, radio_casts: list[RadioCast] | None = None):
        if not radio_casts:
            return "\n".join([f"{s.radio_cast_id}: {s.content}" for s in self.scripts])

        m = {}
        for rc in radio_casts:
            m[rc.id] = rc.name

        for s in self.scripts:
            if s.radio_cast_id not in s:
                m[s.radio_cast_id] = s.radio_cast_id

        return "\n".join([f"{m[s.radio_cast_id]}: {s.content}" for s in self.scripts])
