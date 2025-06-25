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

"""
Google OAuth2 endpoints for authentication and authorization.

This module provides endpoints for initiating the Google OAuth2 flow and handling the callback.
"""

from typing import List

from fastapi import APIRouter, Depends, Query

from ppp.settings import Settings, get_settings
from ppp.utils.google_oauth2 import generate_auth_url

router = APIRouter()


@router.get("/google-oauth2", operation_id="get_google_oauth2_url")
async def google_oauth2(
    listener_id: str = Query(..., description="The listener ID"),
    scopes: List[str] = Query(..., description="The list of scopes to request"),
    settings: Settings = Depends(get_settings),
) -> str:
    """
    Initiate the Google OAuth2 flow.

    Args:
        listener_id: The ID of the current user.
        scopes: The list of scopes to request.
    Returns:
        A redirect to the Google authorization URL.
    """
    return generate_auth_url(settings, listener_id, scopes)
