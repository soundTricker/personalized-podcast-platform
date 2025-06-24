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

from typing import Annotated, Any, List, Optional, Union

from pydantic import BaseModel, Discriminator, Field, Tag

from ppp.models.listener_program_segment import (
    SegmentType,
)
from ppp.schemas.base import Base, BaseCreateSchema, BaseSchema, BaseUpdateSchema


class ListenerProgramSegmentSchema(BaseSchema):
    """
    Base schema for ListenerProgramSegment response.
    """

    title: str = Field(description="番組コーナーのタイトル")
    description: Optional[str] = Field(None, description="番組コーナーの説明")
    constraints: Optional[str] = Field(None, description="番組コーナーの制約条件（例：「定例は除く」「政治的な内容は除く」「AIについては話さない」「最終更新日以降の情報だけ取得する」等）")
    program_id: str = Field(description="番組ID")
    listener_id: str = Field(description="リスナーID")
    order: int = Field(description="番組コーナーの順序")
    segment_type: SegmentType = Field(description="番組コーナー分類")
    override_radio_casts: List[str] = Field(default_factory=list, description="このコーナーだけ異なるラジオパーソナリティーが話す場合に設定")
    last_read_timestamp: Optional[float] = Field(None, description="最終読み取りタイムスタンプ")


class ListenerProgramRSSSegmentSchema(ListenerProgramSegmentSchema):
    """
    Schema for ListenerProgramRSSSegment response.
    """

    segment_type: SegmentType = SegmentType.RSS
    feed_url: str = Field(description="RSS FeedのURL")


class ListenerProgramCalendarSegmentSchema(ListenerProgramSegmentSchema):
    """
    Schema for ListenerProgramCalendarSegment response.
    """

    segment_type: SegmentType = SegmentType.CALENDAR
    start_offset_days: int = Field(description="検索開始日 現在日からのオフセット日数")
    end_offset_days: int = Field(description="検索終了日 現在日からのオフセット日数")
    calendar_id: str = Field(description="予定を取得するGoogle Calendarのcalendar id（基本的にはprimaryを設定）")


class ListenerProgramWebSegmentSchema(ListenerProgramSegmentSchema):
    """
    Schema for ListenerProgramWebSegment response.
    """

    segment_type: SegmentType = SegmentType.WEB
    urls: List[str] = Field(default_factory=list, description="URLのリスト")


class ListenerProgramGmailSegmentSchema(ListenerProgramSegmentSchema):
    """
    Schema for ListenerProgramGmailSegment response.
    """

    segment_type: SegmentType = SegmentType.GMAIL
    filter: str = Field(description="Gmailのクエリ")
    start_offset_days: int = Field(description="検索開始日 現在日からのオフセット日数")
    end_offset_days: int = Field(description="検索終了日 現在日からのオフセット日数")


def listener_program_segment_descriptor(v: Any) -> str | None:
    if isinstance(v, Base) or isinstance(v, BaseModel):
        v = v.model_dump()

    if isinstance(v, dict):
        segment_type = v.get("segmentType")
        if not segment_type:
            segment_type = v.get("segment_type")
    else:
        return None
    if isinstance(segment_type, SegmentType):
        return segment_type.value
    else:
        return str(segment_type)


# Union type for all segment types
ListenerProgramSegmentUnion = Annotated[
    Union[
        Annotated[ListenerProgramRSSSegmentSchema, Tag("rss")],
        Annotated[ListenerProgramCalendarSegmentSchema, Tag("calendar")],
        Annotated[ListenerProgramWebSegmentSchema, Tag("web")],
        Annotated[ListenerProgramGmailSegmentSchema, Tag("gmail")],
    ],
    Discriminator(listener_program_segment_descriptor),
]


# Create schemas
class ListenerProgramSegmentCreateBase(BaseCreateSchema):
    """
    Base schema for creating a ListenerProgramSegment.
    """

    title: str = Field(description="番組コーナーのタイトル", max_length=100, min_length=1)
    description: Optional[str] = Field(description="番組コーナーの説明", max_length=1000, min_length=1, default=None)
    constraints: Optional[str] = Field(
        description="番組コーナーの制約条件（例：「定例は除く」「政治的な内容は除く」「AIについては話さない」「最終更新日以降の情報だけ取得する」等）", max_length=1000, default=None
    )
    order: int = Field(description="番組コーナーの順序")
    override_radio_casts: List[str] = Field(default_factory=list, description="このコーナーだけ異なるラジオパーソナリティーが話す場合に設定")


class ListenerProgramRSSSegmentCreate(ListenerProgramSegmentCreateBase):
    """
    Schema for creating a ListenerProgramRSSSegment.
    """

    segment_type: SegmentType = SegmentType.RSS
    feed_url: str = Field(description="RSS FeedのURL")


class ListenerProgramCalendarSegmentCreate(ListenerProgramSegmentCreateBase):
    """
    Schema for creating a ListenerProgramCalendarSegment.
    """

    segment_type: SegmentType = SegmentType.CALENDAR
    start_offset_days: int = Field(description="検索開始日 現在日からのオフセット日数", default=0)
    end_offset_days: int = Field(description="検索終了日 現在日からのオフセット日数", default=0)
    calendar_id: str = Field(description="予定を取得するGoogle Calendarのcalendar id（基本的にはprimaryを設定）", max_length=100, min_length=1)


class ListenerProgramWebSegmentCreate(ListenerProgramSegmentCreateBase):
    """
    Schema for creating a ListenerProgramWebSegment.
    """

    segment_type: SegmentType = SegmentType.WEB
    urls: List[str] = Field(description="URLのリスト", default_factory=list)


