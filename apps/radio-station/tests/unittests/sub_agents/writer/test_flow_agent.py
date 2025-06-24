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
from google.adk.events import Event
from google.adk.sessions import InMemorySessionService
from google.genai import types

from radio_station.model.talk_script import TalkScript, TalkScriptSegment
from radio_station.state_keys import GlobalState, ProgramPlannerState, ResearcherState
from radio_station.sub_agents.writer.flow_agent import ProgramSegmentWriterFlowAgent
from radio_station.sub_agents.writer.program_segment_writer_agent import ProgramSegmentWriterAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler(sys.stdout))

class TestProgramSegmentWriterFlowAgent:
    """ProgramSegmentWriterFlowAgentクラスのユニットテスト"""

    @pytest.mark.asyncio
    async def test_run_async_impl(self, mock_context, program_plan, research_results):
        """基本的な動作のテスト"""
        # モックの設定
        mock_context.session.state["program:structure"] = program_plan.model_dump()
        mock_context.session.state["research:results"] = research_results

        # ProgramSegmentWriterAgentのrun_asyncをモック
        mock_event = Event(author="ProgramSegmentWriterAgent_1", content=types.Content(role="ProgramSegmentWriterAgent_1", parts=[types.Part(text="Test event")]))

        with patch("radio_station.sub_agents.writer.flow_agent.ProgramSegmentWriterAgent") as MockProgramSegmentWriterAgent:
            mock_agent = MagicMock(spec=ProgramSegmentWriterAgent)
            MockProgramSegmentWriterAgent.return_value = mock_agent
            mock_agent.run_async.return_value = AsyncMock(return_value=[mock_event])
            mock_agent.name = "ProgramSegmentWriterAgent_1"

            # 実行
            agent = ProgramSegmentWriterFlowAgent(name="TestFlowAgent")
            events = [event async for event in agent._run_async_impl(mock_context)]

            # 検証
            assert len(events) == 1
            assert events[0].author == "TestFlowAgent"
            # 他のアサーション...
            MockProgramSegmentWriterAgent.assert_called()
            assert mock_context.session.state["temp:writer:1:segment"] == program_plan.segments[0].model_dump()
            assert mock_context.session.state["temp:writer:2:segment"] == program_plan.segments[1].model_dump()
            assert mock_context.session.state["temp:writer:1:next_segment"] == program_plan.segments[1].model_dump()
            assert mock_context.session.state["temp:writer:2:next_segment"] == {
                'description': '技術系ブログZennのトレンドフィードから最近の技術トレンドを説明するコーナー',
                'is_music': False,
                'program_segment_ids': [2],
                'segment_seconds': 480.0,
                'title': 'Zennのトレンド'
            }

    @pytest.mark.asyncio
    async def test_run_async_impl_no_program_plan(self, mock_context):
        """番組計画がない場合のテスト"""
        # 実行と検証
        agent = ProgramSegmentWriterFlowAgent(name="TestFlowAgent")
        with pytest.raises(ValueError, match="Program plan not found in state."):
            [event async for event in agent._run_async_impl(mock_context)]

    @pytest.mark.asyncio
    async def test_run_async_impl_with_talk_scripts(self, mock_context, program_plan):
        """ProgramSegmentWriterAgentが台本を返す場合のテスト"""
        # モックの設定
        mock_context.session.state["program:structure"] = program_plan.model_dump()

        # ProgramSegmentWriterAgentのrun_asyncをモック
        mock_event = Event(author="ProgramSegmentWriterAgent_1", content=types.Content(role="ProgramSegmentWriterAgent_1", parts=[types.Part(text="Test event")]))
        mock_talk_scripts = TalkScriptSegment(scripts=[TalkScript(radio_cast_id=1, content="aaa")])

        with patch("radio_station.sub_agents.writer.flow_agent.ProgramSegmentWriterAgent") as MockProgramSegmentWriterAgent:
            mock_agent = MagicMock(spec=ProgramSegmentWriterAgent)
            MockProgramSegmentWriterAgent.return_value = mock_agent
            mock_agent.run_async.return_value = AsyncMock(return_value=[mock_event])
            mock_agent.name = "ProgramSegmentWriterAgent_1"
            mock_context.session.state["writer:1:talk_script_segment"] = mock_talk_scripts.model_dump()

            # 実行
            agent = ProgramSegmentWriterFlowAgent(name="TestFlowAgent")
            events = [event async for event in agent._run_async_impl(mock_context)]

            # 検証
            assert len(events) == 1
            assert events[0].author == "TestFlowAgent"
            assert len(events[0].content.parts) == 1
            assert "[[Talk Script]]" in events[0].content.parts[0].text

    @pytest.mark.asyncio
    async def test_real(self, program_plan, research_results, listener_program, listener_program_segments, radio_casts):

        listener_program.base_radio_casts = [radio_casts[0]]

        session_service = InMemorySessionService()
        runner = Runner(
            app_name="test",
            agent=ProgramSegmentWriterFlowAgent(name="ResearchFlowAgent"),
            session_service=session_service,
        )
        session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                GlobalState.RADIO_CASTS: [radio_casts[0].model_dump()],
                ProgramPlannerState.PROGRAM_STRUCTURE: program_plan.model_dump(),
                ResearcherState.RESULTS: research_results,
                GlobalState.LISTENER_PROGRAM: listener_program.model_dump(),
                GlobalState.LISTENER_PROGRAM_SEGMENTS: [lps.model_dump() for lps in listener_program_segments],
            },
        )

        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            logger.info("------------------")
            logger.info(event.model_dump())
            logger.info("------------------")

        session = runner.session_service.get_session(app_name="test", user_id="test", session_id="test")

        talk_script_segment_dicts = session.state.get("writer:talk_script_segments")
        for talk_script_segment in [TalkScriptSegment(**tssd) for tssd in talk_script_segment_dicts]:
            logger.info("============= New Segment =============")
            for talk_script in talk_script_segment.scripts:
                logger.info(f"{talk_script.radio_cast_id}: {talk_script.content}")
            logger.info(f"continue_segment: {talk_script_segment.continue_segment}")
            logger.info(f"hand over: {talk_script_segment.hand_over}")

        # logger.info(session.state.get('writer:talk_script_segments'))
