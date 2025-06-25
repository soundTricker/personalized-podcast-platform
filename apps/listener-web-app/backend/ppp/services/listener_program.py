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

from datetime import datetime, timezone
from typing import List, Optional

from fastapi import HTTPException

from ppp.models.listener_program import BroadcastSchedule, ListenerProgram, ProgramStatus, PublishSetting
from ppp.services.base import BaseService
from ppp.utils.random_string import generate_random_string


class ListenerProgramService(BaseService[ListenerProgram]):
    """
    Service for ListenerProgram CRUD operations.
    """

    def __init__(self):
        """
        Initialize the service with the ListenerProgram model.
        """
        super().__init__(ListenerProgram)

    async def create_listener_program(
        self,
        title: str,
        description: str,
        listener_id: str,
        program_minutes: int = 30,
        insert_music: bool = True,
        base_radio_cast_ids: List[str] = [],
        broadcast_schedule: BroadcastSchedule = BroadcastSchedule.DAILY,
        broadcast_dayofweek: List[str] = [],
        status: ProgramStatus = ProgramStatus.DRAFT,
        publish_setting: PublishSetting = PublishSetting.PRIVATE,
        private_key: Optional[str] = None,
        cover_art_uri: Optional[str] = None,
    ) -> ListenerProgram:
        """
        Create a new listener program.

        Args:
            title: The title of the program.
            description: The description of the program.
            listener_id: The ID of the listener who created the program.
            program_minutes: The duration of the program in minutes.
            insert_music: Whether to insert music into the program.
            base_radio_cast_ids: The IDs of the radio casts that the program will listen.
            broadcast_schedule: The broadcast schedule of the program (daily or weekly).
            broadcast_dayofweek: The days of week for weekly broadcast.
            status: The status of the program.
            publish_setting: The publish setting of the program.
            private_key: The private key for limited access. If None and publish_setting is LIMITED, a random key will be generated.
            cover_art_uri: The URI for podcast cover art (gs:// format).

        Returns:
            The created listener program.
        """
        if base_radio_cast_ids is None:
            base_radio_cast_ids = []

        if broadcast_dayofweek is None:
            broadcast_dayofweek = []

        # Generate random private key if publish_setting is LIMITED and private_key is not provided
        if publish_setting == PublishSetting.LIMITED and private_key is None:
            private_key = generate_random_string()

        return await self.create(
            title=title,
            description=description,
            listener_id=listener_id,
            program_minutes=program_minutes,
            insert_music=insert_music,
            base_radio_cast_ids=base_radio_cast_ids,
            broadcast_schedule=broadcast_schedule,
            broadcast_dayofweek=broadcast_dayofweek,
            status=status,
            publish_setting=publish_setting,
            private_key=private_key,
            cover_art_uri=cover_art_uri,
        )

    async def update_listener_program(
        self,
        id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        program_minutes: Optional[int] = None,
        insert_music: Optional[bool] = None,
        base_radio_cast_ids: Optional[List[str]] = None,
        broadcast_schedule: Optional[BroadcastSchedule] = None,
        broadcast_dayofweek: Optional[List[str]] = None,
        status: Optional[ProgramStatus] = None,
        publish_setting: Optional[PublishSetting] = None,
        private_key: Optional[str] = None,
        published_at: Optional[datetime] = None,
        cover_art_uri: Optional[str] = None,
    ) -> Optional[ListenerProgram]:
        """
        Update a listener program.

        Args:
            id: The ID of the program to update.
            title: The new title of the program.
            description: The new description of the program.
            program_minutes: The new duration of the program in minutes.
            insert_music: Whether to insert music into the program.
            base_radio_cast_ids: The IDs of the radio casts that the program will listen.
            broadcast_schedule: The broadcast schedule of the program (daily or weekly).
            broadcast_dayofweek: The days of week for weekly broadcast.
            status: The new status of the program.
            publish_setting: The new publish setting of the program.
            private_key: The private key for limited access.
            published_at: The date and time when the program was published.
            cover_art_uri: The URI for podcast cover art (gs:// format).

        Returns:
            The updated listener program if found, None otherwise.
        """
        update_data = {}
        if title is not None:
            update_data["title"] = title
        if description is not None:
            update_data["description"] = description
        if program_minutes is not None:
            update_data["program_minutes"] = program_minutes
        if insert_music is not None:
            update_data["insert_music"] = insert_music
        if base_radio_cast_ids is not None:
            update_data["base_radio_cast_ids"] = base_radio_cast_ids
        if broadcast_schedule is not None:
            update_data["broadcast_schedule"] = broadcast_schedule
        if broadcast_dayofweek is not None:
            update_data["broadcast_dayofweek"] = broadcast_dayofweek
        if status is not None:
            update_data["status"] = status
        if publish_setting is not None:
            update_data["publish_setting"] = publish_setting
        if private_key is not None:
            update_data["private_key"] = private_key
        if cover_art_uri is not None:
            update_data["cover_art_uri"] = cover_art_uri

        update_data["updated_at"] = datetime.now(tz=timezone.utc)

        if update_data["status"] == ProgramStatus.ACTIVE:
            program = await self.get_by_id(id)
            program_list = await self.get_listener_programs_by_listener_id(program.listener_id)
            active_programs = [p for p in program_list if p.status == ProgramStatus.ACTIVE and p.id != id]
            if len(active_programs) > 0:
                raise HTTPException(status_code=400, detail="active program can be once")

        return await self.update(id, **update_data)

    async def get_listener_programs_by_listener_id(self, listener_id: str) -> List[ListenerProgram]:
        """
        Get all listener programs for a specific listener.

        Args:
            listener_id: The ID of the listener.

        Returns:
            A list of listener programs.
        """
        return await self.model.find({"listenerId": listener_id})

    async def verify_program_ownership(self, program_id: str, user_id: str) -> Optional[ListenerProgram]:
        """
        Verify that a program belongs to a specific user.

        Args:
            program_id: The ID of the program to verify.
            user_id: The ID of the user to check ownership against.

        Returns:
            The program if it belongs to the user, None otherwise.
        """
        program = await self.get_by_id(program_id)
        if program is None or program.listener_id != user_id:
            return None
        return program


def get_listener_program_service() -> ListenerProgramService:
    """
    Dependency to get the ListenerProgramService.
    """
    return ListenerProgramService()