class ListenerProgramGmailSegmentCreate(ListenerProgramSegmentCreateBase):
    """
    Schema for creating a ListenerProgramGmailSegment.
    """

    segment_type: SegmentType = SegmentType.GMAIL
    filter: str = Field(description="Gmailのクエリ", max_length=100, min_length=1)
    start_offset_days: int = Field(description="検索開始日 現在日からのオフセット日数", default=0)
    end_offset_days: int = Field(description="検索終了日 現在日からのオフセット日数", default=0)


# Union type for all segment create types
ListenerProgramSegmentCreateUnion = Annotated[
    Union[
        Annotated[ListenerProgramRSSSegmentCreate, Tag("rss")],
        Annotated[ListenerProgramCalendarSegmentCreate, Tag("calendar")],
        Annotated[ListenerProgramWebSegmentCreate, Tag("web")],
        Annotated[ListenerProgramGmailSegmentCreate, Tag("gmail")],
    ],
    Discriminator(listener_program_segment_descriptor),
]


# Update schemas
class ListenerProgramSegmentUpdateBase(BaseUpdateSchema):
    """
    Base schema for updating a ListenerProgramSegment.
    """

    title: Optional[str] = Field(description="番組コーナーのタイトル", max_length=100, min_length=1, default=None)
    description: Optional[str] = Field(description="番組コーナーの説明", max_length=1000, min_length=1, default=None)
    constraints: Optional[str] = Field(
        description="番組コーナーの制約条件（例：「定例は除く」「政治的な内容は除く」「AIについては話さない」「最終更新日以降の情報だけ取得する」等）", max_length=1000, min_length=0, default=None
    )
    order: Optional[int] = Field(description="番組コーナーの順序", default=None)
    override_radio_casts: Optional[List[str]] = Field(None, description="このコーナーだけ異なるラジオパーソナリティーが話す場合に設定")


class ListenerProgramRSSSegmentUpdate(ListenerProgramSegmentUpdateBase):
    """
    Schema for updating a ListenerProgramRSSSegment.
    """

    segment_type: SegmentType = SegmentType.RSS
    feed_url: Optional[str] = Field(description="RSS FeedのURL", default=None)


class ListenerProgramCalendarSegmentUpdate(ListenerProgramSegmentUpdateBase):
    """
    Schema for updating a ListenerProgramCalendarSegment.
    """

    segment_type: SegmentType = SegmentType.CALENDAR
    start_offset_days: Optional[int] = Field(description="検索開始日 現在日からのオフセット日数", default=None)
    end_offset_days: Optional[int] = Field(description="検索終了日 現在日からのオフセット日数", default=None)
    calendar_id: Optional[str] = Field(description="予定を取得するGoogle Calendarのcalendar id（基本的にはprimaryを設定）", max_length=100, min_length=1, default=None)


class ListenerProgramWebSegmentUpdate(ListenerProgramSegmentUpdateBase):
    """
    Schema for updating a ListenerProgramWebSegment.
    """

    segment_type: SegmentType = SegmentType.WEB
    urls: Optional[List[str]] = Field(description="URLのリスト", default=None)


class ListenerProgramGmailSegmentUpdate(ListenerProgramSegmentUpdateBase):
    """
    Schema for updating a ListenerProgramGmailSegment.
    """

    segment_type: SegmentType = SegmentType.GMAIL
    filter: Optional[str] = Field(description="Gmailのクエリ", max_length=100, min_length=1, default=None)
    start_offset_days: Optional[int] = Field(description="検索開始日 現在日からのオフセット日数", default=None)
    end_offset_days: Optional[int] = Field(description="検索終了日 現在日からのオフセット日数", default=None)


class McpListenerProgramSegmentUpdateModel(ListenerProgramRSSSegmentUpdate, ListenerProgramCalendarSegmentUpdate, ListenerProgramWebSegmentUpdate, ListenerProgramGmailSegmentUpdate):
    segment_type: SegmentType = Field(description="番組コーナー分類")
    title: str = Field(description="番組コーナーのタイトル")
    description: str = Field(description="番組コーナーの説明")
    constraints: Optional[str] = Field(None, description="番組コーナーの制約条件（例：「定例は除く」「政治的な内容は除く」「AIについては話さない」「最終更新日以降の情報だけ取得する」等）")
    program_id: str = Field(description="番組ID")
    listener_id: str = Field(description="リスナーID")
    order: int = Field(description="番組コーナーの順序")
    override_radio_casts: List[str] = Field(default_factory=list, description="このコーナーだけ異なるラジオパーソナリティーが話す場合に設定")
    last_read_timestamp: Optional[float] = Field(None, description="最終読み取りタイムスタンプ")


# Union type for all segment update types
ListenerProgramSegmentUpdateUnion = Annotated[
    Union[
        Annotated[ListenerProgramRSSSegmentUpdate, Tag("rss")],
        Annotated[ListenerProgramCalendarSegmentUpdate, Tag("calendar")],
        Annotated[ListenerProgramWebSegmentUpdate, Tag("web")],
        Annotated[ListenerProgramGmailSegmentUpdate, Tag("gmail")],
    ],
    Discriminator(listener_program_segment_descriptor),
]


class McpListenerProgramSegmentUpdate(Base):
    listener_id: str = Field(description="listener id")
    listener_program_id: str = Field(description="listener program id")
    segments: List[McpListenerProgramSegmentUpdateModel] = Field(description="list of segments", default_factory=list)
