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

import itertools
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from google.adk import Runner
from google.adk.agents import ParallelAgent
from google.adk.artifacts import InMemoryArtifactService
from google.adk.events import Event
from google.adk.sessions import InMemorySessionService, State
from google.genai import types

from radio_station.model.talk_script import TalkScriptSegment
from radio_station.state_keys import GlobalState, WriterState
from radio_station.sub_agents.recoder.flow_agent import RecordingFlowAgent
from radio_station.sub_agents.recoder.recorder_agent import RecorderAgent
from radio_station.sub_agents.mastering.synthesis_agent import RecordingSynthesisAgent


class TestRecordingFlowAgent:
    """RecordingFlowAgentクラスのユニットテスト"""

    @pytest.mark.asyncio
    async def test_run_async_impl(self, mock_context, radio_casts, talk_scripts_dicts):
        """基本的な動作のテスト"""
        # モックの設定
        mock_context.session.state["radio_casts"] = [rc.model_dump() for rc in radio_casts]
        mock_context.session.state["writer:talk_script_segments"] = talk_scripts_dicts

        # ParallelAgentのrun_asyncをモック
        mock_parallel_event = Event(
            author="ParallelRecodingAgent",
            content=types.Content(role="ParallelRecodingAgent", parts=[types.Part(text="Parallel event")]),
        )
        mock_synthesis_event = Event(
            author="RecordingSynthesisAgent",
            content=types.Content(role="RecordingSynthesisAgent", parts=[types.Part(text="Synthesis event")]),
        )

        with patch(
            "radio_station.sub_agents.recoder.flow_agent.ParallelAgent", autospec=True
        ) as MockParallelAgent, patch(
            "radio_station.sub_agents.recoder.flow_agent.RecordingSynthesisAgent", autospec=True
        ) as MockSynthesisAgent:
            # ParallelAgentのモック
            mock_parallel_agent = MagicMock(spec=ParallelAgent)
            MockParallelAgent.return_value = mock_parallel_agent
            mock_parallel_agent.run_async.return_value = AsyncMock(return_value=[mock_parallel_event])

            # RecordingSynthesisAgentのモック
            mock_synthesis_agent = MagicMock(spec=RecordingSynthesisAgent)
            MockSynthesisAgent.return_value = mock_synthesis_agent
            mock_synthesis_agent.run_async.return_value = AsyncMock(return_value=[mock_synthesis_event])

            # 実行
            agent = RecordingFlowAgent()
            events = []
            async for event in agent._run_async_impl(mock_context):
                events.append(event)

            # # 検証
            # assert len(events) == 2
            # assert events[0] == mock_parallel_event
            # assert events[1] == mock_synthesis_event

            talk_scripts = list(itertools.chain.from_iterable([TalkScriptSegment(**tsd).scripts for tsd in talk_scripts_dicts]))

            # ParallelAgentの呼び出しを検証
            MockParallelAgent.assert_called_once()
            _, kwargs = MockParallelAgent.call_args
            assert kwargs["name"] == "ParallelRecodingAgent"
            assert len(kwargs["sub_agents"]) == len(talk_scripts)
            assert all(isinstance(a, RecorderAgent) for a in kwargs["sub_agents"])

            # RecordingSynthesisAgentの呼び出しを検証
            MockSynthesisAgent.assert_called_once()

            task_ids = mock_context.session.state[f"{State.TEMP_PREFIX}recorder:task_ids"]
            assert len(task_ids) == len(talk_scripts)

    @pytest.mark.asyncio
    async def test_real(self, talk_scripts_dicts, radio_casts):
        """実際のエージェント実行テスト"""
        # セッションサービスとランナーの設定
        session_service = InMemorySessionService()
        artifact_service = InMemoryArtifactService()
        runner = Runner(
            app_name="test",
            agent=RecordingFlowAgent(),
            session_service=session_service,
            artifact_service=artifact_service
        )

        # セッションの作成と状態の設定
        session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                GlobalState.RADIO_CASTS: [rc.model_dump() for rc in radio_casts],
                WriterState.TALK_SCRIPT_SEGMENTS: talk_scripts_dicts
            },
        )

        # エージェントの実行
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            print("------------------")
            print(event.model_dump())
            print("------------------")

        mp3file = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename="audio.mp3")

        with open("test_audio.mp3", "wb") as f:
            f.write(mp3file.inline_data.data)

