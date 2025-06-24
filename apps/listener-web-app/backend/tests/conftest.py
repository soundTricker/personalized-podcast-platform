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
from unittest.mock import Mock

import google.auth.credentials
import pytest
from fastapi.testclient import TestClient
from google.cloud.firestore import AsyncClient

from ppp.firestore.client import configure_firedantic
from ppp.main import app


@pytest.fixture
def client():
    """
    Create a test client for FastAPI.

    Returns:
        A test client for FastAPI.
    """
    return TestClient(app)


@pytest.fixture(autouse=True)
def setup_firestore():
    """
    Set up Firestore for testing.

    This fixture is automatically used for all tests.
    It configures Firedantic to use the Firestore emulator.
    """
    # Set environment variable for Firestore emulator
    os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"

    # Create a Firestore client with mock credentials
    client = AsyncClient(project="ppp-test", credentials=Mock(spec=google.auth.credentials.Credentials))

    # Configure Firedantic with the test client
    configure_firedantic(client, prefix="ppp-test-")

    yield

    # Clean up
    os.environ.pop("FIRESTORE_EMULATOR_HOST", None)
