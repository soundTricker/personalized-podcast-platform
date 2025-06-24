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
from typing import List

from pydantic import Field

from .base_model import BaseModel
from .listener import ListenerID
from .listener_program import ListenerProgramID
from .listener_program_segment import ListenerProgramSegmentID
from .radio_cast import RadioCast


class SegmentType(Enum):
    OPENING = "opening"
    CONTENT = "content"
    MUSIC = "music"
    ENDING = "ending"

class SegmentPlan(BaseModel):
    title: str = Field(description="The title of the segment or music name")
    program_segment_ids: List[ListenerProgramSegmentID] = Field(description="Must. Array of referenced research result's `id` attribute value that were used to create this segment. "
                                                                            "For music segments between content, use an empty array. "
                                                                            "For music within a content segment, include the research result id")
    segment_no: int|None = Field(description="The number of the segment that this segment belongs to", default=None)
    segment_seconds:float = Field(description="The length of the segment in seconds")
    is_music: bool = Field(description="Boolean indicating if this is a music segment (true) or content segment (false)")
    description: str = Field(description="Description of the segment content or music")
    constraints: str|None = Field(description="Constraints from the segment plan", default=None)
    segment_type: SegmentType = Field(description="Segment type, `opening` is the first segment, `ending` is the last segment. `content` is not opening and not ending, music segment set 'music'")
    background_music: str|None = Field(description="Background music image text", default=None)
    radio_casts: list[RadioCast] = Field(description="Radio cast list", default_factory=lambda: [])

    music_bpm: float|None =Field(description="bpm of the music", default=None)


    def to_llm_text(self):
        return f"""=====
Segment Title: {self.title}
Segment No: {self.segment_no}
Segment Description: {self.description}
Music Segment: {self.is_music}
Segment Constraints: {self.constraints}
Segment Type: {self.segment_type}
Background Music: {self.background_music}
Segment Seconds: {self.segment_seconds} sec
Radio Casts:
{'\n'.join([radio_cast.to_llm_text() for radio_cast in self.radio_casts]) if self.radio_casts else ''}
====="""


class ProgramPlan(BaseModel):
    title: str = Field(description="The title of the program")
    listener_id: ListenerID|None = Field(description="Listener ID",default=None)
    listener_program_id: ListenerProgramID|None = Field(description="Listener Program ID",default=None)
    description: str = Field(description="Description of the program")

    program_seconds: int = Field(description="Program duration in seconds")

    segments: List[SegmentPlan] = Field(description="Program segments")

    def to_llm_text(self, include_segments=True):

        return f"""
===
Program Title: {self.title}
Program Description: {self.description}
Program Seconds: {self.program_seconds} sec
{('Segments:\n' + '\n'.join([segment.to_llm_text() for segment in self.segments])) if include_segments else ''}
===
        """
