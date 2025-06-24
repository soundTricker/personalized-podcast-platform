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
from typing import List, Optional

from fastapi import HTTPException, status
from pydantic import Field, ValidationInfo, field_validator, model_validator
from typing_extensions import Self

from ppp.models.listener_program import BroadcastSchedule, ProgramStatus, PublishSetting
from ppp.schemas.base import BaseCreateSchema, BaseSchema, BaseUpdateSchema
from ppp.utils.inspector import run_inspection


class ListenerProgramSchema(BaseSchema):
    """
    Schema for ListenerProgram response.
    """

    title: str = Field(description="ラジオ番組のタイトル")
    description: str = Field(description="ラジオ番組の説明")
    listener_id: str = Field(description="リスナーID")
    program_minutes: int = Field(description="ラジオ番組の分数（10分、15分、20分、30分から選択）")
    insert_music: bool = Field(description="音楽コーナーを作成するかどうか")
    base_radio_cast_ids: List[str] = Field(description="ラジオパーソナリティのIDリスト（最大2人まで）")
    broadcast_schedule: BroadcastSchedule = Field(description="配信スケジュール（日毎、週ごと）")
    broadcast_dayofweek: List[str] = Field(description="週ごと配信の場合の配信曜日リスト（monday,tuesday,wednesday,thursday,friday,saturday,sundayのいずれか）")
    status: ProgramStatus = Field(description="番組ステータス（draft,active,pause）")
    publish_setting: PublishSetting = Field(description="公開設定（private:非公開、limited:限定公開、publish:公開）")
    private_key: Optional[str] = Field(None, description="限定公開用のプライベートキー（32文字以上）")
    published_at: Optional[datetime] = Field(None, description="公開日時")
    number_of_broadcast: int = Field(0, description="配信回数")


class ListenerProgramCreateSchema(BaseCreateSchema):
    """
    Schema for creating a ListenerProgram.
    """

    title: str = Field(description="ラジオ番組のタイトル", max_length=100, min_length=1)
    description: str = Field(description="ラジオ番組の説明", max_length=1000, min_length=1)
    program_minutes: int = Field(description="ラジオ番組の分数（10分、15分、20分、30分から選択）")
    insert_music: bool = Field(True, description="音楽コーナーを作成するかどうか")
    base_radio_cast_ids: List[str] = Field(default_factory=list, description="ラジオパーソナリティのIDリスト（最大2人まで）", min_items=1, max_items=2)
    broadcast_schedule: BroadcastSchedule = Field(BroadcastSchedule.DAILY, description="配信スケジュール（daily:日毎、weekly:週ごと）")
    broadcast_dayofweek: List[str] = Field(default_factory=list, description="週ごと配信の場合の配信曜日リスト（monday,tuesday,wednesday,thursday,friday,saturday,sundayのいずれか）")
    status: ProgramStatus = Field(ProgramStatus.DRAFT, description="番組ステータス（draft:下書き、active:アクティブ、pause:一時停止）")
    publish_setting: PublishSetting = Field(PublishSetting.PRIVATE, description="公開設定（private:非公開、limited:限定公開、publish:公開）")
    private_key: Optional[str] = Field(None, description="限定公開用のプライベートキー（32文字以上、limited設定時に必須）")

    @model_validator(mode="after")
    def validate_private_key(self) -> Self:
        if self.publish_setting == PublishSetting.PRIVATE or self.publish_setting == PublishSetting.PUBLISH:
            return self

        if self.private_key is None:
            raise ValueError("private key is needed on limited setting")

        if len(self.private_key) < 32:
            raise ValueError("Private key must be at least 32 characters long")
        return self

    @field_validator("title", "description")
    @classmethod
    def validate_inspection(cls, value: str | None, config: ValidationInfo) -> str | None:
        result = run_inspection({config.field_name: value})
        if not result.valid:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail={"errorCode": "inspection", "key": config.field_name, "msg": str(result)})
        return value


class ListenerProgramMCPCreateSchema(ListenerProgramCreateSchema):
    """
    Schema for creating a ListenerProgram with MCP.
    """

    private_key: str = Field(description="限定公開用のプライベートキー（32文字以上、limited設定時に必須）", min_length=0, default="")

    @model_validator(mode="after")
    def validate_private_key(self) -> Self:
        if self.publish_setting == PublishSetting.PRIVATE or self.publish_setting == PublishSetting.PUBLISH:
            return self

        if self.private_key == "":
            raise ValueError("private key is needed on limited setting")

        if len(self.private_key) < 32:
            raise ValueError("Private key must be at least 32 characters long")
        return self

    @field_validator("title", "description")
    @classmethod
    def validate_inspection(cls, value: str | None, config: ValidationInfo) -> str | None:
        result = run_inspection({config.field_name: value})
        if not result.valid:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail={"errorCode": "inspection", "key": config.field_name, "msg": str(result)})
        return value


class ListenerProgramUpdateSchema(BaseUpdateSchema):
    """
    Schema for updating a ListenerProgram.
    """

    title: Optional[str] = Field(None, description="ラジオ番組のタイトル")
    description: Optional[str] = Field(None, description="ラジオ番組の説明")
    program_minutes: Optional[int] = Field(None, description="ラジオ番組の分数（10分、15分、20分、30分から選択）")
    insert_music: Optional[bool] = Field(None, description="音楽コーナーを作成するかどうか")
    base_radio_cast_ids: Optional[List[str]] = Field(None, description="ラジオパーソナリティのIDリスト（最大2人まで）", min_items=1, max_items=2)
    broadcast_schedule: Optional[BroadcastSchedule] = Field(None, description="配信スケジュール（daily:日毎、weekly:週ごと）")
    broadcast_dayofweek: Optional[List[str]] = Field(None, description="週ごと配信の場合の配信曜日リスト（monday,tuesday,wednesday,thursday,friday,saturday,sundayのいずれか）")
    status: Optional[ProgramStatus] = Field(None, description="番組ステータス（draft:下書き、active:アクティブ、pause:一時停止）")
    publish_setting: Optional[PublishSetting] = Field(None, description="公開設定（private:非公開、limited:限定公開、publish:公開）")
    private_key: Optional[str] = Field(None, description="限定公開用のプライベートキー（32文字以上、limited設定時に必須）")
    published_at: Optional[datetime] = Field(None, description="公開日時")

    @field_validator("title", "description")
    @classmethod
    def validate_inspection(cls, value: str | None, config: ValidationInfo) -> str | None:
        result = run_inspection({config.field_name: value})
        if not result.valid:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail={"errorCode": "inspection", "key": config.field_name, "msg": str(result)})
        return value

    @model_validator(mode="after")
    def validate_private_key(self) -> Self:
        if self.publish_setting is None or self.publish_setting == PublishSetting.PRIVATE or self.publish_setting == PublishSetting.PUBLISH:
            return self

        if self.private_key is None:
            raise ValueError("private key is needed on limited setting")

        if len(self.private_key) < 32:
            raise ValueError("Private key must be at least 32 characters long")
        return self
