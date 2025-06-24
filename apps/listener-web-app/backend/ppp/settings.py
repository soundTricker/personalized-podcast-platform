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

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

BackendType = Literal["agentengine", "remote"]


class Settings(BaseSettings):
    GOOGLE_CLOUD_PROJECT: str
    GOOGLE_CLOUD_LOCATION: str
    BACKEND_TYPE: BackendType = "remote"
    BACKEND_URL: str | None = "http://localhost:8000"
    AGENT_ENGINE_ID: str | None = None
    CHAINLIT_AUTH_SECRET: str | None = None
    ARTIFACT_BUCKET: str | None = None
    API_BASE_URL: str | None = None
    MCP_ENDPOINT_URL: str | None = None
    RSS_FEED_RAG_CORPUS_ID: str | None = None
    SESSION_SERVICE_URI: str | None = None
    MEMORY_SERVICE_URI: str | None = None
    ARTIFACT_SERVICE_URI: str | None = None

    model_config = SettingsConfigDict(extra="allow")

    @property
    def backend_url(self):
        if self.BACKEND_TYPE != "agentengine":
            return self.BACKEND_URL
        return (f"https://{self.GOOGLE_CLOUD_LOCATION}-aiplatform.googleapis.com/v1/{self.agent_engine_name}",)

    @property
    def agent_engine_name(self):
        return self.AGENT_ENGINE_ID


def get_settings() -> Settings:
    return Settings()  # ty: ignore[missing-argument]
