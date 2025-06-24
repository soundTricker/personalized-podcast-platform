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

import asyncio
import os
import sys
from unittest.mock import AsyncMock, MagicMock, patch

# Set required environment variables for testing
os.environ["GOOGLE_CLOUD_PROJECT"] = "test-project"
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"
os.environ["API_URL"] = "https://api.test.com"

# Add the backend directory to the Python path
sys.path.insert(0, "/")

from datetime import datetime

from ppp.api.v1.endpoints.podcast import get_podcast_audio
from ppp.models.listener_program import ListenerProgram, PublishSetting
from ppp.models.program_broadcast_history import ProgramBroadcastHistory, ProgramBroadcastHistoryStatus


async def test_podcast_audio_endpoint():
    """Test the podcast audio endpoint functionality"""

    # Test data
    program_id = "test_program_123"
    broadcast_history_id = "history_123"
    private_key = "test_private_key_12345678901234567890"

    print("=== Testing Podcast Audio Endpoint ===\n")

    # Test case 1: Program not found (should return 404)
    print("Test 1: Program not found")

    # Create mock services
    listener_program_service = AsyncMock()
    broadcast_history_service = AsyncMock()
    chat_api = AsyncMock()

    listener_program_service.get_by_id.return_value = None

    try:
        await get_podcast_audio(
            program_id=program_id,
            broadcast_history_id=broadcast_history_id,
            private_key=None,
            listener_program_service=listener_program_service,
            broadcast_history_service=broadcast_history_service,
            chat_api=chat_api,
        )
        print("❌ Should have raised 404 error")
    except Exception as e:
        if "404" in str(e) and "Program not found" in str(e):
            print("✅ Correctly returned 404 for missing program")
        else:
            print(f"❌ Unexpected error: {e}")

    # Test case 2: Private program (should return 400)
    print("\nTest 2: Private program")

    # Create fresh mock services
    listener_program_service = AsyncMock()
    broadcast_history_service = AsyncMock()
    chat_api = AsyncMock()

    private_program = ListenerProgram(
        id=program_id, title="Test Private Program", description="This is a private test program", listener_id="listener_123", publish_setting=PublishSetting.PRIVATE, private_key=private_key
    )
    listener_program_service.get_by_id.return_value = private_program

    try:
        await get_podcast_audio(
            program_id=program_id,
            broadcast_history_id=broadcast_history_id,
            private_key=None,
            listener_program_service=listener_program_service,
            broadcast_history_service=broadcast_history_service,
            chat_api=chat_api,
        )
        print("❌ Should have raised 400 error for private program")
    except Exception as e:
        if "400" in str(e) and "private" in str(e).lower():
            print("✅ Correctly returned 400 for private program")
        else:
            print(f"❌ Unexpected error: {e}")

    # Test case 3: Limited program with wrong private key (should return 400)
    print("\nTest 3: Limited program with wrong private key")

    # Create fresh mock services
    listener_program_service = AsyncMock()
    broadcast_history_service = AsyncMock()
    chat_api = AsyncMock()

    limited_program = ListenerProgram(
        id=program_id, title="Test Limited Program", description="This is a limited test program", listener_id="listener_123", publish_setting=PublishSetting.LIMITED, private_key=private_key
    )
    listener_program_service.get_by_id.return_value = limited_program

    try:
        await get_podcast_audio(
            program_id=program_id,
            broadcast_history_id=broadcast_history_id,
            private_key="wrong_key",
            listener_program_service=listener_program_service,
            broadcast_history_service=broadcast_history_service,
            chat_api=chat_api,
        )
        print("❌ Should have raised 400 error for wrong private key")
    except Exception as e:
        if "400" in str(e) and "private key" in str(e).lower():
            print("✅ Correctly returned 400 for wrong private key")
        else:
            print(f"❌ Unexpected error: {e}")

    # Test case 4: Broadcast history not found (should return 404)
    print("\nTest 4: Broadcast history not found")

    # Create fresh mock services
    listener_program_service = AsyncMock()
    broadcast_history_service = AsyncMock()
    chat_api = AsyncMock()

    public_program = ListenerProgram(
        id=program_id, title="Test Public Program", description="This is a public test program", listener_id="listener_123", publish_setting=PublishSetting.PUBLISH, private_key=None
    )
    listener_program_service.get_by_id.return_value = public_program
    broadcast_history_service.get_broadcast_history_by_id.return_value = None

    try:
        await get_podcast_audio(
            program_id=program_id,
            broadcast_history_id=broadcast_history_id,
            private_key=None,
            listener_program_service=listener_program_service,
            broadcast_history_service=broadcast_history_service,
            chat_api=chat_api,
        )
        print("❌ Should have raised 404 error for missing broadcast history")
    except Exception as e:
        if "404" in str(e) and "Broadcast history" in str(e):
            print("✅ Correctly returned 404 for missing broadcast history")
        else:
            print(f"❌ Unexpected error: {e}")

    # Test case 5: Direct artifact serving (no K_SERVICE)
    print("\nTest 5: Direct artifact serving (no K_SERVICE)")

    # Ensure K_SERVICE is not in environment
    if "K_SERVICE" in os.environ:
        del os.environ["K_SERVICE"]

    # Create fresh mock services
    listener_program_service = AsyncMock()
    broadcast_history_service = AsyncMock()
    chat_api = AsyncMock()

    public_program = ListenerProgram(
        id=program_id, title="Test Public Program", description="This is a public test program", listener_id="listener_123", publish_setting=PublishSetting.PUBLISH, private_key=None
    )
    listener_program_service.get_by_id.return_value = public_program

    success_history = ProgramBroadcastHistory(
        id=broadcast_history_id,
        no=1,
        app_name="test_app",
        listener_id="listener_123",
        session_id="session_123",
        artifact_id="artifact_123",
        status=ProgramBroadcastHistoryStatus.SUCCESS,
        size=1024000,
        created_at=datetime.now(),
    )
    broadcast_history_service.get_broadcast_history_by_id.return_value = success_history

    # Mock artifact
    mock_artifact = MagicMock()
    mock_artifact.inline_data.data = b"fake_audio_data"
    mock_artifact.inline_data.mime_type = "audio/mp3"
    chat_api.load_artifact.return_value = mock_artifact

    try:
        response = await get_podcast_audio(
            program_id=program_id,
            broadcast_history_id=broadcast_history_id,
            private_key=None,
            listener_program_service=listener_program_service,
            broadcast_history_service=broadcast_history_service,
            chat_api=chat_api,
        )
        print("✅ Successfully returned audio response via direct artifact serving")

        # Check response properties
        if hasattr(response, "body") and response.body == b"fake_audio_data":
            print("✅ Response contains correct audio data")
        else:
            print("❌ Response missing correct audio data")

    except Exception as e:
        print(f"❌ Unexpected error in direct serving: {e}")

    # Test case 6: GCS signed URL (with K_SERVICE)
    print("\nTest 6: GCS signed URL (with K_SERVICE)")

    # Set K_SERVICE environment variable
    os.environ["K_SERVICE"] = "test-service"

    # Create fresh mock services
    listener_program_service = AsyncMock()
    broadcast_history_service = AsyncMock()
    chat_api = AsyncMock()

    public_program = ListenerProgram(
        id=program_id, title="Test Public Program", description="This is a public test program", listener_id="listener_123", publish_setting=PublishSetting.PUBLISH, private_key=None
    )
    listener_program_service.get_by_id.return_value = public_program

    success_history = ProgramBroadcastHistory(
        id=broadcast_history_id,
        no=1,
        app_name="test_app",
        listener_id="listener_123",
        session_id="session_123",
        artifact_id="artifact_123",
        status=ProgramBroadcastHistoryStatus.SUCCESS,
        size=1024000,
        created_at=datetime.now(),
    )
    broadcast_history_service.get_broadcast_history_by_id.return_value = success_history

    # Mock GCS client and blob
    with patch("ppp.api.v1.endpoints.podcast.storage") as mock_storage:
        mock_client = MagicMock()
        mock_bucket = MagicMock()
        mock_blob = MagicMock()

        mock_storage.Client.return_value = mock_client
        mock_client.bucket.return_value = mock_bucket
        mock_bucket.blob.return_value = mock_blob
        mock_blob.generate_signed_url.return_value = "https://signed-url.example.com/audio.mp3"

        try:
            response = await get_podcast_audio(
                program_id=program_id,
                broadcast_history_id=broadcast_history_id,
                private_key=None,
                listener_program_service=listener_program_service,
                broadcast_history_service=broadcast_history_service,
                chat_api=chat_api,
            )
            print("✅ Successfully generated GCS signed URL response")

            # Check if it's a redirect response
            if hasattr(response, "status_code") and response.status_code == 302:
                print("✅ Response is a redirect (302)")
            else:
                print("❌ Response is not a redirect")

        except Exception as e:
            print(f"❌ Unexpected error in GCS signed URL: {e}")

    print("\n=== All tests completed ===")


if __name__ == "__main__":
    asyncio.run(test_podcast_audio_endpoint())
