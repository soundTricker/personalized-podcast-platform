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
from fastapi.responses import Response, StreamingResponse

from ppp.models.program_broadcast_history import ProgramBroadcastHistory, ProgramBroadcastHistoryStatus
from ppp.schemas.program_broadcast_history import (
    ProgramBroadcastHistoryCreate,
    ProgramBroadcastHistorySchema,
    ProgramBroadcastHistoryUpdate,
)
from ppp.services.chat import ChatAPI, get_chat_api
from ppp.services.listener_program import ListenerProgramService, get_listener_program_service
from ppp.services.program_broadcast_history import ProgramBroadcastHistoryService, get_program_broadcast_history_service
from ppp.services.radio import RadioService, get_radio_service
from ppp.utils.auth import get_current_user_id

router = APIRouter()


@router.get("/{program_id}/broadcast_history", response_model=List[ProgramBroadcastHistorySchema])
async def list_program_broadcast_histories(
    program_id: str,
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    user_id: str = Depends(get_current_user_id),
) -> List[ProgramBroadcastHistory]:
    """
    List all broadcast histories for a listener program.

    Only the owner of the program can retrieve its broadcast histories.
    """
    # Verify that the program belongs to the current user
    program = await program_service.verify_program_ownership(program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found or you don't have permission to access it",
        )

    # Get all broadcast histories for the program
    return await broadcast_history_service.get_broadcast_histories_by_program_id(program_id)


@router.get("/{program_id}/broadcast_history/{broadcast_history_id}", response_model=ProgramBroadcastHistorySchema)
async def get_program_broadcast_history(
    program_id: str,
    broadcast_history_id: str,
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    user_id: str = Depends(get_current_user_id),
) -> ProgramBroadcastHistory:
    """
    Get a specific broadcast history for a listener program.

    Only the owner of the program can retrieve its broadcast histories.
    """
    # Verify that the program belongs to the current user
    program = await program_service.verify_program_ownership(program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found or you don't have permission to access it",
        )

    # Get the broadcast history
    broadcast_history = await broadcast_history_service.get_broadcast_history_by_id(program_id, broadcast_history_id)
    if broadcast_history is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Broadcast history with ID {broadcast_history_id} not found",
        )

    return broadcast_history


@router.post("/{program_id}/broadcast_history/{broadcast_history_id}/generate-podcast", response_model=ProgramBroadcastHistorySchema)
async def generate_podcast(
    program_id: str,
    broadcast_history_id: str,
    dry_run: bool = False,
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    radio_service: RadioService = Depends(get_radio_service),
    user_id: str = Depends(get_current_user_id),
) -> StreamingResponse:
    """
    Get a specific broadcast history for a listener program.

    Only the owner of the program can retrieve its broadcast histories.
    """
    # Verify that the program belongs to the current user
    program = await program_service.verify_program_ownership(program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found or you don't have permission to access it",
        )

    # Get the broadcast history
    broadcast_history = await broadcast_history_service.get_broadcast_history_by_id(program_id, broadcast_history_id)
    if broadcast_history is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Broadcast history with ID {broadcast_history_id} not found",
        )

    if (broadcast_history.dry_run and broadcast_history.status == ProgramBroadcastHistoryStatus.GENERATING) or (
        not broadcast_history.dry_run and broadcast_history.status != ProgramBroadcastHistoryStatus.FAILURE
    ):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="This Broadcast history was not failed.")

    return StreamingResponse(
        radio_service.generate_podcast_sse(program.id, user_id, history_id=broadcast_history.id, dry_run=dry_run),
        media_type="text/event-stream",
    )


@router.get("/{program_id}/broadcast_history/{broadcast_history_id}/audio", responses={200: {"content": {"audio/mp3": {}}}})
async def get_program_broadcast_history_audio(
    program_id: str,
    broadcast_history_id: str,
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    chat_api: ChatAPI = Depends(get_chat_api),
    user_id: str = Depends(get_current_user_id),
) -> Response:
    """
    Get a specific broadcast history for a listener program.

    Only the owner of the program can retrieve its broadcast histories.
    """
    # Verify that the program belongs to the current user
    program = await program_service.verify_program_ownership(program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found or you don't have permission to access it",
        )

    # Get the broadcast history
    broadcast_history = await broadcast_history_service.get_broadcast_history_by_id(program_id, broadcast_history_id)
    if broadcast_history is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Broadcast history with ID {broadcast_history_id} not found",
        )

    artifact = await chat_api.load_artifact(user_id, broadcast_history.session_id, broadcast_history.artifact_id)

    if artifact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Artifact not found",
        )

    return Response(status_code=status.HTTP_200_OK, content=artifact.inline_data.data, media_type=artifact.inline_data.mime_type)


@router.post("/{program_id}/broadcast_history", response_model=ProgramBroadcastHistorySchema, status_code=status.HTTP_201_CREATED)
async def create_program_broadcast_history(
    program_id: str,
    broadcast_history: ProgramBroadcastHistoryCreate,
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    user_id: str = Depends(get_current_user_id),
) -> ProgramBroadcastHistory:
    """
    Create a new broadcast history for a listener program.

    Only the owner of the program can create broadcast histories.
    """
    # Verify that the program belongs to the current user
    program = await program_service.verify_program_ownership(program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found or you don't have permission to access it",
        )

    # Create the broadcast history
    created_history = await broadcast_history_service.create_broadcast_history(
        program_id=program_id,
        no=broadcast_history.no,
        app_name=broadcast_history.app_name,
        listener_id=broadcast_history.listener_id,
        session_id=broadcast_history.session_id,
        artifact_id=broadcast_history.artifact_id,
        status=broadcast_history.status,
    )

    if created_history is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create broadcast history",
        )

    return created_history


@router.put("/{program_id}/broadcast_history/{broadcast_history_id}", response_model=ProgramBroadcastHistorySchema)
async def update_program_broadcast_history(
    program_id: str,
    broadcast_history_id: str,
    broadcast_history_update: ProgramBroadcastHistoryUpdate,
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    user_id: str = Depends(get_current_user_id),
) -> ProgramBroadcastHistory:
    """
    Update a broadcast history for a listener program.

    Only the owner of the program can update broadcast histories.
    Currently, only the status can be updated.
    """
    # Verify that the program belongs to the current user
    program = await program_service.verify_program_ownership(program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found or you don't have permission to access it",
        )

    # Check if the broadcast history exists
    broadcast_history = await broadcast_history_service.get_broadcast_history_by_id(program_id, broadcast_history_id)
    if broadcast_history is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Broadcast history with ID {broadcast_history_id} not found",
        )

    # Update the broadcast history status
    if broadcast_history_update.status is not None:
        updated_history = await broadcast_history_service.update_broadcast_history_status(program_id, broadcast_history_id, broadcast_history_update.status)
        if updated_history is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update broadcast history",
            )
        return updated_history

    # If no fields to update, return the existing broadcast history
    return broadcast_history


@router.delete("/{program_id}/broadcast_history/{broadcast_history_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_program_broadcast_history(
    program_id: str,
    broadcast_history_id: str,
    program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    user_id: str = Depends(get_current_user_id),
) -> None:
    """
    Delete a broadcast history for a listener program.

    Only the owner of the program can delete broadcast histories.
    """
    # Verify that the program belongs to the current user
    program = await program_service.verify_program_ownership(program_id, user_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found or you don't have permission to access it",
        )

    # Delete the broadcast history
    deleted = await broadcast_history_service.delete_broadcast_history(program_id, broadcast_history_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Broadcast history with ID {broadcast_history_id} not found",
        )
