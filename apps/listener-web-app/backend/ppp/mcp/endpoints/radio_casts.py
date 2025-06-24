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

from fastapi import APIRouter, Depends

from ppp.models.radio_cast import RadioCast
from ppp.schemas.radio_cast import RadioCastSchema
from ppp.services.radio_cast import RadioCastService, get_radio_cast_service

router = APIRouter()


@router.get("/", response_model=List[RadioCastSchema], operation_id="get_radio_casts")
async def get_radio_casts(
    listener_id: str,
    service: RadioCastService = Depends(get_radio_cast_service),
) -> List[RadioCast]:
    """
    Get radio casts for MCP.

    Returns both predefined radio casts and radio casts owned by the specified listener.

    Args:
        listener_id: The ID of the listener to get radio casts for
        service: The radio cast service

    Returns:
        A list of available radio casts
    """
    predefined_radio_casts = await service.get_predefined_radio_casts()
    listener_radio_casts = await service.get_radio_casts_by_listener_id(listener_id)

    # Combine predefined and listener-specific radio casts
    all_available_casts = predefined_radio_casts + listener_radio_casts

    return all_available_casts