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
import sys
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from google.adk import Runner
from google.adk.agents import SequentialAgent
from google.adk.artifacts import InMemoryArtifactService
from google.adk.events import Event
from google.adk.sessions import InMemorySessionService
from google.genai import types

from radio_station.model.talk_script import TalkScriptSegment
from radio_station.state_keys import GlobalState, ProgramPlannerState, WriterState
from radio_station.sub_agents.generate_radio_flow_agent import GenerateRadioFlowAgent
from radio_station.utils.agent_helpers import get_auth_config, get_auth_request_function_call

file_handler = logging.FileHandler("test.log")
file_handler.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.INFO, handlers=[file_handler, logging.StreamHandler(sys.stdout)], format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class TestGenerateRadioFlowAgent:
    """GenerateRadioFlowAgentクラスのユニットテスト"""

    @pytest.mark.asyncio
    async def test_run_async_impl(self, mock_context, radio_casts, listener_program, listener_program_segments):
        """基本的な動作のテスト"""
        # モックの設定
        mock_context.session.state[GlobalState.RADIO_CASTS] = [rc.model_dump() for rc in radio_casts]
        mock_context.session.state[GlobalState.LISTENER_PROGRAM] = listener_program.model_dump()
        mock_context.session.state[GlobalState.LISTENER_PROGRAM_SEGMENTS] = [lps.model_dump() for lps in listener_program_segments]

        # SequentialAgentのrun_asyncをモック
        mock_event = Event(author="GenerateRadioFlowSequentialAgent", content=types.Content(role="GenerateRadioFlowSequentialAgent", parts=[types.Part(text="Flow completed")]))

        with patch("radio_station.sub_agents.generate_radio_flow_agent.SequentialAgent") as MockSequentialAgent:
            mock_agent = MagicMock(spec=SequentialAgent)
            MockSequentialAgent.return_value = mock_agent
            mock_agent.run_async.return_value = AsyncMock(return_value=[mock_event])

            # 実行
            agent = GenerateRadioFlowAgent()
            [event async for event in agent._run_async_impl(mock_context)]

            # 検証
            MockSequentialAgent.assert_called_once()

    @pytest.mark.asyncio
    async def test_validate_state_success(self, mock_context, radio_casts, listener_program, listener_program_segments):
        """validate_stateが成功する場合のテスト"""
        mock_context.session.state[GlobalState.RADIO_CASTS] = [rc.model_dump() for rc in radio_casts]
        mock_context.session.state[GlobalState.LISTENER_PROGRAM] = listener_program.model_dump()
        mock_context.session.state[GlobalState.LISTENER_PROGRAM_SEGMENTS] = [lps.model_dump() for lps in listener_program_segments]

        agent = GenerateRadioFlowAgent()
        assert agent.validate_state(mock_context.session.state)

    @pytest.mark.asyncio
    async def test_validate_state_missing_radio_casts(self, mock_context, listener_program, listener_program_segments):
        """validate_stateでradio_castsがない場合のテスト"""
        mock_context.session.state[GlobalState.LISTENER_PROGRAM] = listener_program.model_dump()
        mock_context.session.state[GlobalState.LISTENER_PROGRAM_SEGMENTS] = [lps.model_dump() for lps in listener_program_segments]

        agent = GenerateRadioFlowAgent()
        with pytest.raises(ValueError, match="Radio casts not found in state"):
            agent.validate_state(mock_context.session.state)

    @pytest.mark.asyncio
    async def test_validate_state_missing_listener_program(self, mock_context, radio_casts, listener_program_segments):
        """validate_stateでlistener_programがない場合のテスト"""
        mock_context.session.state[GlobalState.RADIO_CASTS] = [rc.model_dump() for rc in radio_casts]
        mock_context.session.state[GlobalState.LISTENER_PROGRAM_SEGMENTS] = [lps.model_dump() for lps in listener_program_segments]

        agent = GenerateRadioFlowAgent()
        with pytest.raises(ValueError, match="Listener program not found in state"):
            agent.validate_state(mock_context.session.state)

    @pytest.mark.asyncio
    async def test_validate_state_missing_listener_program_segments(self, mock_context, radio_casts, listener_program):
        """validate_stateでlistener_program_segmentsがない場合のテスト"""
        mock_context.session.state[GlobalState.RADIO_CASTS] = [rc.model_dump() for rc in radio_casts]
        mock_context.session.state[GlobalState.LISTENER_PROGRAM] = listener_program.model_dump()

        agent = GenerateRadioFlowAgent()
        with pytest.raises(ValueError, match="Listener program segments not found in state"):
            agent.validate_state(mock_context.session.state)

    @pytest.mark.asyncio
    async def test_real(self, radio_casts, listener_program, listener_program_segments):
        """実際の動作のテスト"""

        session_service = InMemorySessionService()
        artifact_service = InMemoryArtifactService()

        session = await session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                GlobalState.RADIO_CASTS: [r.model_dump() for r in radio_casts],
                GlobalState.LISTENER_PROGRAM: listener_program.model_dump(),
                GlobalState.LISTENER_PROGRAM_SEGMENTS: [lps.model_dump() for lps in listener_program_segments],
            },
        )
        #
        # auth_runner = Runner(app_name=session.app_name, agent=GmailResearchAgent(task_id="1"), session_service=session_service, artifact_service=artifact_service)
        #
        # auth_request_function_call = None
        # async for event in auth_runner.run_async(user_id=session.user_id, session_id=session.id, new_message=types.Content(parts=[types.Part(text="")])):
        #     if auth_request_function_call := get_auth_request_function_call(event):
        #         break
        #
        # auth_request_function_call = await self.auth_flow(auth_request_function_call, auth_runner, session)
        #
        # while auth_request_function_call:
        #     auth_request_function_call = await self.auth_flow(auth_request_function_call, auth_runner,session)
        #

        runner = Runner(app_name="test", agent=GenerateRadioFlowAgent(), session_service=session_service, artifact_service=artifact_service)
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            pass

        session = await session_service.get_session(app_name="test", user_id="test", session_id="test")
        logger.info(f"Program Plan: {session.state.get(ProgramPlannerState.PROGRAM_STRUCTURE)}")

        keys = await artifact_service.list_artifact_keys(app_name="test", user_id="test", session_id="test")

        talk_script_segment_dicts = session.state.get(WriterState.TALK_SCRIPT_SEGMENTS)

        talk_script_segments = [TalkScriptSegment(**tssd) for tssd in talk_script_segment_dicts]
        for tss in talk_script_segments:
            logger.info(tss.to_talk_script_text(radio_casts=radio_casts))
        for artifact_key in keys:
            mp3file = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename=artifact_key)
            with open(artifact_key, "wb") as f:
                f.write(mp3file.inline_data.data)
        mp3file = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename="audio.mp3")

        with open("test_audio.mp3", "wb") as f:
            f.write(mp3file.inline_data.data)

    async def auth_flow(self, auth_request_function_call, auth_runner, session):
        if not auth_request_function_call:
            return None

        logger.info("--> Authentication required by agent.")
        # Store the ID needed to respond later
        if not (auth_request_function_call_id := auth_request_function_call.id):
            raise ValueError(f"Cannot get function call id from function call: {auth_request_function_call}")
        # Get the AuthConfig containing the auth_uri etc.
        auth_config = get_auth_config(auth_request_function_call)

        base_auth_uri = auth_config.exchanged_auth_credential.oauth2.auth_uri
        redirect_uri = "http://localhost:8080/dev-ui"
        auth_request_uri = f"{base_auth_uri}&redirect_uri={redirect_uri}"
        logger.info(f"Access URL: {auth_request_uri}")
        auth_response_uri = input("Input uri:")
        auth_response_uri = auth_response_uri.strip()

        if not auth_response_uri:
            logger.info("Callback URL not provided. Aborting.")
            raise ValueError(f"Cannot get function call id from function call: {auth_request_function_call}")

        print("state", auth_config.exchanged_auth_credential.oauth2.state)
        print("auth_response_uri", auth_response_uri)

        # Update the received AuthConfig with the callback details
        auth_config.exchanged_auth_credential.oauth2.auth_response_uri = auth_response_uri
        # Also include the redirect_uri used, as the token exchange might need it
        auth_config.exchanged_auth_credential.oauth2.redirect_uri = redirect_uri

        auth_content = types.Content(
            role="user",  # Role can be 'user' when sending a FunctionResponse
            parts=[
                types.Part(
                    function_response=types.FunctionResponse(
                        id=auth_request_function_call_id,  # Link to the original request
                        name="adk_request_credential",  # Special framework function name
                        response=auth_config.model_dump(),  # Send back the *updated* AuthConfig
                    )
                )
            ],
        )

        # --- Resume Execution ---
        print("\nSubmitting authentication details back to the agent...")
        auth_request_function_call = None

        auth_runner.run_async(session_id=session.id, user_id=session.user_id, new_message=auth_content)

        event = await auth_runner.run_async(session_id=session.id, user_id=session.user_id, new_message=auth_content).__anext__()
        print(event)
        session = await auth_runner.session_service.get_session(app_name=session.app_name, user_id=session.user_id, session_id=session.id)
        logger.info(f"Current State: {session.state}")

        async for event in auth_runner.run_async(
            session_id=session.id,
            user_id=session.user_id,
            new_message=types.Content(parts=[types.Part(text="")]),
        ):
            session = await auth_runner.session_service.get_session(app_name=session.app_name, user_id=session.user_id, session_id=session.id)
            logger.info(f"Current State: {session.state}")

            if auth_request_function_call := get_auth_request_function_call(event):
                break

            logger.info(event)
        return auth_request_function_call

    @pytest.mark.asyncio
    async def test_real2(self, radio_casts2, listener_program2, listener_program_segments2):
        """実際の動作のテスト"""
        listener_program2.base_radio_casts = radio_casts2

        session_service = InMemorySessionService()
        artifact_service = InMemoryArtifactService()
        runner = Runner(app_name="test", agent=GenerateRadioFlowAgent(), session_service=session_service, artifact_service=artifact_service)
        session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                GlobalState.RADIO_CASTS: [r.model_dump() for r in radio_casts2],
                GlobalState.LISTENER_PROGRAM: listener_program2.model_dump(),
                GlobalState.LISTENER_PROGRAM_SEGMENTS: [lps.model_dump() for lps in listener_program_segments2],
            },
        )

        show_plan = False
        show_talk_script = False
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            # if "LLMSpeakerAgent" in event.author:
            #     logger.info(event.content)
            # session = session_service.get_session(app_name="test", user_id="test", session_id="test")
            # if not show_plan and ProgramPlannerState.PROGRAM_STRUCTURE in session.state:
            #     show_plan = True
            #     program_plan = ProgramPlan(**session.state.get(ProgramPlannerState.PROGRAM_STRUCTURE))
            #     logger.info("Program Structure:")
            #     logger.info(f"{program_plan.to_llm_text(include_segments=True)}")
            #
            # if not show_talk_script and WriterState.TALK_SCRIPT_SEGMENTS in session.state and event.content and event.content.parts and "[[Talk Script]]" in event.content.parts[-1].text:
            #     show_talk_script = True
            #     segment_dicts = session.state.get(WriterState.TALK_SCRIPT_SEGMENTS)
            #     talk_scripts: list[TalkScript] = list(itertools.chain.from_iterable([TalkScriptSegment(**tsd).scripts for tsd in segment_dicts]))
            #     radio_casts = session.state.get(GlobalState.RADIO_CASTS)
            #     m = {}
            #     logger.info("Talk Script:")
            #     for rc in radio_casts:
            #         m[rc["id"]] = rc["name"]
            #
            #     for ts in talk_scripts:
            #         logger.info(f"  {m[ts.radio_cast_id]}({ts.speaking_rate}): {ts.content}")
            pass

        session = session_service.get_session(app_name="test", user_id="test", session_id="test")
        logger.info(f"Program Plan: {session.state.get(ProgramPlannerState.PROGRAM_STRUCTURE)}")

        keys = await artifact_service.list_artifact_keys(app_name="test", user_id="test", session_id="test")

        talk_script_segment_dicts = session.state.get(WriterState.TALK_SCRIPT_SEGMENTS)

        talk_script_segments = [TalkScriptSegment(**tssd) for tssd in talk_script_segment_dicts]
        for tss in talk_script_segments:
            logger.info(tss.to_talk_script_text(radio_casts=radio_casts2))
        for artifact_key in keys:
            mp3file = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename=artifact_key)
            with open(artifact_key, "wb") as f:
                f.write(mp3file.inline_data.data)
        mp3file = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename="audio.mp3")

        with open("test_audio.mp3", "wb") as f:
            f.write(mp3file.inline_data.data)
