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

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from ppp.models.listener_program_segment import ListenerProgramSegment
from ppp.schemas.listener_program_segment import (
    ListenerProgramSegmentUnion,
    ListenerProgramSegmentUpdateUnion,
)
from ppp.services.listener_program import ListenerProgramService
from ppp.services.listener_program_segment import ListenerProgramSegmentService
from ppp.utils.auth import get_current_user_id

router = APIRouter()


def get_listener_program_service() -> ListenerProgramService:
    """
    Dependency to get the ListenerProgramService.
    """
    return ListenerProgramService()


def get_listener_program_segment_service() -> ListenerProgramSegmentService:
    """
    Dependency to get the ListenerProgramSegmentService.
    """
    return ListenerProgramSegmentService()


@router.get("/{program_id}/segments", response_model=List[ListenerProgramSegmentUnion])
async def list_listener_program_segments(
    program_id: str,
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    segment_service: ListenerProgramSegmentService = Depends(get_listener_program_segment_service),
    user_id: str = Depends(get_current_user_id),
) -> List[ListenerProgramSegment]:
    """
    List all segments for a listener program.

    Only the owner of the program can retrieve its segments.
    """
    # Verify that the program belongs to the current user
    program = await program_service.verify_program_ownership(program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found or you don't have permission to access it",
        )

    # Get all segments for the program
    return await segment_service.get_segments_by_program_id(program_id)


@router.put("/{program_id}/segments", response_model=List[ListenerProgramSegmentUnion])
async def update_listener_program_segments(
    program_id: str,
    segments: List[ListenerProgramSegmentUpdateUnion],
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    segment_service: ListenerProgramSegmentService = Depends(get_listener_program_segment_service),
    user_id: str = Depends(get_current_user_id),
) -> List[ListenerProgramSegment]:
    """
    Update segments for a listener program.

    This will:
    1. Update existing segments
    2. Create new segments
    3. Delete segments that are not in the provided list

    Only the owner of the program can update its segments.
    """
    # Verify that the program belongs to the current user
    program = await program_service.verify_program_ownership(program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found or you don't have permission to access it",
        )

    # Convert segments to dictionaries
    segment_dicts = [segment.model_dump() for segment in segments]

    # Update segments
    return await segment_service.update_segments(program_id, user_id, segment_dicts)
