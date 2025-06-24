#!/usr/bin/env python3
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
Simple test script to verify RSS generation functionality.
"""

from feedgen.feed import FeedGenerator

def test_rss_generation():
    """Test basic RSS generation with feedgen library."""
    try:
        # Create feed generator
        fg = FeedGenerator()

        # Set required fields
        fg.title("Test Podcast")
        fg.description("Test podcast description")
        fg.link(href="http://example.com/rss", rel="self")
        fg.language("ja")

        # iTunes specific tags
        fg.load_extension('podcast')
        fg.podcast.itunes_category("Technology")
        fg.podcast.itunes_author("Test Author")
        fg.podcast.itunes_subtitle("Test subtitle")
        fg.podcast.itunes_summary("Test summary")
        fg.podcast.itunes_owner(name="Test Owner", email="test@example.com")
        fg.podcast.itunes_explicit(False)

        # Add a test episode
        fe = fg.add_entry()
        fe.title("Test Episode")
        fe.description("Test episode description")
        fe.guid("test-episode-1", permalink=False)
        fe.enclosure("http://example.com/audio.mp3", "1000000", "audio/mp3")
        fe.load_extension('podcast')
        fe.podcast.itunes_duration("10:00")
        fe.podcast.itunes_explicit(False)

        # Generate RSS
        rss_xml = fg.rss_str(pretty=True).decode("utf-8")

        # Basic validation
        assert "<?xml version=" in rss_xml
        assert "Test Podcast" in rss_xml
        assert "Test Episode" in rss_xml
        assert "audio/mp3" in rss_xml

        print("✓ RSS generation test passed!")
        print(f"Generated RSS length: {len(rss_xml)} characters")

        return True

    except Exception as e:
        print(f"✗ RSS generation test failed: {e}")
        return False

if __name__ == "__main__":
    test_rss_generation()
