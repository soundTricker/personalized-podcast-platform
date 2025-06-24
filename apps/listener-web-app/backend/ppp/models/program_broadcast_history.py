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

from enum import Enum

from firedantic import AsyncSubCollection
from pydantic import Field

from ppp.models.base import BaseSubModel
from ppp.settings import get_settings


class ProgramBroadcastHistoryStatus(str, Enum):
    PREPARE = "prepare"
    GENERATING = "generating"
    SUCCESS = "success"
    FAILURE = "failure"


class ProgramBroadcastHistory(BaseSubModel):
    no: int = Field(description="number of broadcast", min=0)
    app_name: str = Field(description="app name")
    listener_id: str = Field(description="listener ID")
    session_id: str = Field(description="session id")
    artifact_id: str | None = Field(description="artifact id", default=None)
    news_letter_contents: str | None = Field(description="news letter contents", default=None)
    talk_script: str | None = Field(description="generated talk script", default=None)
    error: str | None = Field(description="error", default=None)
    status: ProgramBroadcastHistoryStatus = Field(default=ProgramBroadcastHistoryStatus.PREPARE, description="status")
    dry_run: bool = Field(description="dry run", default=False)
    size: int | None = Field(description="audio file size in bytes", default=None)

    def gcs_uri(self, version="0"):
        settings = get_settings()
        return f"gs://{settings.ARTIFACT_BUCKET}/{self.app_name}/{self.listener_id}/{self.session_id}/{self.artifact_id}/{version}"

    class Collection(AsyncSubCollection):
        __collection_tpl__ = "listener_programs/{id}/broadcast_history"
