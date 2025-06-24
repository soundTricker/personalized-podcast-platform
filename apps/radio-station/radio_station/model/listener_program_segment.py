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
from typing import Annotated, TypeAlias

from pydantic import Field

from .base_model import BaseModel
from .listener import ListenerID
from .listener_program import ListenerProgramID
from .radio_cast import RadioCast


class SegmentType(str, Enum):
    RSS = "rss"
    # WEATHER = "weather"
    # SEARCH = "search"
    # TOOL = "tool"
    CALENDAR = "calendar"
    GMAIL = "gmail"
    WEB = "web"


ListenerProgramSegmentID: TypeAlias = int | str


class ListenerProgramSegment(BaseModel):
    """
    リスナープログラムのセグメントを表します。

    ListenerProgramSegmentクラスは、リスナープログラム内のセグメントに関する情報をカプセル化するように設計されています。
    このクラスは、適切にフォーマットされた有効なデータを確保するために、その属性に対して検証ルールを適用します。
    タイトル、説明、セグメントのタイプなどの詳細が含まれています。

    :ivar title: セグメントのタイトル。
    :type title: str
    :ivar description: セグメントの説明。提供されない場合のデフォルトはNoneです。
    :type description: str or None
    :ivar segment_type: セグメントのタイプ。
    :type segment_type: SegmentType
    """

    id: ListenerProgramSegmentID = Field(description="The ID of the listener program segment")
    listener_id: ListenerID | None = Field(description="The ID of the listener", default=None)
    listener_program_id: ListenerProgramID | None = Field(description="The ID of the listener program", default=None)

    title: str = Field(description="The title of the segment", max_length=100, min_length=1)
    description: str | None = Field(description="The description of the segment", max_length=1000, min_length=1, default=None)
    constraints: str | None = Field(description="The constraints of the segment", max_length=1000, min_length=0, default=None)

    segment_type: SegmentType = Field(description="The type of the segment", default=SegmentType.RSS)

    override_radio_casts: list[RadioCast] = Field(
        description="The list of radio casts to use in this segment, if it provided, the program base radio casts will be override in this segment.", default_factory=lambda: []
    )
    additional_guests: list[RadioCast] = Field(description="The additional radio casts to use in this segment.", default_factory=lambda: [])

    last_read_timestamp: float | None = Field(description="Last data read timestamp", default=None)


class ListenerProgramRSSSegment(ListenerProgramSegment):
    """
    リスナープログラム内のRSSセグメントを表します。

    このクラスは、セグメントの内容がRSSフィードから取得される特定のタイプのセグメントを定義およびモデル化するために使用されます。
    ListenerProgramSegmentベースクラスを継承しています。このクラスでは、`segment_type`は`SegmentType.RSS`として
    事前に定義されており、他のセグメントタイプと区別されます。さらに、RSSフィードのURLを格納するために使用される
    `feed_url`属性も含まれています。

    :ivar segment_type: セグメントのタイプ。このクラスでは常に`SegmentType.RSS`に設定されます。
    :type segment_type: SegmentType
    :ivar feed_url: このセグメントに関連付けられたRSSフィードのURL。
    :type feed_url: HttpUrl
    """

    segment_type: Annotated[SegmentType, Field()] = SegmentType.RSS
    feed_url: str = Field(description="The url of the feed")


class ListenerProgramCalendarSegment(ListenerProgramSegment):
    segment_type: Annotated[SegmentType, Field()] = SegmentType.CALENDAR
    start_offset_days: int = Field(description="The searching start offset days from now", default=0)
    end_offset_days: int = Field(description="The searching end offset days from now", default=0)
    calendar_id: str = Field(description="The name of the calendar", max_length=100, min_length=1)


class ListenerProgramWebSegment(ListenerProgramSegment):
    segment_type: Annotated[SegmentType, Field()] = SegmentType.WEB
    urls: list[str] = Field(description="The url of the web", default_factory=lambda: [])


class ListenerProgramGmailSegment(ListenerProgramSegment):
    segment_type: Annotated[SegmentType, Field()] = SegmentType.GMAIL
    filter: str = Field(description="The filter of the gmail query", max_length=100, min_length=1)
    start_offset_days: int = Field(description="The searching start offset days from now", default=0)
    end_offset_days: int = Field(description="The searching end offset days from now", default=0)


#
# class ListenerProgramWeatherSegment(ListenerProgramSegment):
#     """
#     リスナープログラムの天気セグメントを表します。
#
#     このクラスはListenerProgramSegmentを継承し、天気関連のセグメントに特化した
#     実装を提供します。天気セグメントの地理的位置を表すarea属性が含まれています。
#
#     :ivar segment_type: セグメントのタイプ、WEATHERに固定されています。
#     :type segment_type: SegmentType
#     :ivar area: 天気予報の地理的エリア。
#     :type area: str
#     """
#
#     segment_type: Annotated[SegmentType, Field()] = SegmentType.WEATHER
#     area: str = Field(description="The area of the weather")
