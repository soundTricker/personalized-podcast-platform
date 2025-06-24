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

from typing import Optional

from pydantic import Field

from ppp.models.program_broadcast_history import ProgramBroadcastHistoryStatus
from ppp.schemas.base import BaseCreateSchema, BaseSchema, BaseUpdateSchema


class ProgramBroadcastHistorySchema(BaseSchema):
    """
    Schema for ProgramBroadcastHistory response.
    """

    no: int
    app_name: str
    listener_id: str
    session_id: str
    artifact_id: str | None
    status: ProgramBroadcastHistoryStatus
    news_letter_contents: str | None
    talk_script: str | None
    dry_run: bool = False

    def gcs_uri(self, version="0"):
        """
        Get the GCS URI for the broadcast artifact.
        """
        from ppp.settings import get_settings

        settings = get_settings()
        return f"gs://{settings.ARTIFACT_BUCKET}/{self.app_name}/{self.listener_id}/{self.session_id}/{self.artifact_id}/{version}"


class ProgramBroadcastHistoryCreate(BaseCreateSchema):
    """
    Schema for creating a ProgramBroadcastHistory.
    """

    no: int = Field(description="Number of broadcast", ge=0)
    app_name: str = Field(description="App name")
    listener_id: str = Field(description="Listener ID")
    session_id: str = Field(description="Session ID")
    artifact_id: str | None = Field(description="Artifact ID", default=None)
    status: ProgramBroadcastHistoryStatus = Field(default=ProgramBroadcastHistoryStatus.GENERATING, description="Status")


class ProgramBroadcastHistoryUpdate(BaseUpdateSchema):
    """
    Schema for updating a ProgramBroadcastHistory.
    """

    status: Optional[ProgramBroadcastHistoryStatus] = Field(default=None, description="Status")
