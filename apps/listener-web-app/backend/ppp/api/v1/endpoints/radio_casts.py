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

from fastapi import APIRouter, Depends, HTTPException, Query, status

from ppp.models.radio_cast import RadioCast
from ppp.schemas.radio_cast import (
    RadioCastCreateSchema,
    RadioCastSchema,
    RadioCastUpdateSchema,
)
from ppp.services.radio_cast import RadioCastService
from ppp.utils.auth import get_current_user_id

router = APIRouter()


def get_radio_cast_service() -> RadioCastService:
    """
    Dependency to get the RadioCastService.
    """
    return RadioCastService()


@router.post("/", response_model=RadioCastSchema, status_code=status.HTTP_201_CREATED)
async def create_radio_cast(
    radio_cast: RadioCastCreateSchema,
    service: RadioCastService = Depends(get_radio_cast_service),
    user_id: str = Depends(get_current_user_id),
) -> RadioCast:
    """
    Create a new radio cast.
    """
    return await service.create_radio_cast(
        name=radio_cast.name,
        listener_id=user_id,  # Use user_id from get_current_user_id
        role=radio_cast.role,
        voice_name=radio_cast.voice_name,
        personality=radio_cast.personality,
    )


@router.get("/{radio_cast_id}", response_model=RadioCastSchema)
async def get_radio_cast(
    radio_cast_id: str,
    service: RadioCastService = Depends(get_radio_cast_service),
    user_id: str = Depends(get_current_user_id),
) -> RadioCast:
    """
    Get a radio cast by ID.

    Only the owner of the radio cast can retrieve it.
    """
    # Verify that the radio cast belongs to the current user
    radio_cast = await service.verify_radio_cast_ownership(radio_cast_id, user_id)
    if radio_cast is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Radio cast with ID {radio_cast_id} not found or you don't have permission to access it",
        )
    return radio_cast


@router.get("/", response_model=list[RadioCastSchema])
async def list_radio_casts(
    radio_cast_ids: Optional[List[str]] = Query(title="Radio Cast IDs", default=None),
    service: RadioCastService = Depends(get_radio_cast_service),
    user_id: str = Depends(get_current_user_id),
) -> list[RadioCast]:
    """
    List radio casts for the current user.

    If radio_cast_ids is provided, only returns radio casts with matching IDs.
    Only predefined radio casts or radio casts owned by the current user will be returned.
    """
    predefined_radio_casts = await service.get_predefined_radio_casts()
    listener_radio_casts = await service.get_radio_casts_by_listener_id(user_id)

    all_available_casts = predefined_radio_casts + listener_radio_casts

    # If radio_cast_ids is provided, filter the results
    if radio_cast_ids:
        # Filter to only include casts that match the provided IDs
        # and are either predefined or owned by the current user
        filtered_casts = [cast for cast in all_available_casts if cast.id in radio_cast_ids]
        return filtered_casts

    # If no radio_cast_ids provided, return all available casts
    return all_available_casts


@router.put("/{radio_cast_id}", response_model=RadioCastSchema)
async def update_radio_cast(
    radio_cast_id: str,
    radio_cast: RadioCastUpdateSchema,
    service: RadioCastService = Depends(get_radio_cast_service),
    user_id: str = Depends(get_current_user_id),
) -> RadioCast:
    """
    Update a radio cast.

    Only the owner of the radio cast can update it.
    """
    # Verify that the radio cast belongs to the current user
    cast = await service.verify_radio_cast_ownership(radio_cast_id, user_id)
    if cast is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Radio cast with ID {radio_cast_id} not found or you don't have permission to update it",
        )

    updated_cast = await service.update_radio_cast(
        id=radio_cast_id,
        name=radio_cast.name,
        role=radio_cast.role,
        voice_name=radio_cast.voice_name,
        personality=radio_cast.personality,
    )

    return updated_cast


@router.delete("/{radio_cast_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_radio_cast(
    radio_cast_id: str,
    service: RadioCastService = Depends(get_radio_cast_service),
    user_id: str = Depends(get_current_user_id),
) -> None:
    """
    Delete a radio cast.

    Only the owner of the radio cast can delete it.
    """
    # Verify that the radio cast belongs to the current user
    cast = await service.verify_radio_cast_ownership(radio_cast_id, user_id)
    if cast is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Radio cast with ID {radio_cast_id} not found or you don't have permission to delete it",
        )

    await service.delete(radio_cast_id)
