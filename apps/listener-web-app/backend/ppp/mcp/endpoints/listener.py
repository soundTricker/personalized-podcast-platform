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

from fastapi import APIRouter, Depends, status, HTTPException

from ppp.models.listener import Listener
from ppp.schemas.listener import ListenerSchema
from ppp.services.listener import ListenerService, get_listener_service

router = APIRouter()

@router.get("/{listener_id}", response_model=ListenerSchema, status_code=status.HTTP_200_OK, operation_id="get_listener")
async def get_listener(listener_id: str, service: ListenerService = Depends(get_listener_service)) -> Listener:
    listener = await service.get_listener_by_id(listener_id)
    if not listener:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Listener not found")
    return listener
