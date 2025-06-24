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
import json
import sys

import pytest
from google.adk.evaluation import AgentEvaluator

from radio_station.model.listener_program import ListenerProgram
from radio_station.model.listener_program_segment import ListenerProgramSegment, ListenerProgramRSSSegment
from radio_station.model.program_plan import SegmentPlan
from radio_station.model.radio_cast import RadioCast, RadioCastRole
from radio_station.model.talk_script import TalkScript, TalkScripts


@pytest.fixture
def create_test_files(tmp_path):
    """テスト用のファイルを作成するフィクスチャ"""
    # テスト用のディレクトリを作成
    test_dir = tmp_path / "test_program_segment_writer"
    test_dir.mkdir()

    # テスト用のセッションファイルを作成
    session_file = test_dir / "initial.session.json"

    # リスナープログラムの作成
    listener_program = ListenerProgram(
        id=1,
        listener_id=1,
        title="テスト番組",
        description="テスト番組の説明",
        program_minutes=30,
        insert_music=True,
        base_radio_casts=[
            RadioCast(id=1, name="パーソナリティ太郎", role=RadioCastRole.RadioPersonality, personality="明るく陽気"),
            RadioCast(id=2, name="アシスタント次郎", role=RadioCastRole.Assistant, personality="冷静沈着なツッコミ役"),
        ],
    )

    # 番組セグメントの作成
    listener_program_segments = [
        ListenerProgramRSSSegment(
            id=1,
            listener_id=1,
            listener_program_id=1,
            title="テクノロジーの話題",
            description="最新のテクノロジーニュースについて",
            feed_url="https://zenn.dev/feed",
        )
    ]

    # セグメント計画の作成
    segment_plan = SegmentPlan(
        title="テクノロジーの話題",
        description="最新のテクノロジーニュースについて",
        program_segment_ids=[1],
        segment_seconds=10,
        is_music=False
    )

    session_data = {
        "id": "test_session",
        "app_name": "radio_station",
        "user_id": "test_user",
        "state": {
            "user:listener_program": listener_program.model_dump(),
            "user:listener_program_segments": [s.model_dump() for s in listener_program_segments],
            "temp:writer:1:segment": segment_plan.model_dump(),  # task_id=1 を仮定
            "writer:next_segment": SegmentPlan(title="エンディング", description="番組のエンディング", program_segment_ids=[], segment_seconds=10, is_music=False).model_dump(),
            "writer:talk_scripts": [
                TalkScripts(
                    scripts=[
                        TalkScript(radio_cast_id=1, content="こんにちはテスト番組の時間です。 パーソナリティのパーソナリティ太郎です！"),
                        TalkScript(radio_cast_id=2, content="アシスタント次郎です。"),
                        TalkScript(radio_cast_id=1, content="この番組はテスト番組の〇〇について△△する番組です。"),
                    ]
                ).model_dump(),
            ],
        },
        "events": [],
        "last_update_time": datetime.datetime.now().timestamp(),
    }
    session_file.write_text(json.dumps(session_data, ensure_ascii=False))

    # テスト用のevalsetファイルを作成
    evalset_file = test_dir / "program_segment_writer.test.json"
    evalset_data = [
        {
            "query": "台本を作成してください",
            "expected_tool_use": [],
            "expected_intermediate_agent_responses": [],
            "reference": json.dumps(
                {
                    "scripts": [
                        {
                            "radio_cast_id": 1,
                            "content": "皆さん、こんにちは！今日の「テクノロジーの話題」では、最新のAI技術についてお話しします。",
                        },
                        {
                            "radio_cast_id": 2,
                            "content": "はい、パーソナリティさん。特に注目されているのは、〇〇と△△の分野ですね。",
                        },
                    ]
                },
                ensure_ascii=False,
            ),
        }
    ]
    evalset_file.write_text(json.dumps(evalset_data, ensure_ascii=False))

    # テスト用の設定ファイルを作成
    config_file = test_dir / "test_config.json"
    config_data = {"criteria": {"tool_trajectory_avg_score": 1.0, "response_match_score": 0.5}}
    config_file.write_text(json.dumps(config_data))

    return {
        "test_dir": test_dir,
        "session_file": session_file,
        "evalset_file": evalset_file,
        "config_file": config_file,
    }


@pytest.mark.integration
def test_program_segment_writer_agent_integration(create_test_files):
    """ProgramSegmentWriterAgentの統合テスト"""
    test_files = create_test_files

    # モジュールパスを作成（テスト用のモジュールを動的に作成）
    module_dir = test_files["test_dir"] / "agent_module"
    module_dir.mkdir()

    # __init__.pyファイルを作成
    init_file = module_dir / "__init__.py"
    init_file.write_text(
        """
from radio_station.sub_agents.writer.program_segment_writer_agent import ProgramSegmentWriterAgent

# テスト用のルートエージェントを作成
agent = ProgramSegmentWriterAgent(task_id="1")  # task_id=1 を指定
"""
    )

    sys.path.append(str(test_files["test_dir"]))

    # 評価を実行
    try:
        AgentEvaluator.evaluate(
            module_dir.name.replace("/", "."),
            str(test_files["evalset_file"]),
            initial_session_file=str(test_files["session_file"]),
        )
    except Exception as e:
        pytest.fail(f"Test setup failed: {e}")
