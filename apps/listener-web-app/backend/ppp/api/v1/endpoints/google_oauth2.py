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

import logging
import os
from typing import List

import requests
from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from fastapi.responses import RedirectResponse

from ppp.services.listener import ListenerService
from ppp.utils.auth import get_current_user_id

router = APIRouter()
listener_service = ListenerService()

# Google OAuth2 endpoints
GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"

# Get client ID and secret from environment variables
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")

if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
    raise ValueError("GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET must be set in environment variables")


@router.get("/google-oauth2")
async def google_oauth2(
    request: Request,
    scopes: List[str] = Query(..., description="The list of scopes to request"),
    user_id: str = Depends(get_current_user_id),
) -> str:
    """
    Initiate the Google OAuth2 flow.

    Args:
        request: The request object.
        scopes: The list of scopes to request.
        user_id: The ID of the current user.

    Returns:
        A redirect to the Google authorization URL.
    """
    # Construct the redirect URI
    redirect_uri = f"{os.environ.get('API_BASE_URL', 'http://localhost:3000')}/api/v1/google-oauth2/callback"

    # Construct the authorization URL
    auth_params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": " ".join(scopes),
        "access_type": "offline",  # Request a refresh token
        "prompt": "consent",  # Force the consent screen to appear
        "state": user_id,  # Pass the user ID as state to retrieve it in the callback
    }

    auth_url = f"{GOOGLE_AUTH_URL}?{'&'.join(f'{k}={v}' for k, v in auth_params.items())}"

    # Redirect to the authorization URL
    return auth_url


@router.get("/google-oauth2/callback")
async def google_oauth2_callback(
    code: str = Query(..., description="The authorization code"),
    state: str = Query(..., description="The state parameter containing the user ID"),
):
    """
    Handle the Google OAuth2 callback.

    Args:
        code: The authorization code.
        state: The state parameter containing the user ID.

    Returns:
        A redirect to the frontend.
    """
    # The state parameter contains the user ID
    user_id = state

    # Construct the redirect URI (must match the one used in the authorization request)
    redirect_uri = f"{os.environ.get('API_BASE_URL', 'http://localhost:3000')}/api/v1/google-oauth2/callback"

    # Exchange the authorization code for tokens
    token_params = {
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
    }

    try:
        token_response = requests.post(GOOGLE_TOKEN_URL, data=token_params)
        token_response.raise_for_status()
        token_data = token_response.json()
    except requests.RequestException as e:
        logging.exception(token_response.content)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to exchange authorization code for tokens: {str(e)}",
        )

    # Extract tokens and scopes
    access_token = token_data.get("access_token")
    refresh_token = token_data.get("refresh_token")
    scopes = token_data.get("scope", "").split(" ")

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No access token received from Google",
        )

    # Update the listener with the tokens and scopes
    listener = await listener_service.update_google_oauth_tokens(
        id=user_id,
        access_token=access_token,
        refresh_token=refresh_token or "",  # Refresh token might not be present if already granted
        scopes=scopes,
    )

    if not listener:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Listener with ID {user_id} not found",
        )

    # Redirect to the frontend
    frontend_url = os.environ.get("FRONTEND_URL", "http://localhost:3000")
    return RedirectResponse(f"{frontend_url}/oauth2-success")
