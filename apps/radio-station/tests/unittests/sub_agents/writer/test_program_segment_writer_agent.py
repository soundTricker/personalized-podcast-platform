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

"""
ProgramSegmentWriterAgentのユニットテスト
"""

import json

import pytest
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from radio_station.constants import GENERIC_MODEL
from radio_station.model.listener_program import ListenerProgram
from radio_station.model.program_plan import SegmentPlan
from radio_station.model.radio_cast import RadioCast, RadioCastRole
from radio_station.sub_agents.writer.program_segment_writer_agent import ProgramSegmentWriterAgent, before_model_callback


class TestProgramSegmentWriterAgent:
    """ProgramSegmentWriterAgentのテストクラス"""

    @pytest.fixture
    def segment_plan(self):
        """テスト用のSegmentPlanを作成"""
        return SegmentPlan(
            title="テストセグメント",
            program_segment_ids=[1, 2],
            segment_seconds=300,
            is_music=False,
            description="テストセグメントの説明"
        )

    @pytest.fixture
    def listener_program(self):
        """テスト用のListenerProgramを作成"""
        return ListenerProgram(
            id=1,
            listener_id=1,
            title="テストプログラム",
            description="テストプログラムの説明",
            program_minutes=30,
            insert_music=True,
            base_radio_casts=[
                RadioCast(
                    id=1,
                    name="司会田太郎",
                    role=RadioCastRole.RadioPersonality,
                    personality="とにかく明るく元気",
                    voice_name="ja-JP-Chirp3-HD-Achird",
                ),
                RadioCast(
                    id=2,
                    name="助次郎",
                    role=RadioCastRole.Assistant,
                    personality="冷静沈着",
                    voice_name="ja-JP-Chirp3-HD-Algenib",
                ),
                RadioCast(id=3, name="ゲースト三郎", role=RadioCastRole.Guest, personality="静かな専門家",voice_name="ja-JP-Chirp3-HD-Algieba",),
            ],
        )

    def test_init(self):
        """初期化のテスト"""
        # 実行
        agent = ProgramSegmentWriterAgent(task_id="test_task_id")

        # 検証
        assert agent.name == "ProgramSegmentWriterAgent_test_task_id"
        assert agent.model == GENERIC_MODEL
        assert agent.task_id == "test_task_id"

    def test_before_model_callback(self, mock_callback_context, mock_llm_request, segment_plan, listener_program):
        """before_model_callbackのテスト"""
        mock_context = mock_callback_context
        # モックの設定
        mock_context.agent_name = "ProgramSegmentWriterAgent_test_task_id"
        mock_context.state["temp:writer:test_task_id:segment"] = segment_plan.model_dump()
        mock_context.state["user:listener_program"] = listener_program.model_dump()

        # 実行
        result = before_model_callback(mock_context, mock_llm_request)

        # 検証
        assert result is None  # コールバックはNoneを返す
        mock_llm_request.append_instructions.assert_called_once()

        # 呼び出し引数を取得
        args, _ = mock_llm_request.append_instructions.call_args
        instructions = args[0][0]

        # 指示にセグメント情報とラジオキャスト情報が含まれていることを確認
        assert "[Segment Plan]" in instructions
        assert json.dumps(segment_plan.model_dump(), ensure_ascii=False) in instructions
        assert "[Radio Casts]" in instructions
        assert json.dumps([cast.model_dump() for cast in listener_program.base_radio_casts], ensure_ascii=False) in instructions

    def test_before_model_callback_missing_segment_plan(self, mock_callback_context, mock_llm_request):
        """セグメント情報が欠けている場合のbefore_model_callbackのテスト"""
        # モックの設定（セグメント情報なし）
        mock_callback_context.state = {}
        mock_callback_context.agent_name = "hoge_test_task_id"

        # 実行と検証
        with pytest.raises(ValueError, match="Segment plan not found for task_id: test_task_id"):
            before_model_callback(mock_callback_context, mock_llm_request)

    def test_before_model_callback_missing_listener_program(self, mock_callback_context, mock_llm_request, segment_plan):
        """リスナープログラム情報が欠けている場合のbefore_model_callbackのテスト"""
        # モックの設定（リスナープログラム情報なし）
        mock_callback_context.state["temp:writer:test_task_id:segment"] = segment_plan.model_dump()
        mock_callback_context.agent_name = "hoge_test_task_id"
        # 実行と検証
        with pytest.raises(ValueError, match="Listener program not found"):
            before_model_callback(mock_callback_context, mock_llm_request)

    @pytest.mark.asyncio
    async def test_real(self, segment_plan, listener_program):
        """実際のエージェント実行テスト"""
        # セッションサービスとランナーの設定
        session_service = InMemorySessionService()
        runner = Runner(
            app_name="test",
            agent=ProgramSegmentWriterAgent(task_id="test_task_id"),
            session_service=session_service,
        )

        # セッションの作成と状態の設定
        session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                "temp:writer:test_task_id:segment": segment_plan.model_dump(),
                "user:listener_program": listener_program.model_dump(),
            },
        )

        # エージェントの実行
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            print("------------------")
            print(event.model_dump())
            print("------------------")
