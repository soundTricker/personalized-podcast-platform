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

# tests/api/v1/endpoints/test_listener_programs.py

from unittest.mock import AsyncMock

import pytest
from fastapi import FastAPI, status
from fastapi.testclient import TestClient

from ppp.api.v1.endpoints.listener_programs import get_listener_program_service

# Import the router and the specific dependency functions to override them directly
from ppp.api.v1.endpoints.listener_programs import router as listener_programs_router
from ppp.models.listener_program import ListenerProgram, ProgramStatus
from ppp.schemas.listener_program import (
    ListenerProgramCreateSchema,
    ListenerProgramUpdateSchema,
)
from ppp.services.listener_program import ListenerProgramService
from ppp.utils.auth import get_current_user_id

# Create a FastAPI app instance for testing and include the router
app = FastAPI()
app.include_router(
    listener_programs_router,
    prefix="/api/v1/listener-programs",  # Match your actual prefix
    tags=["listener-programs"],
)

# Test client
client = TestClient(app)

# Mock user ID for testing
TEST_USER_ID = "test_user_auth0_123"


# Sample data factory for ListenerProgram
def create_sample_program_model(**overrides) -> ListenerProgram:
    """Helper to create ListenerProgram model instances for mocking service returns."""
    defaults = {
        "id": "prog_default_id_123",
        "listener_id": TEST_USER_ID,
        "title": "Default Test Program",
        "description": "A default description for testing.",
        "program_minutes": 10,
        "insert_music": True,
        "base_radio_cast_ids": ["cast_id_1", "cast_id_2"],
        "status": ProgramStatus.DRAFT,
        "created_at": "2023-10-26T10:00:00Z",  # ISO format string
        "updated_at": "2023-10-26T10:00:00Z",  # ISO format string
        "published_at": None,
        "generated_script": None,
        "generated_audio_url": None,
        "error_message": None,
    }
    # Pydantic models are immutable by default, so create a new dict for model creation
    model_data = {**defaults, **overrides}
    return ListenerProgram(**model_data)


@pytest.fixture
def mock_service_instance():
    """Provides a mock instance of ListenerProgramService."""
    service = AsyncMock(spec=ListenerProgramService)
    return service


@pytest.fixture(autouse=True)  # Apply to all tests in this module
def override_auth_dependency():
    """Overrides the get_current_user_id dependency for all tests."""
    app.dependency_overrides[get_current_user_id] = lambda: TEST_USER_ID
    yield
    del app.dependency_overrides[get_current_user_id]  # Clean up


@pytest.fixture(autouse=True)  # Apply to all tests in this module
def override_listener_program_service_dependency(mock_service_instance):
    """Overrides the get_listener_program_service dependency for all tests."""
    app.dependency_overrides[get_listener_program_service] = lambda: mock_service_instance
    yield
    del app.dependency_overrides[get_listener_program_service]  # Clean up


# --- Test Cases ---


@pytest.mark.asyncio
async def test_create_listener_program(mock_service_instance: AsyncMock):
    # Prepare data for creating a listener program
    create_payload = ListenerProgramCreateSchema(
        title="My New Awesome Program",
        description="This is a program created via test.",
        program_minutes=25,
        insert_music=False,
        base_radio_cast_ids=["rc_101", "rc_102"],
        status=ProgramStatus.DRAFT,
    )
    # Define the expected return value from the service
    expected_created_program = create_sample_program_model(
        id="new_prog_id_456",
        title=create_payload.title,
        description=create_payload.description,
        program_minutes=create_payload.program_minutes,
        insert_music=create_payload.insert_music,
        base_radio_cast_ids=create_payload.base_radio_cast_ids,
        status=create_payload.status,
        listener_id=TEST_USER_ID,  # Ensure listener_id is set
    )
    mock_service_instance.create_listener_program.return_value = expected_created_program

    # Make the API call
    response = client.post("/api/v1/listener-programs/", json=create_payload.model_dump())

    # Assertions
    assert response.status_code == status.HTTP_201_CREATED
    response_data = response.json()
    assert response_data["id"] == expected_created_program.id
    assert response_data["title"] == create_payload.title
    assert response_data["listener_id"] == TEST_USER_ID

    # Verify the service method was called correctly
    mock_service_instance.create_listener_program.assert_called_once_with(
        title=create_payload.title,
        description=create_payload.description,
        listener_id=TEST_USER_ID,
        program_minutes=create_payload.program_minutes,
        insert_music=create_payload.insert_music,
        base_radio_cast_ids=create_payload.base_radio_cast_ids,
        status=create_payload.status,
    )


@pytest.mark.asyncio
async def test_get_listener_program_found(mock_service_instance: AsyncMock):
    program_id = "prog_to_get_789"
    expected_program = create_sample_program_model(id=program_id, listener_id=TEST_USER_ID)
    mock_service_instance.verify_program_ownership.return_value = expected_program

    response = client.get(f"/api/v1/listener-programs/{program_id}")

    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert response_data["id"] == program_id
    assert response_data["title"] == expected_program.title
    mock_service_instance.verify_program_ownership.assert_called_once_with(program_id, TEST_USER_ID)


