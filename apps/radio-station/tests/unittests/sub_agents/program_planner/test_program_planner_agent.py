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

import pytest
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from radio_station.constants import THINKING_MODEL
from radio_station.model.program_plan import ProgramPlan
from radio_station.state_keys import GlobalState, ResearcherState
from radio_station.sub_agents.program_planner.program_planner_agent import ProgramPlannerAgent, before_model_callback


class TestProgramPlannerAgent:
    """ProgramPlannerAgentクラスのユニットテスト"""

    def test_init(self):
        """初期化のテスト"""
        # 実行
        agent = ProgramPlannerAgent()

        # 検証
        assert agent.name == "ProgramPlannerAgent"
        assert agent.model == THINKING_MODEL
        assert agent.output_schema == ProgramPlan
        assert agent.output_key == "program:structure"
        assert agent.before_model_callback == before_model_callback

    def test_before_model_callback(self, mock_callback_context, mock_llm_request, listener_program, research_results):
        """before_model_callbackのテスト"""

        mock_context = mock_callback_context

        # モックの設定
        mock_context.state["user:listener_program"] = listener_program.model_dump()
        mock_context.state["research:results"] = research_results

        # 実行
        result = before_model_callback(mock_context, mock_llm_request)

        # 検証
        assert result is None  # コールバックはNoneを返す
        mock_llm_request.append_instructions.assert_called_once()

        # 呼び出し引数を取得
        args, _ = mock_llm_request.append_instructions.call_args
        instructions = args[0][0]

        # 指示にリスナープログラムと研究結果が含まれていることを確認
        assert "[Program]" in instructions
        assert "[Segments]" in instructions

    def test_before_model_callback_empty_state(self, mock_context, mock_llm_request):
        """空のステートでのbefore_model_callbackのテスト"""
        # モックの設定（空のステート）
        mock_context.state = {}

        # 実行
        result = before_model_callback(mock_context, mock_llm_request)

        # 検証
        assert result is None  # コールバックはNoneを返す
        mock_llm_request.append_instructions.assert_called_once()

        # 呼び出し引数を取得
        args, _ = mock_llm_request.append_instructions.call_args
        instructions = args[0][0]

        # 指示にリスナープログラムと研究結果が含まれていることを確認（nullの場合）
        assert "[Program]" in instructions
        assert "null" in instructions
        assert "[Segments]" in instructions
        assert "null" in instructions

    @pytest.mark.asyncio
    async def test_real(self, listener_program, research_results):
        session_service = InMemorySessionService()
        runner = Runner(
            app_name="test",
            agent=ProgramPlannerAgent(),
            session_service=session_service,
        )
        session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                GlobalState.LISTENER_PROGRAM: listener_program.model_dump(),
                ResearcherState.RESULTS: research_results,
            },
        )

        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            print("------------------")
            print(event.model_dump())
            print("------------------")
        session = runner.session_service.get_session(app_name="test", user_id="test", session_id="test")
        assert session.state.get("program:structure") is not None
        print(ProgramPlan(**session.state.get("program:structure")).to_llm_text())
