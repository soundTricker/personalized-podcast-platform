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

from ppp.models.listener import Listener
from ppp.schemas.listener import ListenerCreateSchema, ListenerSchema
from ppp.services.listener import ListenerService
from ppp.utils.auth import get_current_user

router = APIRouter()


def get_listener_service() -> ListenerService:
    """
    Dependency to get the ListenerService.
    """
    return ListenerService()


@router.post("/signup", response_model=ListenerSchema, status_code=status.HTTP_201_CREATED)
async def signup(
    _: ListenerCreateSchema | None = None,  # Not used, but kept for API consistency
    service: ListenerService = Depends(get_listener_service),
    user: dict = Depends(get_current_user),
) -> Listener:
    """
    Create a new listener (signup).

    This endpoint uses the Firebase ID token to get the user's email and ID,
    and creates a new listener in the database.

    If a listener with the given ID already exists, a 409 Conflict error is returned.
    """
    # Get user information from Firebase Auth
    firebase_id = user["uid"]
    email = user["email"]

    # Get display name if available
    display_name = user.get("name")

    # Create the listener
    return await service.create_listener(
        id=firebase_id,
        email=email,
        display_name=display_name,
    )


@router.get("/me", response_model=ListenerSchema)
async def get_current_listener(
    service: ListenerService = Depends(get_listener_service),
    user: dict = Depends(get_current_user),
) -> Listener:
    """
    Get the current listener.

    This endpoint uses the Firebase ID token to get the user's ID,
    and returns the corresponding listener from the database.

    If the listener does not exist, a 404 Not Found error is returned.
    """
    # Get user ID from Firebase Auth
    firebase_id = user["uid"]

    # Get the listener
    listener = await service.get_listener_by_id(firebase_id)

    # If the listener does not exist, return 404
    if listener is None:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener with ID {firebase_id} not found",
        )

    return listener
