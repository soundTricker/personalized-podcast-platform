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
from unittest.mock import AsyncMock

# Set required environment variables for testing
os.environ["GOOGLE_CLOUD_PROJECT"] = "test-project"
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"
os.environ["API_URL"] = "https://api.test.com"

# Add the backend directory to the Python path
sys.path.insert(0, "/")

from datetime import datetime

from ppp.models.listener_program import ListenerProgram, PublishSetting
from ppp.models.program_broadcast_history import ProgramBroadcastHistory, ProgramBroadcastHistoryStatus
from ppp.services.rss import RSSService


async def test_rss_service():
    """Test the RSS service functionality"""

    # Test data
    program_id = "test_program_123"
    private_key = "test_private_key_12345678901234567890"

    # Test case 1: Program not found (should return 404)
    print("Test 1: Program not found")

    # Create fresh mock services for this test
    listener_program_service = AsyncMock()
    program_broadcast_history_service = AsyncMock()
    rss_service = RSSService(listener_program_service, program_broadcast_history_service)

    listener_program_service.get_by_id.return_value = None

    try:
        await rss_service.generate_rss_feed(program_id)
        print("❌ Should have raised 404 error")
    except Exception as e:
        if "404" in str(e) and "Program not found" in str(e):
            print("✅ Correctly returned 404 for missing program")
        else:
            print(f"❌ Unexpected error: {e}")

    # Test case 2: Private program (should return 400)
    print("\nTest 2: Private program")

    # Create fresh mock services for this test
    listener_program_service = AsyncMock()
    program_broadcast_history_service = AsyncMock()
    rss_service = RSSService(listener_program_service, program_broadcast_history_service)

    private_program = ListenerProgram(
        id=program_id, title="Test Private Program", description="This is a private test program", listener_id="listener_123", publish_setting=PublishSetting.PRIVATE, private_key=private_key
    )
    listener_program_service.get_by_id.return_value = private_program

    try:
        await rss_service.generate_rss_feed(program_id)
        print("❌ Should have raised 400 error for private program")
    except Exception as e:
        if "400" in str(e) and "private" in str(e).lower():
            print("✅ Correctly returned 400 for private program")
        else:
            print(f"❌ Unexpected error: {e}")

    # Test case 3: Limited program with wrong private key (should return 400)
    print("\nTest 3: Limited program with wrong private key")

    # Create fresh mock services for this test
    listener_program_service = AsyncMock()
    program_broadcast_history_service = AsyncMock()
    rss_service = RSSService(listener_program_service, program_broadcast_history_service)

    limited_program = ListenerProgram(
        id=program_id, title="Test Limited Program", description="This is a limited test program", listener_id="listener_123", publish_setting=PublishSetting.LIMITED, private_key=private_key
    )
    listener_program_service.get_by_id.return_value = limited_program

    try:
        await rss_service.generate_rss_feed(program_id, "wrong_key")
        print("❌ Should have raised 400 error for wrong private key")
    except Exception as e:
        if "400" in str(e) and "private key" in str(e).lower():
            print("✅ Correctly returned 400 for wrong private key")
        else:
            print(f"❌ Unexpected error: {e}")

    # Test case 4: Limited program with correct private key (should work)
    print("\nTest 4: Limited program with correct private key")

    # Create fresh mock services for this test
    listener_program_service = AsyncMock()
    program_broadcast_history_service = AsyncMock()
    rss_service = RSSService(listener_program_service, program_broadcast_history_service)

    # Set up the limited program for this test
    limited_program = ListenerProgram(
        id=program_id, title="Test Limited Program", description="This is a limited test program", listener_id="listener_123", publish_setting=PublishSetting.LIMITED, private_key=private_key
    )
    listener_program_service.get_by_id.return_value = limited_program

    # Mock broadcast histories
    success_history = ProgramBroadcastHistory(
        id="history_1",
        no=1,
        app_name="test_app",
        listener_id="listener_123",
        session_id="session_123",
        artifact_id="artifact_123",
        news_letter_contents="Test episode content",
        status=ProgramBroadcastHistoryStatus.SUCCESS,
        size=1024000,  # 1MB
        created_at=datetime.now(),
    )

    failed_history = ProgramBroadcastHistory(
        id="history_2",
        no=2,
        app_name="test_app",
        listener_id="listener_123",
        session_id="session_123",
        artifact_id="artifact_124",
        status=ProgramBroadcastHistoryStatus.FAILURE,
        size=512000,
        created_at=datetime.now(),
    )

    program_broadcast_history_service.get_broadcast_histories_by_program_id.return_value = [success_history, failed_history]

    try:
        rss_xml = await rss_service.generate_rss_feed(program_id, private_key)
        print("✅ Successfully generated RSS for limited program with correct key")

        # Check if RSS contains expected elements
        if "Test Limited Program" in rss_xml:
            print("✅ RSS contains program title")
        else:
            print("❌ RSS missing program title")

        if "Test episode content" in rss_xml:
            print("✅ RSS contains episode content")
        else:
            print("❌ RSS missing episode content")

        if "1024000" in rss_xml:
            print("✅ RSS contains file size")
        else:
            print("❌ RSS missing file size")

        # Should only contain success episodes (not failed ones)
        if "history_1" in rss_xml and "history_2" not in rss_xml:
            print("✅ RSS correctly filters only SUCCESS episodes")
        else:
            print("❌ RSS filtering not working correctly")

        # Check enclosure URL format
        if f"/podcast/audio/{program_id}/history_1?private_key={private_key}" in rss_xml:
            print("✅ RSS contains correct enclosure URL with private key")
        else:
            print("❌ RSS missing correct enclosure URL format")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    # Test case 5: Public program (should work without private key)
    print("\nTest 5: Public program")

    # Create fresh mock services for this test
    listener_program_service = AsyncMock()
    program_broadcast_history_service = AsyncMock()
    rss_service = RSSService(listener_program_service, program_broadcast_history_service)

    public_program = ListenerProgram(
        id=program_id, title="Test Public Program", description="This is a public test program", listener_id="listener_123", publish_setting=PublishSetting.PUBLISH, private_key=None
    )
    listener_program_service.get_by_id.return_value = public_program

    # Mock broadcast histories for public program test
    success_history = ProgramBroadcastHistory(
        id="history_1",
        no=1,
        app_name="test_app",
        listener_id="listener_123",
        session_id="session_123",
        artifact_id="artifact_123",
        news_letter_contents="Test episode content",
        status=ProgramBroadcastHistoryStatus.SUCCESS,
        size=1024000,  # 1MB
        created_at=datetime.now(),
    )
    program_broadcast_history_service.get_broadcast_histories_by_program_id.return_value = [success_history]

    try:
        rss_xml = await rss_service.generate_rss_feed(program_id)
        print("✅ Successfully generated RSS for public program")

        # Check enclosure URL format (should not have private key)
        if f"/podcast/audio/{program_id}/history_1?private_key=" not in rss_xml and f"/podcast/audio/{program_id}/history_1" in rss_xml:
            print("✅ RSS contains correct enclosure URL without private key")
        else:
            print("❌ RSS enclosure URL format incorrect for public program")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    asyncio.run(test_rss_service())
