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

import logging

from fastapi import APIRouter, Depends, HTTPException, Response, status

from ppp.models.mail import Mail
from ppp.models.program_broadcast_history import ProgramBroadcastHistory, ProgramBroadcastHistoryStatus
from ppp.schemas.program_broadcast_history import ProgramBroadcastHistorySchema
from ppp.services.listener import ListenerService, get_listener_service
from ppp.services.listener_program import ListenerProgramService, get_listener_program_service
from ppp.services.listener_program_segment import ListenerProgramSegmentService, get_listener_program_segment_service
from ppp.services.program_broadcast_history import ProgramBroadcastHistoryService, get_program_broadcast_history_service
from ppp.services.radio import RadioService, get_radio_service
from ppp.services.radio_cast import RadioCastService, get_radio_cast_service

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/{program_id}/broadcast_history", response_model=ProgramBroadcastHistorySchema, status_code=status.HTTP_201_CREATED)
async def create_broadcast_history(
    program_id: str,
    listener_program_service: ListenerProgramService = Depends(get_listener_program_service),
    listener_service: ListenerService = Depends(get_listener_service),
    listener_program_segment_service: ListenerProgramSegmentService = Depends(get_listener_program_segment_service),
    radio_cast_service: RadioCastService = Depends(get_radio_cast_service),
    radio_service: RadioService = Depends(get_radio_service),
):
    """
    Create a new broadcast history for a listener program.

    Args:
        program_id: The ID of the listener program.

    Returns:
        The created broadcast history.

    Responses:
        204: No content if the listener program or listener does not exist.
        201: Created if the broadcast history was successfully created.
    """
    # Get the listener program
    program = await listener_program_service.get_by_id(program_id)
    if program is None:
        logging.error(f"Listener program not found listener_program_id: f{program_id}")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    # Get the listener
    listener = await listener_service.get_listener_by_id(program.listener_id)
    if listener is None:
        logger.error(f"Listener not found listener_id: f{program.listener_id}")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    # Get the segments
    segments = await listener_program_segment_service.get_segments_by_program_id(program.id)

    # Get the radio casts
    radio_cast_id_set = {radio_cast_id for radio_cast_id in program.base_radio_cast_ids}
    for seg in segments:
        radio_cast_id_set.update(seg.override_radio_casts)
    radio_casts = await radio_cast_service.get_radio_casts_by_ids(list(radio_cast_id_set))

    # Create the broadcast history
    history, _ = await radio_service.make_history(listener_id=listener.id, program=program, segments=segments, radio_casts=radio_casts, status=ProgramBroadcastHistoryStatus.PREPARE)

    # Return the created broadcast history
    return history


@router.get("/{program_id}/broadcast_history/{broadcast_history_id}", response_model=ProgramBroadcastHistorySchema)
async def get_broadcast_history(
    program_id: str,
    broadcast_history_id: str,
    listener_program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
) -> ProgramBroadcastHistory:
    """
    Get a specific broadcast history for a listener program.

    Args:
        program_id: The ID of the listener program.
        broadcast_history_id: The ID of the broadcast history.

    Returns:
        The broadcast history.

    Responses:
        404: Not found if the listener program or broadcast history does not exist.
        200: OK if the broadcast history was successfully retrieved.
    """
    # Get the listener program
    program = await listener_program_service.get_by_id(program_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found",
        )

    # Get the broadcast history
    broadcast_history = await broadcast_history_service.get_broadcast_history_by_id(program_id, broadcast_history_id)
    if broadcast_history is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Broadcast history with ID {broadcast_history_id} not found",
        )

    return broadcast_history


@router.post("/{program_id}/broadcast_history/{broadcast_history_id}/send-mail", status_code=status.HTTP_201_CREATED)
async def send_mail(
    program_id: str,
    broadcast_history_id: str,
    listener_program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    listener_service: ListenerService = Depends(get_listener_service),
) -> dict:
    """
    Send an email for a specific broadcast history.

    Args:
        program_id: The ID of the listener program.
        broadcast_history_id: The ID of the broadcast history.

    Returns:
        A success message with the mail ID.

    Responses:
        404: Not found if the listener program, broadcast history, or listener does not exist.
        400: Bad request if the broadcast history status is not success or news_letter_contents is missing.
        201: Created if the mail was successfully queued for sending.
    """
    # Get the listener program
    program = await listener_program_service.get_by_id(program_id)
    if program is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener program with ID {program_id} not found",
        )

    # Get the broadcast history
    broadcast_history = await broadcast_history_service.get_broadcast_history_by_id(program_id, broadcast_history_id)
    if broadcast_history is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Broadcast history with ID {broadcast_history_id} not found",
        )

    # Check if broadcast history status is success
    if broadcast_history.status != ProgramBroadcastHistoryStatus.SUCCESS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Broadcast history status must be 'success', current status: {broadcast_history.status}",
        )

    # Check if news_letter_contents exists
    if not broadcast_history.news_letter_contents:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Broadcast history must have news_letter_contents to send email",
        )

    # Get the listener
    listener = await listener_service.get_listener_by_id(program.listener_id)
    if listener is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener with ID {program.listener_id} not found",
        )

    # Create and send mail
    mail = await Mail.send(
        subject=f"Podcast Newsletter: {program.title}",
        body=broadcast_history.news_letter_contents,
        from_email="noreply@example.com",  # TODO: Configure proper sender email
        to=[listener.email],
        cc=[],
        attachments=[],
    )

    logger.info(f"Mail queued for sending: mail_id={mail.id}, listener_email={listener.email}")

    return {
        "message": "Mail successfully queued for sending",
        "mail_id": mail.id,
        "recipient": listener.email,
    }
