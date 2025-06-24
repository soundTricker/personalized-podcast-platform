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
from radio_station.sub_agents.program_planner.program_planner_agent import ProgramPlannerAgent

agent = ProgramPlannerAgent()


@pytest.fixture
def create_test_files(tmp_path):
    """テスト用のファイルを作成するフィクスチャ"""
    # テスト用のディレクトリを作成
    test_dir = tmp_path / "test_program_planner"
    test_dir.mkdir()

    # テスト用のセッションファイルを作成
    session_file = test_dir / "initial.session.json"

    # リスナープログラムの作成
    listener_program = ListenerProgram(id=1, listener_id=1, title="テスト番組", description="テスト番組の説明", program_minutes=30, insert_music=True)

    # 調査結果の作成
    research_results = [
        {
            "id": 1,
            "title": "テクノロジーニュース",
            "summary": "最新のテクノロジートレンドについての要約",
            "description": "AIと機械学習の最新動向についての詳細な分析。特に自然言語処理と画像認識の分野での進展が著しい。",
            "source": "Tech News RSS",
        },
        {
            "id": 2,
            "title": "健康と栄養",
            "summary": "健康的な食事と運動に関する最新の研究",
            "description": "最新の栄養学研究によると、バランスの取れた食事と定期的な運動が健康維持に重要であることが再確認されている。特に、野菜と果物の摂取量を増やすことが推奨されている。",
            "source": "Health News RSS",
        },
        {
            "id": 3,
            "title": "環境問題",
            "summary": "気候変動と持続可能性に関する最新情報",
            "description": "世界中の科学者たちが気候変動の影響を警告している。持続可能なエネルギー源への移行と二酸化炭素排出量の削減が急務とされている。",
            "source": "Environmental News RSS",
        },
    ]

    session_data = {
        "id": "test_session",
        "app_name": "radio_station",
        "user_id": "test_user",
        "state": {"user:listener_program": listener_program.model_dump(), "research:results": research_results},
        "events": [],
        "last_update_time": datetime.datetime.now().timestamp(),
    }
    session_file.write_text(json.dumps(session_data))

    # テスト用のevalsetファイルを作成
    evalset_file = test_dir / "program_planner.test.json"
    evalset_data = [
        {
            "query": "番組の構成を作成してください",
            "expected_tool_use": [],
            "expected_intermediate_agent_responses": [],
            "reference": json.dumps(
                {
                    "title": "テスト番組",
                    "listener_id": 1,
                    "listener_program_id": 1,
                    "description": "テスト番組の説明",
                    "program_seconds": 1800,  # 30分 = 1800秒
                    "segments": [
                        {"title": "テクノロジーの最新動向", "segment_seconds": 600, "program_segment_ids": [1], "is_music": False, "description": "AIと機械学習の最新トレンドについての分析"},
                        {"title": "リラックスミュージック", "segment_seconds": 120, "program_segment_ids": [], "is_music": True, "description": "穏やかなインストゥルメンタル音楽"},
                        {"title": "健康的な生活", "segment_seconds": 540, "program_segment_ids": [2], "is_music": False, "description": "バランスの取れた食事と運動の重要性について"},
                        {"title": "アップビートミュージック", "segment_seconds": 180, "program_segment_ids": [], "is_music": True, "description": "エネルギッシュなポップミュージック"},
                        {"title": "環境問題と持続可能性", "segment_seconds": 360, "program_segment_ids": [3], "is_music": False, "description": "気候変動と持続可能なエネルギーについての議論"},
                    ]
                },
                ensure_ascii=False,
            ),
        }
    ]
    evalset_file.write_text(json.dumps(evalset_data))

    # テスト用の設定ファイルを作成
    config_file = test_dir / "test_config.json"
    config_data = {"criteria": {"tool_trajectory_avg_score": 1.0, "response_match_score": 0.5}}
    config_file.write_text(json.dumps(config_data))

    return {"test_dir": test_dir, "session_file": session_file, "evalset_file": evalset_file, "config_file": config_file}


@pytest.mark.integration
def test_program_planner_agent_integration(create_test_files):
    """ProgramPlannerAgentの統合テスト"""
    test_files = create_test_files

    # モジュールパスを作成（テスト用のモジュールを動的に作成）
    module_dir = test_files["test_dir"] / "agent_module"
    module_dir.mkdir()

    # __init__.pyファイルを作成
    init_file = module_dir / "__init__.py"
    init_file.write_text("""
from radio_station.sub_agents.program_planner_agent import ProgramPlannerAgent

# テスト用のルートエージェントを作成
agent = ProgramPlannerAgent()
""")

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
