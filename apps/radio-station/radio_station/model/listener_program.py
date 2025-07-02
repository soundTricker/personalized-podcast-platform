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
from random import randint
from typing import List, Optional, Self, TypeAlias

from pydantic import Field, model_validator

from .base_model import BaseModel
from .listener import ListenerID
from .radio_cast import RadioCast

ListenerProgramID: TypeAlias = str | int


class ListenerProgram(BaseModel):
    """
    The radio program setting that the listener wants to make.
    """

    id: ListenerProgramID = Field(description="The ID of the listener program")
    listener_id: ListenerID = Field(description="The ID of the listener")
    title: str = Field(description="The title of the program", max_length=100, min_length=1)
    description: str = Field(description="The description of the program", max_length=1000, min_length=1)
    program_minutes: int = Field(description="The number of minutes that the program will listen", ge=5)
    insert_music: bool = Field(description="Whether to insert music into the program", default=True)
    number_of_broadcast: int = Field(description="The number of broadcast this program", default=0)
    pro_mode: bool = Field(description="Pro Mode", default=False)
    tts_seed: Optional[int] = Field(description="Seed value for TTS model", default=None)

    base_radio_casts: List[RadioCast] = Field(description="The radio casts that the program will listen", default=[])

    def to_llm_text(self):
        return f"""
=====
Program Title: {self.title}
Program Description: {self.description}
Number OF Broadcast this Program: {self.number_of_broadcast}
Program Minutes: {self.program_minutes} minutes
Insert Music: {self.insert_music}
Main Radio Casts:
{"\n".join([rc.to_llm_text() for rc in self.base_radio_casts]) if self.base_radio_casts else ""}
=====
        """

    @model_validator(mode="after")
    def set_tts_seed(self) -> Self:
        if self.tts_seed is None or self.tts_seed > 2147483647:
            self.tts_seed = randint(0, 2147483647 - 1)
        return self
