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
from typing import Annotated

from firedantic import AsyncSubCollection
from pydantic import Field

from ppp.models.base import BaseSubModel


class SegmentType(str, Enum):
    """
    Enum representing the types of segments available in a listener program.
    """

    RSS = "rss"
    CALENDAR = "calendar"
    GMAIL = "gmail"
    WEB = "web"


class ListenerProgramSegment(BaseSubModel):
    """
    Listener Program Segment model representing a segment within a podcast program.

    This model is used to store information about podcast program segments in Firestore.
    Each program can have multiple segments.
    """

    # Segment information
    title: str = Field(description="The title of the segment", max_length=100, min_length=1)
    description: str | None = Field(description="The description of the segment", max_length=1000, min_length=1, default=None)
    constraints: str | None = Field(description="The constraints of the segment", max_length=1000, default=None)
    program_id: str = Field(description="Reference to ListenerProgram.id")
    listener_id: str = Field(description="The ID of the listener")

    # Segment details
    order: int = Field(description="Order of the segment in the program")
    segment_type: SegmentType = Field(description="The type of the segment")

    # Radio cast information
    override_radio_casts: list[str] = Field(
        description="The list of radio cast IDs to use in this segment, if provided, the program base radio casts will be overridden in this segment.", default_factory=lambda: []
    )
    last_read_timestamp: float | None = Field(description="Last data read timestamp", default=None)

    class Collection(AsyncSubCollection):
        __collection_tpl__ = "listener_programs/{id}/segments"


class ListenerProgramRSSSegment(ListenerProgramSegment):
    """
    Listener Program RSS Segment model representing an RSS feed segment.
    """

    segment_type: Annotated[SegmentType, Field()] = SegmentType.RSS
    feed_url: str = Field(alias="feedUrl", description="The URL of the RSS feed")


class ListenerProgramCalendarSegment(ListenerProgramSegment):
    """
    Listener Program Calendar Segment model representing a calendar segment.
    """

    segment_type: Annotated[SegmentType, Field()] = SegmentType.CALENDAR
    start_offset_days: int = Field(description="The searching start offset days from now", default=0)
    end_offset_days: int = Field(description="The searching end offset days from now", default=0)
    calendar_id: str = Field(description="The ID of the calendar", max_length=100, min_length=1)


class ListenerProgramWebSegment(ListenerProgramSegment):
    """
    Listener Program Web Segment model representing a web content segment.
    """

    segment_type: Annotated[SegmentType, Field()] = SegmentType.WEB
    urls: list[str] = Field(description="The URLs of the web content", default_factory=lambda: [])


class ListenerProgramGmailSegment(ListenerProgramSegment):
    """
    Listener Program Gmail Segment model representing a Gmail segment.
    """

    segment_type: Annotated[SegmentType, Field()] = SegmentType.GMAIL
    filter: str = Field(description="The filter of the Gmail query", max_length=100, min_length=1)
    start_offset_days: int = Field(description="The searching start offset days from now", default=0)
    end_offset_days: int = Field(description="The searching end offset days from now", default=0)
