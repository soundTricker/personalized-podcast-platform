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

import datetime
from unittest.mock import MagicMock, patch

import pytest
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.run_config import RunConfig
from google.adk.auth.auth_credential import ServiceAccount
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.openapi_tool.auth.auth_helpers import service_account_scheme_credential
from google.genai import types

from radio_station.model.listener_program_segment import ListenerProgramCalendarSegment
from radio_station.state_keys import ResearcherState
from radio_station.sub_agents.researcher.calendar_researcher_agent import CalendarResearchAgent, CalendarResearchFlowAgent
from radio_station.utils.agent_helpers import get_auth_config, get_auth_request_function_call


class TestCalendarResearchAgent:
    """CalendarResearchAgentクラスのユニットテスト"""

    def test_init(self):
        """初期化のテスト"""
        # 実行
        agent = CalendarResearchAgent(task_id="test")

        # 検証
        assert agent.name == "CalendarResearchAgent_test"
        assert agent.model == "gemini-2.0-flash"
        assert agent.output_key == "research:test:research_result"
        assert "summary" in agent.instruction
        assert "JSON" in agent.instruction
        assert "Output Format" in agent.instruction
        assert "Output Schema" in agent.instruction

    @pytest.mark.asyncio
    async def test_make_calendar_info(self):
        """make_calendar_infoメソッドのテスト"""
        # 準備
        task_id = "test_task"
        agent = CalendarResearchAgent(task_id=task_id)
        callback_context = MagicMock(spec=CallbackContext)
        task_info_dict = {
            "start_offset_days": 1,
            "end_offset_days": 7,
            "calendar_id": "test@example.com",
        }
        callback_context.state.get.return_value = task_info_dict
        with patch("radio_station.sub_agents.researcher.calendar_researcher_agent.get_current_time") as mock_get_current_time:
            mock_get_current_time.return_value = datetime.datetime(2024, 1, 1, 0, 0, 0).isoformat()

            # 実行
            result = agent.make_calendar_info(callback_context)

            # 検証
            assert result is None
            callback_context.state.get.assert_called_once_with(ResearcherState.task_info(task_id))
            assert callback_context.state[ResearcherState.task_calendar_info(task_id)] == {
                "calendar_id": "test@example.com",
                "time_min": datetime.datetime(2024, 1, 2, 0, 0, 0).isoformat(),
                "time_max": datetime.datetime(2024, 1, 8, 0, 0, 0).isoformat(),
            }

    @pytest.mark.asyncio
    async def test_real(self):
        """統合テスト"""
        # 準備
        session_service = InMemorySessionService()
        task_id = "test_task"
        task_info = ListenerProgramCalendarSegment(
            id=1,
            listener_id=1,
            listener_program_id=1,
            title="Test Calendar",
            description="Test Calendar Description",
            start_offset_days=0,
            end_offset_days=6,
            calendar_id="keisuke.oohashi@gmail.com",
        )
        agent = CalendarResearchFlowAgent(task_id=task_id, task=task_info)

        await session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={ResearcherState.task_info(task_id): task_info.model_dump()},
        )
        runner = Runner(
            app_name="test",
            agent=agent,
            session_service=session_service,
        )

        # 実行
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="今日の予定を教えて")]), run_config=RunConfig()):
            print("------------------")
            print(event.model_dump())
            print("------------------")

        session = await session_service.get_session(
            app_name="test",
            user_id="test",
            session_id="test"
        )

        print(session.state.get(ResearcherState.research_result(task_id)))


    @pytest.mark.asyncio
    async def test_real_oauth(self):
        """統合テスト"""
        # 準備
        session_service = InMemorySessionService()
        task_id = "test_task"
        agent = CalendarResearchAgent(task_id=task_id)
        runner = Runner(
            app_name="test",
            agent=agent,
            session_service=session_service,
        )
        task_info = ListenerProgramCalendarSegment(
            id=1,
            listener_id=1,
            listener_program_id=1,
            title="Test Calendar",
            description="Test Calendar Description",
            start_offset_days=0,
            end_offset_days=1,
            calendar_id="test@example.com",
        )
        session = session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={ResearcherState.task_info(task_id): task_info.model_dump()},
        )

        # 実行

        auth_request_function_call_id, auth_config = None, None

        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="今日の予定を教えて")]), run_config=RunConfig()):
            print("------------------")
            print(event.model_dump())
            print("------------------")

            if auth_request_function_call := get_auth_request_function_call(event):
                auth_config = get_auth_config(auth_request_function_call)
                print(auth_config)

        if auth_request_function_call_id and auth_config:
            base_auth_uri = auth_config.exchanged_auth_credential.oauth2.auth_uri

            if base_auth_uri:
                redirect_uri = "http://localhost:8000/callback"  # MUST match your OAuth client app config
                # Append redirect_uri (use urlencode in production)
                auth_request_uri = base_auth_uri + f"&redirect_uri={redirect_uri}"
                # Now you need to redirect your end user to this auth_request_uri or ask them to open this auth_request_uri in their browser
                # This auth_request_uri should be served by the corresponding auth provider and the end user should login and authorize your applicaiton to access their data
                # And then the auth provider will redirect the end user to the redirect_uri you provided
                # Next step: Get this callback URL from the user (or your web server handler)
            else:
                print("ERROR: Auth URI not found in auth_config.")
                # Handle error


