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

from fastapi import APIRouter, Depends, status

from ppp.models.listener_program import ListenerProgram
from ppp.schemas.listener_program import ListenerProgramMCPCreateSchema, ListenerProgramSchema
from ppp.services.listener_program import ListenerProgramService, get_listener_program_service

router = APIRouter()


@router.post("/", response_model=ListenerProgramSchema, status_code=status.HTTP_201_CREATED, operation_id="create_listener_program")
async def create_listener_program(
    listener_id: str,
    listener_program: ListenerProgramMCPCreateSchema,
    service: ListenerProgramService = Depends(get_listener_program_service),
) -> ListenerProgram:
    """
    Create a new listener program for MCP.

    Args:
        listener_id: The ID of the listener to create the program for
        listener_program: The listener program data
        service: The listener program service

    Returns:
        The created listener program
    """
    return await service.create_listener_program(
        title=listener_program.title,
        description=listener_program.description,
        listener_id=listener_id,
        program_minutes=listener_program.program_minutes,
        insert_music=listener_program.insert_music,
        base_radio_cast_ids=listener_program.base_radio_cast_ids,
        status=listener_program.status,
        publish_setting=listener_program.publish_setting,
        private_key=listener_program.private_key or None,
        cover_art_uri=listener_program.cover_art_uri,
    )
