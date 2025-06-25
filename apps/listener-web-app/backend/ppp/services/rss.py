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

from datetime import datetime, timezone
from typing import List, Optional

from fastapi import Depends, HTTPException
from feedgen.feed import FeedGenerator

from ppp.models.listener import Listener
from ppp.models.listener_program import ListenerProgram, PublishSetting
from ppp.models.program_broadcast_history import ProgramBroadcastHistory, ProgramBroadcastHistoryStatus
from ppp.services.listener import get_listener_service, ListenerService
from ppp.services.listener_program import ListenerProgramService, get_listener_program_service
from ppp.services.program_broadcast_history import ProgramBroadcastHistoryService, get_program_broadcast_history_service
from ppp.settings import get_settings


class RSSService:
    """
    Service for RSS feed generation for podcasts.
    """

    def __init__(
        self,
        listener_service: ListenerService,
        listener_program_service: ListenerProgramService,
        program_broadcast_history_service: ProgramBroadcastHistoryService,
    ):
        """
        Initialize the RSS service.
        """
        self.listener_service = listener_service
        self.listener_program_service = listener_program_service
        self.program_broadcast_history_service = program_broadcast_history_service
        self.settings = get_settings()

    async def generate_rss_feed(self, program_id: str, private_key: Optional[str] = None) -> str:
        """
        Generate RSS feed for a podcast program.

        Args:
            program_id: The ID of the program.
            private_key: The private key for limited access (optional).

        Returns:
            RSS feed as XML string.

        Raises:
            HTTPException: If program not found, access denied, or other errors.
        """
        # 1. Get ListenerProgram by program_id
        program = await self.listener_program_service.get_by_id(program_id)
        if not program:
            raise HTTPException(status_code=404, detail="Program not found")

        # 2. Check publish_setting
        if program.publish_setting == PublishSetting.PRIVATE:
            raise HTTPException(status_code=400, detail="Program is private")

        if program.publish_setting == PublishSetting.LIMITED:
            if not private_key or private_key != program.private_key:
                raise HTTPException(status_code=400, detail="Invalid private key")

        # 3. Get ProgramBroadcastHistory with status=success
        all_histories = await self.program_broadcast_history_service.get_broadcast_histories_by_program_id(program_id)
        success_histories = [h for h in all_histories if h.status == ProgramBroadcastHistoryStatus.SUCCESS]
        
        # 4. Get Listener
        listener = await self.listener_service.get_listener_by_id(program.listener_id)

        if not listener:
            raise HTTPException(status_code=404, detail="Listener not found")

        # 5. Generate RSS feed
        rss_xml = self._create_rss_feed(listener, program, success_histories, private_key)

        return rss_xml

    def _create_rss_feed(self, listener: Listener, program: ListenerProgram, histories: List[ProgramBroadcastHistory], private_key: Optional[str] = None) -> str:
        """
        Create RSS feed using feedgen library.

        Args:
            listener: The Listener instance
            program: The ListenerProgram instance.
            histories: List of successful ProgramBroadcastHistory instances.
            private_key: The private key for limited access (optional).

        Returns:
            RSS feed as XML string.
        """
        # Create feed generator
        fg = FeedGenerator()

        # Load podcast extension if not already loaded
        if not hasattr(fg, "_FeedGenerator__extensions") or "podcast" not in fg._FeedGenerator__extensions:
            fg.load_extension("podcast")

        # Channel level tags
        fg.title(program.title)
        fg.description(program.description)
        fg.link(href=f"{self.settings.API_BASE_URL}/api/v1/podcast/rss/{program.id}", rel="self")
        fg.language("ja")  # Japanese language

        # iTunes specific tags
        # TODO category
        fg.podcast.itunes_category("Technology")  # Default category, can be customized
        fg.podcast.itunes_author("Personalized Podcast Platform -PPP-")  # Default author
        fg.podcast.itunes_subtitle(program.description[:255])  # Subtitle (max 255 chars)
        fg.podcast.itunes_summary(program.description)

        # TODO override owner each program
        fg.podcast.itunes_owner(name="Personalized Podcast Platform", email=listener.email)  # Default owner info
        fg.podcast.itunes_explicit("no")  # Use "no" instead of False

        # Cover art image tags
        if program.cover_art_uri:
            # Construct cover URL
            if program.publish_setting == PublishSetting.PUBLISH:
                # Public access - no private_key needed
                cover_url = f"{self.settings.API_BASE_URL}/api/v1/podcast/cover/{program.id}"
            else:
                # Limited access - include private_key
                cover_url = f"{self.settings.API_BASE_URL}/api/v1/podcast/cover/{program.id}?private_key={private_key}"
        else:
            cover_url = f"{self.settings.API_BASE_URL}/ppp_logo.jpeg"

        # iTunes image tag
        fg.podcast.itunes_image(cover_url)

        # Standard RSS image tag
        fg.image(url=cover_url, title=program.title, link=f"{self.settings.API_BASE_URL}/api/v1/podcast/rss/{program.id}")

        # Add episodes from broadcast histories
        for history in histories:
            self._add_episode_to_feed(fg, program, history, private_key)

        # Generate RSS XML
        return fg.rss_str(pretty=True).decode("utf-8")

    def _add_episode_to_feed(self, fg: FeedGenerator, program: ListenerProgram, history: ProgramBroadcastHistory, private_key: Optional[str] = None) -> None:
        """
        Add an episode to the RSS feed.

        Args:
            fg: FeedGenerator instance.
            program: The ListenerProgram instance.
            history: The ProgramBroadcastHistory instance.
            private_key: The private key for limited access (optional).
        """
        fe = fg.add_entry()

        # Load podcast extension for the entry if not already loaded
        if not hasattr(fe, "_FeedEntry__extensions") or "podcast" not in fe._FeedEntry__extensions:
            fe.load_extension("podcast")

        # Episode title
        episode_title = f"{program.title} - Episode {history.no}"
        fe.title(episode_title)

        # Episode description
        episode_description = history.news_letter_contents or f"Episode {history.no} of {program.title}"
        fe.description(episode_description)

        # Episode GUID (unique identifier)
        fe.guid(f"{program.id}-{history.id}", permalink=False)

        # Publication date
        pub_date = history.created_at if history.created_at else datetime.now(timezone.utc)
        # Ensure timezone-aware datetime
        if pub_date.tzinfo is None:
            pub_date = pub_date.replace(tzinfo=timezone.utc)
        fe.pubDate(pub_date)

        # Enclosure URL
        if program.publish_setting == PublishSetting.PUBLISH:
            # Public access - no private_key needed
            enclosure_url = f"{self.settings.API_BASE_URL}/api/v1/podcast/audio/{program.id}/{history.id}"
        else:
            # Limited access - include private_key
            enclosure_url = f"{self.settings.API_BASE_URL}/api/v1/podcast/audio/{program.id}/{history.id}?private_key={private_key}"

        # Enclosure tag with URL, length, and type
        file_size = history.size or 0  # Use 0 if size is not available
        fe.enclosure(enclosure_url, str(file_size), "audio/mp3")

        # iTunes episode specific tags
        fe.podcast.itunes_duration(f"{program.program_minutes}:00")  # Duration in MM:SS format
        fe.podcast.itunes_explicit("no")  # Use "no" instead of False


def get_rss_service(
    listener_service=Depends(get_listener_service),
    listener_program_service=Depends(get_listener_program_service),
    program_broadcast_history_service=Depends(get_program_broadcast_history_service),
) -> RSSService:
    """
    Dependency to get the RSSService.
    """
    return RSSService(listener_service, listener_program_service, program_broadcast_history_service)
