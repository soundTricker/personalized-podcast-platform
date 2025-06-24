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
from typing import List, Optional

from fastapi import HTTPException, status
from pydantic import BaseModel, Field, ValidationInfo, field_validator

from ppp.models.radio_cast import RadioCastRole
from ppp.schemas.base import BaseCreateSchema, BaseSchema, BaseUpdateSchema
from ppp.utils.inspector import run_inspection


class VoiceName(str, Enum):
    BRIGHT = "Bright"
    UPBEAT = "Upbeat"
    INFORMATIVE = "Informative"
    FIRM = "Firm"
    EXCITABLE = "Excitable"
    YOUTHFUL = "Youthful"
    BREEZY = "Breezy"
    EASY = "Easy"
    BREATHY = "Breathy"
    CLEAR = "Clear"
    SMOOTH = "Smooth"
    GRAVELLY = "Gravelly"
    SOFT = "Soft"
    EVEN = "Even"
    MATURE = "Mature"
    FORWARD = "Forward"
    FRIENDLY = "Friendly"
    CASUAL = "Casual"
    GENTLE = "Gentle"
    LIVELY = "Lively"
    KNOWLEDGEABLE = "Knowledgeable"
    WARM = "Warm"


class RadioCastSchema(BaseSchema):
    """
    Schema for RadioCast response.
    """

    name: str
    listener_id: Optional[str] = None
    role: RadioCastRole = RadioCastRole.RadioPersonality
    voice_name: Optional[str] = None
    personality: Optional[str] = None


class RadioCastCreateSchema(BaseCreateSchema):
    """
    Schema for creating a RadioCast.
    """

    name: str = Field(description="Radio cast name", min_length=1, max_length=100)
    role: RadioCastRole = RadioCastRole.RadioPersonality
    voice_name: VoiceName = Field(description="For Google GenAI voice")
    personality: str = Field(description="Personality", min_length=1, max_length=500)

    @field_validator("name", "personality")
    @classmethod
    def validate_inspection(cls, value: str, config: ValidationInfo) -> str:
        result = run_inspection({config.field_name: value})
        if not result.valid:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail={"errorCode": "inspection", "key": config.field_name, "msg": str(result)})
        return value


class RadioCastUpdateSchema(BaseUpdateSchema):
    """
    Schema for updating a RadioCast.
    """

    name: Optional[str] = None
    role: Optional[RadioCastRole] = None
    voice_name: Optional[str] = None
    personality: Optional[str] = None

    @field_validator("name", "personality")
    @classmethod
    def validate_inspection(cls, value: str | None, config: ValidationInfo) -> str | None:
        if not value:
            return value

        result = run_inspection({config.field_name: value})
        if not result.valid:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail={"errorCode": "inspection", "key": config.field_name, "msg": str(result)})
        return value


class RadioCastIdsSchema(BaseModel):
    """
    Schema for requesting multiple radio casts by their IDs.
    """

    radio_cast_ids: List[str] = Field(description="List of radio cast IDs to retrieve")
