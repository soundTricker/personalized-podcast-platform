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

from ppp.models.radio_cast import RadioCast, RadioCastRole
from ppp.services.base import BaseService


class RadioCastService(BaseService[RadioCast]):
    """
    Service for RadioCast CRUD operations.
    """

    def __init__(self):
        """
        Initialize the service with the RadioCast model.
        """
        super().__init__(RadioCast)

    async def create_radio_cast(
        self,
        name: str,
        listener_id: str,
        role: RadioCastRole = RadioCastRole.RadioPersonality,
        voice_name: Optional[str] = None,
        personality: Optional[str] = None,
    ) -> RadioCast:
        """
        Create a new radio cast.

        Args:
            name: The name of the radio cast.
            description: The description of the radio cast.
            listener_id: The ID of the listener who created the radio cast.
            role: The role of the radio cast.
            voice_name: The name of the voice to use for the radio cast.
            personality: The personality description of the radio cast.

        Returns:
            The created radio cast.
        """
        return await self.create(
            name=name,
            listener_id=listener_id,
            role=role,
            voice_name=voice_name,
            personality=personality,
        )

    async def update_radio_cast(
        self,
        id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        role: Optional[RadioCastRole] = None,
        voice_name: Optional[str] = None,
        personality: Optional[str] = None,
    ) -> Optional[RadioCast]:
        """
        Update a radio cast.

        Args:
            id: The ID of the radio cast to update.
            name: The new name of the radio cast.
            description: The new description of the radio cast.
            role: The new role of the radio cast.
            voice_name: The new voice name for the radio cast.
            personality: The new personality description of the radio cast.

        Returns:
            The updated radio cast if found, None otherwise.
        """
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if description is not None:
            update_data["description"] = description
        if role is not None:
            update_data["role"] = role
        if voice_name is not None:
            update_data["voice_name"] = voice_name
        if personality is not None:
            update_data["personality"] = personality

        return await self.update(id, **update_data)

    async def get_predefined_radio_casts(self) -> list[RadioCast]:
        return await self.model.find_predefined_radio_casts()

    async def get_radio_casts_by_listener_id(self, listener_id: str) -> List[RadioCast]:
        """
        Get all radio casts for a specific listener.

        Args:
            listener_id: The ID of the listener.

        Returns:
            A list of radio casts.
        """
        return await self.model.find({"listenerId": listener_id})

    async def verify_radio_cast_ownership(self, radio_cast_id: str, user_id: str) -> Optional[RadioCast]:
        """
        Verify that a radio cast belongs to a specific user.

        Args:
            radio_cast_id: The ID of the radio cast to verify.
            user_id: The ID of the user to check ownership against.

        Returns:
            The radio cast if it belongs to the user, None otherwise.
        """
        radio_cast = await self.get_by_id(radio_cast_id)
        if radio_cast is None or radio_cast.listener_id != user_id:
            return None
        return radio_cast

    async def get_radio_casts_by_ids(self, radio_cast_ids: List[str]) -> List[RadioCast]:
        """
        Get radio casts by their IDs.

        Args:
            radio_cast_ids: List of radio cast IDs to retrieve.

        Returns:
            A list of radio casts matching the provided IDs.
        """
        result = []
        for radio_cast_id in radio_cast_ids:
            radio_cast = await self.get_by_id(radio_cast_id)
            if radio_cast is not None:
                result.append(radio_cast)
        return result


def get_radio_cast_service() -> RadioCastService:
    return RadioCastService()
