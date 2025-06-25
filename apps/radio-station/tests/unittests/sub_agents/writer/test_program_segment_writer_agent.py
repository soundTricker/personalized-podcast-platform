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

import pytest
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from radio_station.constants import GENERIC_MODEL
from radio_station.model.listener_program import ListenerProgram
from radio_station.model.program_plan import SegmentPlan
from radio_station.model.radio_cast import RadioCast, RadioCastRole
from radio_station.state_keys import GlobalState, ProgramPlannerState, ResearcherState
from radio_station.sub_agents.writer.program_segment_writer_agent import ProgramSegmentWriterAgent


class TestProgramSegmentWriterAgent:
    """ProgramSegmentWriterAgentのテストクラス"""

    @pytest.fixture
    def segment_plan(self):
        """テスト用のSegmentPlanを作成"""
        return SegmentPlan(title="テストセグメント", program_segment_ids=[1, 2], segment_seconds=300, is_music=False, description="テストセグメントの説明")

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
                RadioCast(
                    id=3,
                    name="ゲースト三郎",
                    role=RadioCastRole.Guest,
                    personality="静かな専門家",
                    voice_name="ja-JP-Chirp3-HD-Algieba",
                ),
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

    @pytest.mark.asyncio
    async def test_real(self, segment_plan, listener_program, research_results, radio_casts):
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
                ProgramPlannerState.PROGRAM_STRUCTURE: segment_plan.model_dump(),
                GlobalState.LISTENER_PROGRAM: listener_program.model_dump(),
                ResearcherState.RESULTS: research_results,
                GlobalState.RADIO_CASTS: radio_casts,
            },
        )

        # エージェントの実行
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            print("------------------")
            print(event.model_dump())
            print("------------------")
