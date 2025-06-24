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

from typing import Any, AsyncIterable

from google.adk.agents.run_config import StreamingMode
from google.adk.artifacts import BaseArtifactService
from google.adk.runners import RunConfig
from vertexai.preview import reasoning_engines


class CustomAdkApp(reasoning_engines.AdkApp):
    """An ADK Application."""

    def clone(self):
        """Returns a clone of the ADK application."""
        import copy

        return CustomAdkApp(
            agent=copy.deepcopy(self._tmpl_attrs.get("agent")),
            enable_tracing=self._tmpl_attrs.get("enable_tracing"),
            session_service_builder=self._tmpl_attrs.get("session_service_builder"),
            artifact_service_builder=self._tmpl_attrs.get("artifact_service_builder"),
            env_vars=self._tmpl_attrs.get("env_vars"),
        )

    def set_up(self):
        super().set_up()

        import os

        import google.cloud.logging

        self.logging_client = google.cloud.logging.Client(project=os.environ.get("GOOGLE_CLOUD_PROJECT"))
        self.logging_client.setup_logging(
            name="ppp.radio-station.log",  # the ID of the logName in Cloud Logging.
            resource=google.cloud.logging.Resource(
                type="aiplatform.googleapis.com/ReasoningEngine",
                labels={
                    "location": "us-central1",
                    "resource_container": os.environ.get("GOOGLE_CLOUD_PROJECT"),
                    "reasoning_engine_id": os.environ.get("K_SERVICE", "").split("-")[-1],
                },
            ),
        )

    def stream_query_sse(
        self,
        *,
        message: str | dict[str, Any],
        user_id: str,
        session_id: str | None = None,
        **kwargs,
    ):
        return self.stream_query(message=message, user_id=user_id, session_id=session_id, run_config=RunConfig(streaming_mode=StreamingMode.SSE), **kwargs)

    async def async_stream_query_sse(
        self,
        *,
        message: str | dict[str, Any],
        user_id: str,
        session_id: str | None = None,
        **kwargs,
    ) -> AsyncIterable[dict[str, Any]]:
        return self.async_stream_query(message=message, user_id=user_id, session_id=session_id, run_config=RunConfig(streaming_mode=StreamingMode.SSE), **kwargs)

    async def load_artifact(self, user_id: str, session_id: str, artifact_id: str, **kwargs):
        artifact_service: BaseArtifactService = self._tmpl_attrs["artifact_service"]
        return await artifact_service.load_artifact(app_name=self._tmpl_attrs.get("app_name"), user_id=user_id, session_id=session_id, filename=artifact_id)

    async def list_artifact(self, user_id: str, session_id: str, **kwargs):
        artifact_service: BaseArtifactService = self._tmpl_attrs["artifact_service"]
        return await artifact_service.list_artifact_keys(app_name=self._tmpl_attrs.get("app_name"), user_id=user_id, session_id=session_id)

    def register_operations(self) -> dict[str, list[str]]:
        """Registers the operations of the ADK application."""
        return {
            "": [
                "get_session",
                "list_sessions",
                "create_session",
                "delete_session",
            ],
            "async": [
                "async_get_session",
                "async_list_sessions",
                "async_create_session",
                "async_delete_session",
                "load_artifact",
            ],
            "stream": ["stream_query_sse", "stream_query", "streaming_agent_run_with_events"],
            "async_stream": ["async_stream_query", "async_stream_query_sse"],
        }
