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

from fastapi import HTTPException, status

from ppp.models.listener import Listener
from ppp.services.base import BaseService
from ppp.utils.crypto import decrypt, encrypt


class ListenerService(BaseService[Listener]):
    """
    Service for Listener CRUD operations.
    """

    def __init__(self):
        """
        Initialize the service with the Listener model.
        """
        super().__init__(Listener)

    async def create_listener(self, id: str, email: str, display_name: Optional[str] = None) -> Listener:
        """
        Create a new listener.

        Args:
            id: The ID of the listener (Firebase Auth UID).
            email: The email of the listener.
            display_name: The display name of the listener.

        Returns:
            The created listener.

        Raises:
            HTTPException: If a listener with the given ID already exists.
        """
        # Check if a listener with the given ID already exists
        existing_listener = await self.get_by_id(id)
        if existing_listener is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Listener with ID {id} already exists",
            )

        # Create the listener
        return await self.create(
            id=id,
            email=email,
            display_name=display_name,
        )

    async def get_listener_by_id(self, id: str) -> Optional[Listener]:
        """
        Get a listener by ID.

        Args:
            id: The ID of the listener.

        Returns:
            The listener if found, None otherwise.
        """
        return await self.get_by_id(id)

    async def update_listener(self, id: str, email: Optional[str] = None, display_name: Optional[str] = None) -> Optional[Listener]:
        """
        Update a listener.

        Args:
            id: The ID of the listener to update.
            email: The new email of the listener.
            display_name: The new display name of the listener.

        Returns:
            The updated listener if found, None otherwise.
        """
        update_data = {}
        if email is not None:
            update_data["email"] = email
        if display_name is not None:
            update_data["display_name"] = display_name

        return await self.update(id, **update_data)

    async def update_google_oauth_tokens(self, id: str, access_token: str, refresh_token: str, scopes: List[str]) -> Optional[Listener]:
        """
        Update a listener's Google OAuth tokens and scopes.

        Args:
            id: The ID of the listener to update.
            access_token: The Google access token.
            refresh_token: The Google refresh token.
            scopes: The list of scopes the listener has granted access to.

        Returns:
            The updated listener if found, None otherwise.
        """
        # Encrypt the tokens before storing them
        encrypted_access_token = encrypt(access_token)
        encrypted_refresh_token = encrypt(refresh_token)

        update_data = {
            "encrypted_google_access_token": encrypted_access_token,
            "encrypted_google_refresh_token": encrypted_refresh_token,
            "scopes": scopes,
        }

        return await self.update(id, **update_data)

    async def get_google_oauth_tokens(self, id: str) -> tuple[Optional[str], Optional[str], List[str]]:
        """
        Get a listener's Google OAuth tokens and scopes.

        Args:
            id: The ID of the listener.

        Returns:
            A tuple containing the decrypted access token, refresh token, and scopes.
            If the listener is not found or tokens are not set, returns (None, None, []).
        """
        listener = await self.get_by_id(id)
        if listener is None:
            return None, None, []

        access_token = None
        if listener.encrypted_google_access_token:
            access_token = decrypt(listener.encrypted_google_access_token)

        refresh_token = None
        if listener.encrypted_google_refresh_token:
            refresh_token = decrypt(listener.encrypted_google_refresh_token)

        return access_token, refresh_token, listener.scopes


def get_listener_service() -> ListenerService:
    """
    Dependency to get the ListenerService.
    """
    return ListenerService()
