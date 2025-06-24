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

from abc import ABC, abstractmethod
from typing import Any, AsyncIterable, Generator

import httpx
import vertexai
from fastapi import Depends
from google.adk.sessions import Session
from google.genai import types
from httpx_sse import aconnect_sse, connect_sse
from pydantic_core import from_json
from vertexai import agent_engines

from ppp.settings import Settings, get_settings
from ppp.utils.httpx_auth import GoogleJWTAuth


class ChatAPI(ABC):
    settings: Settings = get_settings()

    @abstractmethod
    async def get_session(self, user_id: str, session_id: str) -> Session | None:
        raise NotImplementedError("not implemented")

    @abstractmethod
    async def list_sessions(self, user_id: str) -> list[Session]:
        raise NotImplementedError("not implemented")

    @abstractmethod
    async def create_session(self, user_id: str, state: dict[str, Any] | None = None) -> Session:
        raise NotImplementedError("not implemented")

    @abstractmethod
    async def delete_session(self, user_id: str, session_id: str) -> None:
        raise NotImplementedError("not implemented")

    @abstractmethod
    def stream_query(self, message: str | dict[str, Any], user_id: str, session_id: str | None = None, **kwargs) -> Generator[dict[str, Any], None, None]:
        raise NotImplementedError("not implemented")

    @abstractmethod
    async def async_stream_query(self, message: str | dict[str, Any], user_id: str, session_id: str | None = None, **kwargs) -> AsyncIterable[dict[str, Any]]:
        raise NotImplementedError("not implemented")

    @abstractmethod
    async def load_artifact(self, user_id: str, session_id: str, artifact_id: str) -> types.Part:
        raise NotImplementedError("not implemented")


class VertexAIChatAPI(ChatAPI):
    app: agent_engines.AgentEngine

    def __init__(self):
        vertexai.init(project=self.settings.GOOGLE_CLOUD_PROJECT, location=self.settings.GOOGLE_CLOUD_LOCATION)
        self.app = agent_engines.get(self.settings.agent_engine_name)

    async def get_session(self, user_id: str, session_id: str) -> Session | None:
        session = await self.app.async_get_session(user_id=user_id, session_id=session_id)
        return Session.model_validate(session)

    async def list_sessions(self, user_id: str) -> list[Session]:
        sessions = await self.app.async_list_sessions(user_id=user_id)
        return [Session.model_validate(**s) for s in sessions]

    async def load_artifact(self, user_id: str, session_id: str, artifact_id: str):
        return await self.app.load_artifact(user_id=user_id, session_id=session_id, artifact_id=artifact_id)

    async def create_session(self, user_id: str, session_id: str | None = None, state: dict[str, Any] | None = None) -> Session:
        session = await self.app.create_session(user_id=user_id, session_id=session_id, state=state)
        return Session.model_validate(session)

    async def delete_session(self, user_id: str, session_id: str) -> None:
        await self.app.async_delete_session(user_id=user_id, session_id=session_id)

    def stream_query(self, message: str | dict[str, Any], user_id: str, session_id: str | None = None, **kwargs) -> Generator[dict[str, Any], None, None]:
        for event in self.app.stream_query_sse(message=message, user_id=user_id, session_id=session_id, **kwargs):
            yield event

    async def async_stream_query(self, message: str | dict[str, Any], user_id: str, session_id: str | None = None, **kwargs) -> AsyncIterable[dict[str, Any]]:
        async for event in self.app.async_stream_query_sse(message=message, user_id=user_id, session_id=session_id):
            yield event


class RemoteChatAPI(ChatAPI):
    app_name: str = "radio_station"

    def __init__(self, app_name="radio_station"):
        self.app_name = app_name
        super().__init__()

    async def get_session(self, user_id: str, session_id: str) -> Session | None:
        async with httpx.AsyncClient(auth=GoogleJWTAuth(settings=self.settings), timeout=600) as client:
            res = await client.get(f"{self.settings.backend_url}/apps/{self.app_name}/users/{user_id}/sessions/{session_id}")
            if res.status_code != 200:
                return None
            else:
                return Session.model_validate(res.json())

    async def delete_session(self, user_id: str, session_id: str) -> None:
        async with httpx.AsyncClient(auth=GoogleJWTAuth(settings=self.settings), timeout=600) as client:
            res = await client.delete(f"{self.settings.backend_url}/apps/{self.app_name}/users/{user_id}/sessions/{session_id}")
            res.raise_for_status()

    async def list_sessions(self, user_id: str) -> list[Session]:
        async with httpx.AsyncClient(auth=GoogleJWTAuth(settings=self.settings), timeout=600) as client:
            res = await client.get(f"{self.settings.backend_url}/apps/{self.app_name}/users/{user_id}/sessions")
            return [Session.model_validate(j) for j in res.json()]

    async def create_session(self, user_id: str, state: dict[str, Any] | None = None) -> Session:
        async with httpx.AsyncClient(auth=GoogleJWTAuth(settings=self.settings), timeout=600) as client:
            res = await client.post(f"{self.settings.backend_url}/apps/{self.app_name}/users/{user_id}/sessions", json={"state": state})
            return Session.model_validate(res.json())

    async def load_artifact(self, user_id: str, session_id: str, artifact_id: str):
        async with httpx.AsyncClient(auth=GoogleJWTAuth(settings=self.settings), timeout=600) as client:
            res = await client.get(f"{self.settings.backend_url}/apps/{self.app_name}/users/{user_id}/sessions/{session_id}/artifacts/{artifact_id}")
            if "detail" in res.json() and res.json()["detail"] == "Artifact not found":
                return None
            return types.Part.model_validate(res.json())

    def stream_query(self, message: str | dict[str, Any], user_id: str, session_id: str | None = None, streaming=False, **kwargs) -> Generator[dict[str, Any], None, None]:
        with httpx.Client(auth=GoogleJWTAuth(settings=self.settings), timeout=None) as client:
            new_message = types.UserContent(parts=[types.Part(text=message)])

            with connect_sse(
                client,
                "POST",
                f"{self.settings.backend_url}/run_sse",
                json={
                    "app_name": self.app_name,
                    "user_id": user_id,
                    "session_id": session_id,
                    "new_message": new_message.to_json_dict(),
                    "streaming": streaming,
                },
                headers={
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                },
            ) as event_source:
                for sse in event_source.iter_sse():
                    yield from_json(sse.data)

    async def async_stream_query(self, message: str | dict[str, Any], user_id: str, session_id: str | None = None, streaming=False, **kwargs) -> AsyncIterable[dict[str, Any]]:
        new_message = types.UserContent(parts=[types.Part(text=message)])

        async with httpx.AsyncClient(auth=GoogleJWTAuth(settings=self.settings), timeout=None) as client:
            async with aconnect_sse(
                client,
                "POST",
                f"{self.settings.backend_url}/run_sse",
                json={"app_name": self.app_name, "user_id": user_id, "session_id": session_id, "new_message": new_message.to_json_dict(), "streaming": streaming},
                headers={
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                },
            ) as event_source:
                async for sse in event_source.aiter_sse():
                    yield from_json(sse.data)


def get_chat_api(settings: Settings = Depends(get_settings)) -> ChatAPI:
    if settings.BACKEND_TYPE == "remote":
        return RemoteChatAPI()
    elif settings.BACKEND_TYPE == "agentengine":
        return VertexAIChatAPI()
    else:
        raise ValueError(f"Unknown backend type: {settings.BACKEND_TYPE}")