@pytest.mark.asyncio
async def test_get_listener_program_not_found_or_no_permission(mock_service_instance: AsyncMock):
    program_id = "prog_not_exists_123"
    mock_service_instance.verify_program_ownership.return_value = None  # Simulate not found or no permission

    response = client.get(f"/api/v1/listener-programs/{program_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "not found or you don't have permission" in response.json()["detail"]
    mock_service_instance.verify_program_ownership.assert_called_once_with(program_id, TEST_USER_ID)


@pytest.mark.asyncio
async def test_list_listener_programs(mock_service_instance: AsyncMock):
    program1 = create_sample_program_model(id="prog_list_1", title="Program Alpha")
    program2 = create_sample_program_model(id="prog_list_2", title="Program Beta")
    expected_programs_list = [program1, program2]
    mock_service_instance.get_listener_programs_by_listener_id.return_value = expected_programs_list

    response = client.get("/api/v1/listener-programs/")

    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert len(response_data) == 2
    assert response_data[0]["id"] == program1.id
    assert response_data[1]["id"] == program2.id
    mock_service_instance.get_listener_programs_by_listener_id.assert_called_once_with(TEST_USER_ID)


@pytest.mark.asyncio
async def test_update_listener_program(mock_service_instance: AsyncMock):
    program_id_to_update = "prog_to_update_321"
    update_payload = ListenerProgramUpdateSchema(
        title="Updated Program Title",
        description="This description has been updated.",
        program_minutes=30,
        status=ProgramStatus.READY_TO_GENERATE,
        # base_radio_cast_ids can be updated too, ensure it's in schema
        base_radio_cast_ids=["rc_updated_1", "rc_updated_2"],
    )

    # Mock ownership verification
    existing_program = create_sample_program_model(id=program_id_to_update, listener_id=TEST_USER_ID)
    mock_service_instance.verify_program_ownership.return_value = existing_program

    # Mock the result of the update operation
    updated_program_from_service = create_sample_program_model(
        id=program_id_to_update,
        listener_id=TEST_USER_ID,
        title=update_payload.title,
        description=update_payload.description,
        program_minutes=update_payload.program_minutes,
        status=update_payload.status,
        base_radio_cast_ids=update_payload.base_radio_cast_ids,
        updated_at="2023-10-27T12:00:00Z",  # Simulate time update
    )
    mock_service_instance.update_listener_program.return_value = updated_program_from_service

    response = client.put(
        f"/api/v1/listener-programs/{program_id_to_update}",
        json=update_payload.model_dump(exclude_unset=True),  # Important for partial updates
    )

    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert response_data["id"] == program_id_to_update
    assert response_data["title"] == update_payload.title
    assert response_data["status"] == update_payload.status.value  # Compare with enum value

    mock_service_instance.verify_program_ownership.assert_called_once_with(program_id_to_update, TEST_USER_ID)
    # Check all fields passed to update_listener_program, including those not in exclude_unset
    # The service method receives all fields from ListenerProgramUpdateSchema that were provided
    expected_update_args = update_payload.model_dump(exclude_unset=True)
    mock_service_instance.update_listener_program.assert_called_once_with(id=program_id_to_update, **expected_update_args)


@pytest.mark.asyncio
async def test_update_listener_program_not_found_or_no_permission(mock_service_instance: AsyncMock):
    program_id = "prog_update_fail_404"
    update_payload = ListenerProgramUpdateSchema(title="Attempted Update")
    mock_service_instance.verify_program_ownership.return_value = None  # Simulate not found/no permission

    response = client.put(f"/api/v1/listener-programs/{program_id}", json=update_payload.model_dump(exclude_unset=True))

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "not found or you don't have permission to update it" in response.json()["detail"]
    mock_service_instance.verify_program_ownership.assert_called_once_with(program_id, TEST_USER_ID)
    mock_service_instance.update_listener_program.assert_not_called()


@pytest.mark.asyncio
async def test_delete_listener_program(mock_service_instance: AsyncMock):
    program_id_to_delete = "prog_to_delete_654"

    # Mock ownership verification
    existing_program = create_sample_program_model(id=program_id_to_delete, listener_id=TEST_USER_ID)
    mock_service_instance.verify_program_ownership.return_value = existing_program
    mock_service_instance.delete.return_value = None  # Typically delete operations return None or True

    response = client.delete(f"/api/v1/listener-programs/{program_id_to_delete}")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    mock_service_instance.verify_program_ownership.assert_called_once_with(program_id_to_delete, TEST_USER_ID)
    mock_service_instance.delete.assert_called_once_with(program_id_to_delete)


@pytest.mark.asyncio
async def test_delete_listener_program_not_found_or_no_permission(mock_service_instance: AsyncMock):
    program_id = "prog_delete_fail_404"
    mock_service_instance.verify_program_ownership.return_value = None  # Simulate not found/no permission

    response = client.delete(f"/api/v1/listener-programs/{program_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "not found or you don't have permission to delete it" in response.json()["detail"]
    mock_service_instance.verify_program_ownership.assert_called_once_with(program_id, TEST_USER_ID)
    mock_service_instance.delete.assert_not_called()
