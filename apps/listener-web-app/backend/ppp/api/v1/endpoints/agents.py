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

import logging
import threading
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from google.adk import Runner
from google.adk.agents import RunConfig
from google.adk.agents.run_config import StreamingMode
from google.adk.artifacts import BaseArtifactService, GcsArtifactService, InMemoryArtifactService
from google.adk.auth.credential_service.base_credential_service import BaseCredentialService
from google.adk.auth.credential_service.in_memory_credential_service import InMemoryCredentialService
from google.adk.memory import BaseMemoryService, InMemoryMemoryService, VertexAiRagMemoryService
from google.adk.sessions import BaseSessionService, InMemorySessionService, Session, VertexAiSessionService
from google.genai import types

from ppp.agents.concierge.agent import RadioProgramCreatingAssistantAgent
from ppp.schemas.agents import AgentRunRequest
from ppp.settings import Settings, get_settings
from ppp.utils.auth import get_current_user_id

router = APIRouter()

logger = logging.getLogger(__name__)

agent_map = {
    "concierge": RadioProgramCreatingAssistantAgent(),
}

runner_dict = {}


class AgentServices:
    _instance = None
    _lock = threading.Lock()
    settings = None
    _session_service = None
    _artifact_service = None
    _memory_service = None
    _credential_service = None

    def __new__(cls, settings: Settings):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(AgentServices, cls).__new__(cls)
                    cls._instance.settings = settings
                    cls._instance._initialize(settings)
        return cls._instance

    def _initialize(self, settings: Settings):
        self._credential_service = InMemoryCredentialService()
        memory_service_uri = settings.MEMORY_SERVICE_URI
        if memory_service_uri:
            if memory_service_uri.startswith("rag://"):
                rag_corpus = memory_service_uri.split("://")[1]
                if not rag_corpus:
                    raise Exception("Rag corpus can not be empty.")
                self._memory_service = VertexAiRagMemoryService(rag_corpus=f"projects/{settings.GOOGLE_CLOUD_PROJECT}/locations/{settings.GOOGLE_CLOUD_LOCATION}/ragCorpora/{rag_corpus}")
            else:
                raise Exception("Unsupported memory service URI: %s" % memory_service_uri)
        else:
            self._memory_service = InMemoryMemoryService()

        session_service_uri = settings.SESSION_SERVICE_URI

        if session_service_uri and session_service_uri.startswith("agentengine://"):
            # Create vertex session service
            agent_engine_id = session_service_uri.split("://")[1]
            if not agent_engine_id:
                raise Exception("Agent engine id can not be empty.")
            self._session_service = VertexAiSessionService(
                project=settings.GOOGLE_CLOUD_PROJECT,
                location=settings.GOOGLE_CLOUD_LOCATION,
                agent_engine_id=agent_engine_id,
            )
        else:
            self._session_service = InMemorySessionService()

        artifact_service_uri = settings.ARTIFACT_SERVICE_URI
        if artifact_service_uri:
            if artifact_service_uri.startswith("gs://"):
                gcs_bucket = artifact_service_uri.split("://")[1]
                self._artifact_service = GcsArtifactService(bucket_name=gcs_bucket)
            else:
                raise Exception("Unsupported artifact service URI: %s" % artifact_service_uri)
        else:
            self._artifact_service = InMemoryArtifactService()

    @property
    def session_service(self):
        return self._session_service

    @property
    def artifact_service(self):
        return self._artifact_service

    @property
    def memory_service(self):
        return self._memory_service

    @property
    def credential_service(self):
        return self._credential_service


def get_session_service(settings: Settings = Depends(get_settings)):
    service = AgentServices(settings)
    return service.session_service


def get_artifact_service(settings: Settings = Depends(get_settings)):
    service = AgentServices(settings)
    return service.artifact_service


def get_memory_service(settings: Settings = Depends(get_settings)):
    service = AgentServices(settings)
    return service.memory_service


def get_credential_service(settings: Settings = Depends(get_settings)):
    service = AgentServices(settings)
    return service.credential_service


async def _get_runner_async(
    app_name: str, artifact_service: BaseArtifactService, session_service: BaseSessionService, memory_service: BaseMemoryService, credential_service: BaseCredentialService
) -> Runner:
    if app_name in runner_dict:
        return runner_dict[app_name]

    root_agent = agent_map[app_name]

    runner = Runner(
        app_name=app_name,
        agent=root_agent,
        artifact_service=artifact_service,
        session_service=session_service,
        memory_service=memory_service,
        credential_service=credential_service,
    )
    runner_dict[app_name] = runner
    return runner


@router.post("/{app_name}/session", operation_id="create_chat_session")
async def create_session(
    app_name: str,
    state: Optional[dict[str, Any]] = None,
    user_id: str = Depends(get_current_user_id),
    session_service: BaseSessionService = Depends(get_session_service),
) -> Session:
    """
    Create a new chat session.
    """

    if state is None:
        state = {}

    state["user:listener_id"] = user_id
    session = await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        state=state,
    )
    return session


@router.get("/{app_name}/session/{session_id}", operation_id="get_chat_session")
async def get_session(
    app_name: str,
    session_id: str,
    user_id: str = Depends(get_current_user_id),
    session_service: BaseSessionService = Depends(get_session_service),
) -> Session:
    """
    Get a chat session.
    """
    session = await session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)
    if session is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found.")
    return session


@router.post("/chat")
async def chat(
    req: AgentRunRequest,
    user_id: str = Depends(get_current_user_id),
    artifact_service: BaseArtifactService = Depends(get_artifact_service),
    memory_service: BaseMemoryService = Depends(get_memory_service),
    credential_service: BaseCredentialService = Depends(get_credential_service),
    session_service: BaseSessionService = Depends(get_session_service),
) -> StreamingResponse:
    # SSE endpoint

    session = await session_service.get_session(app_name=req.app_name, user_id=user_id, session_id=req.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Convert the events to properly formatted SSE
    async def event_generator():
        try:
            stream_mode = StreamingMode.SSE if req.streaming else StreamingMode.NONE
            runner = await _get_runner_async(
                req.app_name,
                artifact_service=artifact_service,
                session_service=session_service,
                memory_service=memory_service,
                credential_service=credential_service,
            )
            async for event in runner.run_async(
                user_id=user_id,
                session_id=req.session_id,
                new_message=types.UserContent(parts=[types.Part(text=req.new_message)]),
                run_config=RunConfig(streaming_mode=stream_mode),
            ):
                # Format as SSE data
                sse_event = event.model_dump_json(exclude_none=True, by_alias=True)
                logger.info("Generated event in agent run streaming: %s", sse_event)
                yield f"data: {sse_event}\n\n"
        except Exception as e:
            logger.exception("Error in event_generator: %s", e)
            # You might want to yield an error event here
            yield f'data: {{"error": "{str(e)}"}}\n\n'

    # Returns a streaming response with the proper media type for SSE
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
    )
