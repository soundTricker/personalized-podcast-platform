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

from typing import List, Optional

from fastapi import Depends

from ppp.models.program_broadcast_history import ProgramBroadcastHistory, ProgramBroadcastHistoryStatus
from ppp.services.listener_program import ListenerProgramService, get_listener_program_service


class ProgramBroadcastHistoryService:
    """
    Service for ProgramBroadcastHistory CRUD operations.
    """

    def __init__(self, listener_program_service: ListenerProgramService):
        """
        Initialize the service.
        """
        self.listener_program_service = listener_program_service

    async def get_broadcast_history_by_session_id(self, program_id: str, app_name: str, listener_id: str, session_id: str) -> Optional[ProgramBroadcastHistory]:
        """
        Get a specific broadcast history by ID.

        Args:
            program_id: The ID of the program.
            broadcast_history_id: The ID of the broadcast history.

        Returns:
            The broadcast history if found, None otherwise.
        """
        program = await self.listener_program_service.get_by_id(program_id)

        if not program:
            return None

        # Create a model for the specific program
        model_for_program = ProgramBroadcastHistory.model_for(program)
        try:
            return await model_for_program.find_one({"appName": app_name, "listenerId": listener_id, "sessionId": session_id})
        except Exception:
            return None

    async def get_broadcast_histories_by_program_id(self, program_id: str) -> List[ProgramBroadcastHistory]:
        """
        Get all broadcast histories for a specific program.

        Args:
            program_id: The ID of the program.

        Returns:
            A list of broadcast histories.
        """
        program = await self.listener_program_service.get_by_id(program_id)

        if not program:
            return []

        # Create a model for the specific program
        model_for_program = ProgramBroadcastHistory.model_for(program)

        # Find all broadcast histories for the program
        broadcast_histories = await model_for_program.find({})

        # Sort broadcast histories by number (descending)
        broadcast_histories.sort(key=lambda x: x.no, reverse=True)

        return broadcast_histories

    async def get_broadcast_history_by_id(self, program_id: str, broadcast_history_id: str) -> Optional[ProgramBroadcastHistory]:
        """
        Get a specific broadcast history by ID.

        Args:
            program_id: The ID of the program.
            broadcast_history_id: The ID of the broadcast history.

        Returns:
            The broadcast history if found, None otherwise.
        """
        program = await self.listener_program_service.get_by_id(program_id)

        if not program:
            return None

        # Create a model for the specific program
        model_for_program = ProgramBroadcastHistory.model_for(program)

        try:
            return await model_for_program.get_by_id(broadcast_history_id)
        except Exception:
            return None

    async def create_broadcast_history(
        self,
        program_id: str,
        no: int,
        app_name: str,
        listener_id: str,
        session_id: str,
        status: ProgramBroadcastHistoryStatus = ProgramBroadcastHistoryStatus.PREPARE,
        dry_run: bool = False,
    ) -> Optional[ProgramBroadcastHistory]:
        """
        Create a new broadcast history.

        Args:
            program_id: The ID of the program.
            no: The number of the broadcast.
            app_name: The name of the app.
            listener_id: The ID of the listener.
            session_id: The ID of the session.
            artifact_id: The ID of the artifact.
            status: The status of the broadcast.
            dry_run: This broadcast is dry run

        Returns:
            The created broadcast history if successful, None otherwise.
        """
        program = await self.listener_program_service.get_by_id(program_id)

        if not program:
            return None

        # Create a model for the specific program
        model_for_program = ProgramBroadcastHistory.model_for(program)

        # Create a new broadcast history
        broadcast_history = model_for_program(
            no=no,
            app_name=app_name,
            listener_id=listener_id,
            session_id=session_id,
            status=status,
            dry_run=dry_run,
        )

        await broadcast_history.save()
        return broadcast_history

    async def update_broadcast_history_status(
        self,
        program_id: str,
        broadcast_history_id: str,
        status: ProgramBroadcastHistoryStatus,
    ) -> Optional[ProgramBroadcastHistory]:
        """
        Update the status of a broadcast history.

        Args:
            program_id: The ID of the program.
            broadcast_history_id: The ID of the broadcast history.
            status: The new status of the broadcast.

        Returns:
            The updated broadcast history if found, None otherwise.
        """
        broadcast_history = await self.get_broadcast_history_by_id(program_id, broadcast_history_id)

        if not broadcast_history:
            return None

        broadcast_history.status = status
        await broadcast_history.save()
        return broadcast_history

    async def delete_broadcast_history(self, program_id: str, broadcast_history_id: str) -> bool:
        """
        Delete a broadcast history.

        Args:
            program_id: The ID of the program.
            broadcast_history_id: The ID of the broadcast history.

        Returns:
            True if the broadcast history was deleted, False otherwise.
        """
        broadcast_history = await self.get_broadcast_history_by_id(program_id, broadcast_history_id)

        if not broadcast_history:
            return False

        await broadcast_history.delete()
        return True


def get_program_broadcast_history_service(listener_program_service=Depends(get_listener_program_service)) -> ProgramBroadcastHistoryService:
    return ProgramBroadcastHistoryService(listener_program_service=listener_program_service)
