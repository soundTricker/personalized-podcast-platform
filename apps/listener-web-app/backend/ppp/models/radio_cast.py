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

from ppp.models.base import BaseModel


class RadioCastRole(str, Enum):
    RadioPersonality = "radio personality"
    Assistant = "assistant"
    Guest = "guest"


class RadioCast(BaseModel):
    """
    Radio Cast model representing a cast (speaker) for a podcast.

    This model is used to store information about podcast casts in Firestore.
    """

    __collection__ = "radio_casts"

    # Cast information
    name: str
    listener_id: str | None  # Reference to Listener.id who created this cast, when it is none, this radio_cast is pre-defined radio cast
    role: RadioCastRole = RadioCastRole.RadioPersonality

    # Cast details
    voice_name: str | None = None  # For Google GenAI voice
    personality: str | None = None

    @classmethod
    async def find_predefined_radio_casts(cls) -> list["RadioCast"]:
        return await cls.find({"listenerId": None})
