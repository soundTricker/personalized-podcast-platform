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

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response

from ppp.models.program_broadcast_history import ProgramBroadcastHistoryStatus
from ppp.services.listener import ListenerService, get_listener_service
from ppp.services.listener_program import ListenerProgramService, get_listener_program_service
from ppp.services.program_broadcast_history import ProgramBroadcastHistoryService, get_program_broadcast_history_service
from ppp.services.radio import RadioService, get_radio_service

# Create tasks router
tasks_router = APIRouter()

logger = logging.getLogger(__name__)


@tasks_router.post(
    "/generate-podcast",
    responses={204: {"model": None}},
)
async def generate_podcast(
    listener_program_id: str,
    broadcast_history_id: str,
    listener_program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    listener_service: ListenerService = Depends(get_listener_service),
    radio_service: RadioService = Depends(get_radio_service),
) -> Response:
    """
    Generate a podcast for a listener program using the specified broadcast history.

    Args:
        listener_program_id: The ID of the listener program
        broadcast_history_id: The ID of the broadcast history

    Returns:
        A streaming response with the generated podcast
    """
    # Get the listener program
    program = await listener_program_service.get_by_id(listener_program_id)
    if program is None:
        logger.error(f"Listener program not found listener_program_id: f{listener_program_id}")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    # Get the listener
    listener = await listener_service.get_listener_by_id(program.listener_id)
    if listener is None:
        logger.error(f"Listener not found listener_id: f{program.listener_id}")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    # Get the broadcast history
    broadcast_history = await broadcast_history_service.get_broadcast_history_by_id(listener_program_id, broadcast_history_id)
    if broadcast_history is None:
        logger.error(f"BroadCastHistory not found listener_program_id: f{listener_program_id} broadcast_history_id: f{broadcast_history_id}")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    # Check if the broadcast history is in a failed state
    if broadcast_history.status == ProgramBroadcastHistoryStatus.GENERATING:
        logger.error(f"BroadCastHistory is running : f{listener_program_id} broadcast_history_id: f{broadcast_history_id}")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    async for event in await radio_service.generate_podcast(program.id, listener.id, history_id=broadcast_history.id):
        if event.error_message or event.error_code:
            logger.error(f"failed to generate podcast error: {event.error_message} {event.error_code}")
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"failed to generate podcast error: {event.error_message} {event.error_code}")

    logger.info(f"finished to generate podcast listener_program_id: f{listener_program_id} broadcast_history_id: f{broadcast_history_id}")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@tasks_router.post(
    "/send-mail",
    responses={204: {"model": None}},
)
async def send_mail(
    mail_id: str,
) -> Response:
    """
    Send an email using the specified mail document.

    This is an asynchronous task endpoint that processes email sending.
    Currently, this is a placeholder implementation that does nothing.

    Args:
        mail_id: The ID of the mail document to process

    Returns:
        A 204 No Content response
    """
    logger.info(f"Processing mail sending task for mail_id: {mail_id}")

    # TODO: Implement actual email sending logic
    # For now, this task does nothing as specified in the requirements

    logger.info(f"Mail sending task completed for mail_id: {mail_id}")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
