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
from fastapi.responses import StreamingResponse

from ppp.models.listener_program import ListenerProgram
from ppp.schemas.listener_program import (
    ListenerProgramCreateSchema,
    ListenerProgramSchema,
    ListenerProgramUpdateSchema,
)
from ppp.services.listener_program import ListenerProgramService, get_listener_program_service
from ppp.services.radio import RadioService, get_radio_service
from ppp.utils.auth import get_current_user_id

router = APIRouter()


@router.post("/", response_model=ListenerProgramSchema, status_code=status.HTTP_201_CREATED)
async def create_listener_program(
    listener_program: ListenerProgramCreateSchema,
    service: ListenerProgramService = Depends(get_listener_program_service),
    user_id: str = Depends(get_current_user_id),
) -> ListenerProgram:
    """
    Create a new listener program.
    """

    return await service.create_listener_program(
        title=listener_program.title,
        description=listener_program.description,
        listener_id=user_id,  # Use user_id from get_current_user_id
        program_minutes=listener_program.program_minutes,
        insert_music=listener_program.insert_music,
        base_radio_cast_ids=listener_program.base_radio_cast_ids,
        status=listener_program.status,
        publish_setting=listener_program.publish_setting,
        private_key=listener_program.private_key,
        cover_art_uri=listener_program.cover_art_uri,
    )


@router.get("/{listener_program_id}", response_model=ListenerProgramSchema)
async def get_listener_program(
    listener_program_id: str,
    service: ListenerProgramService = Depends(get_listener_program_service),
    user_id: str = Depends(get_current_user_id),
) -> ListenerProgram:
    """
    Get a listener program by ID.

    Only the owner of the program can retrieve it.
    """
    # Verify that the program belongs to the current user
    program = await service.verify_program_ownership(listener_program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {listener_program_id} not found or you don't have permission to access it",
        )
    return program


@router.get("/", response_model=List[ListenerProgramSchema])
async def list_listener_programs(
    service: ListenerProgramService = Depends(get_listener_program_service),
    user_id: str = Depends(get_current_user_id),
) -> List[ListenerProgram]:
    """
    List listener programs for the current user.
    """
    return await service.get_listener_programs_by_listener_id(user_id)


@router.put("/{listener_program_id}", response_model=ListenerProgramSchema)
async def update_listener_program(
    listener_program_id: str,
    listener_program: ListenerProgramUpdateSchema,
    service: ListenerProgramService = Depends(get_listener_program_service),
    user_id: str = Depends(get_current_user_id),
) -> ListenerProgram:
    """
    Update a listener program.

    Only the owner of the program can update it.
    """
    # Verify that the program belongs to the current user
    program = await service.verify_program_ownership(listener_program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {listener_program_id} not found or you don't have permission to update it",
        )

    updated_program = await service.update_listener_program(
        id=listener_program_id,
        title=listener_program.title,
        description=listener_program.description,
        program_minutes=listener_program.program_minutes,
        insert_music=listener_program.insert_music,
        base_radio_cast_ids=listener_program.base_radio_cast_ids,
        status=listener_program.status,
        publish_setting=listener_program.publish_setting,
        private_key=listener_program.private_key,
        published_at=listener_program.published_at,
        cover_art_uri=listener_program.cover_art_uri,
        broadcast_schedule=listener_program.broadcast_schedule,
        broadcast_dayofweek=listener_program.broadcast_dayofweek,
    )

    return updated_program


@router.delete("/{listener_program_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_listener_program(
    listener_program_id: str,
    service: ListenerProgramService = Depends(get_listener_program_service),
    user_id: str = Depends(get_current_user_id),
) -> None:
    """
    Delete a listener program.

    Only the owner of the program can delete it.
    """
    # Verify that the program belongs to the current user
    program = await service.verify_program_ownership(listener_program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {listener_program_id} not found or you don't have permission to delete it",
        )

    await service.delete(listener_program_id)


@router.post("/{listener_program_id}/generate-podcast")
async def generate_podcast(
    listener_program_id: str,
    dry_run: bool = False,
    radio_service: RadioService = Depends(get_radio_service),
    user_id: str = Depends(get_current_user_id),
) -> StreamingResponse:
    """
    Generate a podcast for a listener program.

    If dry_run is True, the podcast will be generated but no changes will be made to the database.
    """

    return StreamingResponse(
        radio_service.generate_podcast_sse(listener_program_id, user_id, dry_run=dry_run),
        media_type="text/event-stream",
    )
