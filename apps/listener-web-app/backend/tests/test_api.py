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

from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient):
    """
    Test the root endpoint.

    Args:
        client: The test client.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to PPP Listener Web API"}


def test_api_v1_endpoint(client: TestClient):
    """
    Test the API v1 endpoint.

    Args:
        client: The test client.
    """
    # This test will fail until we implement the API v1 endpoint
    # Uncomment when the endpoint is implemented
    # response = client.get("/api/v1")
    # assert response.status_code == 200
    pass
