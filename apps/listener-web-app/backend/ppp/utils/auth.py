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

import firebase_admin
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth, credentials

# Initialize Firebase Admin SDK
cred = None
try:
    # Try to initialize with default credentials
    import os

    if os.environ.get("FIRESTORE_EMULATOR_HOST"):
        firebase_admin.initialize_app(options={"projectId": "ppp-listener-web-app"})
    else:
        firebase_admin.initialize_app()
except ValueError:
    # If already initialized, get the default app
    try:
        firebase_admin.get_app()
    except ValueError:
        # If running locally, use a service account

        if os.environ.get("FIRESTORE_EMULATOR_HOST"):
            # Use mock credentials for local development
            cred = credentials.Certificate("path/to/service-account.json")
            firebase_admin.initialize_app(cred)

# Create security scheme
security = HTTPBearer()


async def verify_id_token(token) -> dict:
    try:
        # Verify the ID token
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """
    Get the current user from the Firebase ID token.

    Args:
        credentials: The HTTP authorization credentials.

    Returns:
        The user claims from the Firebase ID token.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    token = credentials.credentials
    return await verify_id_token(token)


async def get_current_user_id(user: dict = Depends(get_current_user)) -> str:
    """
    Get the current user ID from the Firebase ID token.

    Args:
        user: The user claims from the Firebase ID token.

    Returns:
        The user ID.
    """
    return user["uid"]
