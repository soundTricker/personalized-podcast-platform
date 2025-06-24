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
    McpListenerProgramSegmentUpdate,
)
from ppp.services.listener_program import ListenerProgramService
from ppp.services.listener_program_segment import ListenerProgramSegmentService

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


@router.post("/segments", response_model=List[ListenerProgramSegmentUnion], operation_id="update_listener_program_segments")
async def update_listener_program_segments(
    params: McpListenerProgramSegmentUpdate,
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    segment_service: ListenerProgramSegmentService = Depends(get_listener_program_segment_service),
) -> List[ListenerProgramSegment]:
    """
    Update segments for a listener program for MCP.

    This will:
    1. Update existing segments
    2. Create new segments
    3. Delete segments that are not in the provided list

    Args:
        params: McpListenerProgramSegmentUpdate update parameter body
    Returns:
        The updated list of segments
    """
    segments = params.segments
    listener_program_id = params.listener_program_id
    listener_id = params.listener_id

    # Verify that the program belongs to the listener
    program = await program_service.verify_program_ownership(listener_program_id, listener_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {listener_program_id} not found or you don't have permission to access it",
        )

    # Convert segments to dictionaries
    segment_dicts = [segment.model_dump(exclude_none=True) for segment in segments]

    # Update segments
    return await segment_service.update_segments(listener_program_id, listener_id, segment_dicts)
