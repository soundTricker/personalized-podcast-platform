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

from typing import Dict, List, Type

from ppp.constants import GoogleApiScope
from ppp.models.listener_program_segment import (
    ListenerProgramCalendarSegment,
    ListenerProgramGmailSegment,
    ListenerProgramRSSSegment,
    ListenerProgramSegment,
    ListenerProgramWebSegment,
    SegmentType,
)
from ppp.services.listener import ListenerService
from ppp.services.listener_program import ListenerProgramService
from ppp.services.radio_cast import RadioCastService


class ListenerProgramSegmentService:
    """
    Service for ListenerProgramSegment CRUD operations.
    """

    def __init__(self):
        """
        Initialize the service with the ListenerProgramSegment model.
        """
        # Create a mapping of segment types to their respective models
        self.segment_type_to_model: Dict[SegmentType, Type[ListenerProgramSegment]] = {
            SegmentType.RSS: ListenerProgramRSSSegment,
            SegmentType.CALENDAR: ListenerProgramCalendarSegment,
            SegmentType.WEB: ListenerProgramWebSegment,
            SegmentType.GMAIL: ListenerProgramGmailSegment,
        }

    async def get_segments_by_program_id(self, program_id: str) -> List[ListenerProgramSegment]:
        """
        Get all segments for a specific program.

        Args:
            program_id: The ID of the program.

        Returns:
            A list of segments.
        """
        all_segments = []

        program = await ListenerProgramService().get_by_id(program_id)

        # For each segment type, get all segments for the program
        for segment_type, segment_model in self.segment_type_to_model.items():
            # Create a model for the specific program
            model_for_program = segment_model.model_for(program)
            # Find all segments of this type for the program
            segments = await model_for_program.find({"segmentType": segment_type})
            all_segments.extend(segments)

        # Sort segments by order
        all_segments.sort(key=lambda x: x.order)

        return all_segments

    async def update_segments(self, program_id: str, listener_id: str, segments: List[Dict]) -> List[ListenerProgramSegment]:
        """
        Update segments for a program. This will:
        1. Update existing segments
        2. Create new segments
        3. Delete segments that are not in the provided list

        Args:
            program_id: The ID of the program.
            listener_id: The ID of the listener.
            segments: A list of segment data.

        Returns:
            A list of updated segments.
        """

        listener_service = ListenerService()

        listener = await listener_service.get_listener_by_id(listener_id)

        if not listener:
            raise ValueError(f"Listener with ID {listener_id} not found")

        # Get all existing segments
        existing_segments = await self.get_segments_by_program_id(program_id)

        # Create a mapping of segment IDs to segments
        existing_segment_map = {segment.id: segment for segment in existing_segments}

        # Track which segments we've processed
        processed_segment_ids = set()

        # Updated segments to return
        updated_segments = []

        program = await ListenerProgramService().get_by_id(program_id)
        radio_cast_service = RadioCastService()

        # Process each segment in the input
        for segment_data in segments:
            segment_id = segment_data.get("id")
            segment_type = segment_data.get("segment_type")

            if segment_type not in self.segment_type_to_model:
                continue

            if segment_type == SegmentType.GMAIL:
                if GoogleApiScope.GmailReadOnly not in listener.scopes:
                    raise ValueError("listener does not have gmail read only scope")

            if segment_type == SegmentType.CALENDAR:
                if GoogleApiScope.CalendarReadOnly not in listener.scopes:
                    raise ValueError("listener does not have calendar read only scope")

            # Check if override_radio_casts exists and verify the radio casts exist
            override_radio_casts = segment_data.get("override_radio_casts")
            if override_radio_casts and isinstance(override_radio_casts, list) and len(override_radio_casts) > 0:
                # Verify that all radio casts exist
                existing_radio_casts = await radio_cast_service.get_radio_casts_by_ids(override_radio_casts)
                existing_radio_cast_ids = [cast.id for cast in existing_radio_casts]

                # Update override_radio_casts to only include existing radio casts
                segment_data["override_radio_casts"] = existing_radio_cast_ids

            # Get the appropriate model for this segment type
            segment_model = self.segment_type_to_model[segment_type]

            # Create a model for the specific program
            model_for_program = segment_model.model_for(program)

            # Add program_id and listener_id to the segment data
            segment_data["program_id"] = program_id
            segment_data["listener_id"] = listener_id

            if segment_id and segment_id in existing_segment_map:
                # Update existing segment
                existing_segment = existing_segment_map[segment_id]

                # Update fields
                for key, value in segment_data.items():
                    if key != "id" and value is not None:
                        setattr(existing_segment, key, value)

                await existing_segment.save()
                updated_segments.append(existing_segment)
                processed_segment_ids.add(segment_id)
            else:
                # Create new segment
                segment = model_for_program(**segment_data)
                await segment.save()
                updated_segments.append(segment)
                if segment_id:
                    processed_segment_ids.add(segment_id)

        # Delete segments that weren't in the input
        for segment_id, segment in existing_segment_map.items():
            if segment_id not in processed_segment_ids:
                await segment.delete()

        # Sort segments by order
        updated_segments.sort(key=lambda x: x.order)

        return updated_segments


def get_listener_program_segment_service() -> ListenerProgramSegmentService:
    return ListenerProgramSegmentService()
