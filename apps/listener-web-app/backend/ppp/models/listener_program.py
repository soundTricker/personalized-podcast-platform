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

from datetime import datetime
from enum import Enum
from random import randint

from pydantic import model_validator
from typing_extensions import Self

from ppp.models.base import BaseModel


class ProgramStatus(str, Enum):
    """
    Enum representing the status of a listener program.
    """

    DRAFT = "draft"
    ACTIVE = "active"
    PAUSE = "pause"


class BroadcastSchedule(str, Enum):
    """
    Enum representing the broadcast schedule of a listener program.
    """

    DAILY = "daily"
    WEEKLY = "weekly"


class PublishSetting(str, Enum):
    """
    Enum representing the publish setting of a listener program.
    """

    PRIVATE = "private"
    LIMITED = "limited"
    PUBLISH = "publish"


class ListenerProgram(BaseModel):
    """
    Listener Program model representing a podcast program created by a listener.

    This model is used to store information about podcast programs in Firestore.
    """

    __collection__ = "listener_programs"

    # Program information
    title: str
    description: str
    listener_id: str  # Reference to Listener.id
    pro_mode: bool = False

    # Program details
    program_minutes: int = 10  # Default 10 minutes (renamed from duration_minutes)
    insert_music: bool = True  # Whether to insert music into the program
    base_radio_cast_ids: list[str] = []  # The radio casts that the program will listen

    # Broadcast settings
    broadcast_schedule: BroadcastSchedule = BroadcastSchedule.DAILY
    broadcast_dayofweek: list[str] = []  # Days of week for weekly broadcast

    # Status
    status: ProgramStatus = ProgramStatus.DRAFT
    publish_setting: PublishSetting = PublishSetting.PRIVATE
    private_key: str | None = None  # Private key for limited access (32+ characters)

    number_of_broadcast: int = 0

    # Cover art
    cover_art_uri: str | None = None  # URI for podcast cover art (gs:// format)

    # Additional timestamps
    published_at: datetime | None = None

    last_broadcasted_at: datetime | None = None

    tts_seed: int | None = None

    @model_validator(mode="after")
    def validate_private_key(self) -> Self:
        if self.publish_setting == PublishSetting.PRIVATE or self.publish_setting == PublishSetting.PUBLISH:
            return self

        if self.private_key is None:
            raise ValueError("private key is needed on limited setting")

        if len(self.private_key) < 32:
            raise ValueError("Private key must be at least 32 characters long")
        return self

    @model_validator(mode="after")
    def set_tts_seed(self) -> Self:
        if self.tts_seed is None:
            self.tts_seed = randint(0, 2147483647 - 1)
        return self
