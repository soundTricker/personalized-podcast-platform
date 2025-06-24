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

import os

import google.auth.credentials
from firedantic import configure
from google.cloud.firestore import AsyncClient, Client


def get_firestore_client(async_client: bool = True) -> Client | AsyncClient:
    """
    Get a Firestore client based on the environment.

    Args:
        async_client: Whether to return an async client or not.

    Returns:
        A Firestore client.
    """
    # Check if running in Firestore emulator
    if os.environ.get("FIRESTORE_EMULATOR_HOST"):
        # Use mock credentials for local development
        from unittest.mock import Mock

        if async_client:
            client = AsyncClient(project="ppp-listener-web-app", credentials=Mock(spec=google.auth.credentials.Credentials))
        else:
            client = Client(project="ppp-listener-web-app", credentials=Mock(spec=google.auth.credentials.Credentials))
    else:
        # Use default credentials for production
        if async_client:
            client = AsyncClient()
        else:
            client = Client()

    return client


def configure_firedantic(client: Client | AsyncClient | None = None, prefix: str = "ppp-"):
    """
    Configure Firedantic with the given client and prefix.

    Args:
        client: The Firestore client to use. If None, a new client will be created.
        prefix: The collection prefix to use.
    """
    if client is None:
        client = get_firestore_client()

    configure(client, prefix=prefix)
