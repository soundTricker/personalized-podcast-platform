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
from unittest.mock import MagicMock, patch

import pytest
from google.adk.evaluation import AgentEvaluator
from google.adk.sessions import State

from radio_station.model.listener_program_segment import (
    ListenerProgramRSSSegment,
)


@pytest.fixture
def mock_feedparser():
    """feedparserをモックするフィクスチャ"""
    with patch("feedparser.parse") as mock_parse:

        def side_effect(url):
            # URLに基づいて異なるフィードを返す
            if "rss1" in url:
                mock_feed = MagicMock()
                mock_feed.title = "Test Feed 1"
                mock_feed.link = "https://example.com/feed1"
                mock_feed.description = "Test Description 1"
                mock_feed.updated = "2023-02-01"
                mock_feed.updated_parsed = datetime.datetime(2023, 2, 1).timetuple()

                mock_entry = MagicMock()
                mock_entry.title = "Test Entry 1"
                mock_entry.link = "https://example.com/entry1"
                mock_entry.description = "Test Entry Description 1"
                mock_entry.updated = "2023-02-01"
                mock_entry.updated_parsed = datetime.datetime(2023, 2, 1).timetuple()

                return MagicMock(feed=mock_feed, entries=[mock_entry])
            else:
                mock_feed = MagicMock()
                mock_feed.title = "Test Feed 2"
                mock_feed.link = "https://example.com/feed2"
                mock_feed.description = "Test Description 2"
                mock_feed.updated = "2023-02-01"
                mock_feed.updated_parsed = datetime.datetime(2023, 2, 1).timetuple()

                mock_entry = MagicMock()
                mock_entry.title = "Test Entry 2"
                mock_entry.link = "https://example.com/entry2"
                mock_entry.description = "Test Entry Description 2"
                mock_entry.updated = "2023-02-01"
                mock_entry.updated_parsed = datetime.datetime(2023, 2, 1).timetuple()

                return MagicMock(feed=mock_feed, entries=[mock_entry])

        mock_parse.side_effect = side_effect
        yield mock_parse


@pytest.fixture
def create_test_files(tmp_path):
    """テスト用のファイルを作成するフィクスチャ"""
    # テスト用のディレクトリを作成
    test_dir = tmp_path / "test_flow_agent"
    test_dir.mkdir()

    # RSSセグメントを作成
    rss_segment1 = ListenerProgramRSSSegment(id=1, listener_id=100, listener_program_id=200, title="Test RSS Feed 1", description="Test RSS Description 1", feed_url="https://example.com/rss1")

    # 2つ目のRSSセグメントを作成
    rss_segment2 = ListenerProgramRSSSegment(id=2, listener_id=101, listener_program_id=201, title="Test RSS Feed 2", description="Test RSS Description 2", feed_url="https://example.com/rss2")

    # テスト用のセッションファイルを作成
    session_file = test_dir / "initial.session.json"
    session_data = {
        "id": "test_session",
        "app_name": "radio_station",
        "user_id": "test_user",
        "state": {"listener_program_segments": [rss_segment1.model_dump(), rss_segment2.model_dump()]},
        "events": [],
        "last_update_time": datetime.datetime.now().timestamp(),
    }
    session_file.write_text(json.dumps(session_data))

    # テスト用のevalsetファイルを作成
    evalset_file = test_dir / "flow_agent.test.json"
    evalset_data = [
        {
            "query": "リサーチフローを実行してください",
            "expected_tool_use": [],
            "expected_intermediate_agent_responses": [],
            "reference": """
        [[Research Result (Segment:1)]]
        Investigation ID: 1
        Segment Title: Test RSS Feed 1
        Segment Description: Test RSS Description 1
        Investigation Result: {}

        [[Investigation Result (Segment:2)]]
        Segment ID: 2
        Segment Title: Test RSS Feed 2
        Segment Description: Test RSS Description 2
        Investigation Result: {}
        """,
        }
    ]
    evalset_file.write_text(json.dumps(evalset_data))

    # テスト用の設定ファイルを作成
    config_file = test_dir / "test_config.json"
    config_data = {"criteria": {"tool_trajectory_avg_score": 1.0, "response_match_score": 0.5}}
    config_file.write_text(json.dumps(config_data))

    return {"test_dir": test_dir, "session_file": session_file, "evalset_file": evalset_file, "config_file": config_file}


@pytest.mark.integration
def test_flow_agent_integration_with_multiple_segments(create_test_files, mock_feedparser):
    """ResearchFlowAgentの統合テスト"""
    test_files = create_test_files

    # モジュールパスを作成（テスト用のモジュールを動的に作成）
    module_dir = test_files["test_dir"] / "agent_module"
    module_dir.mkdir()

    # __init__.pyファイルを作成
    init_file = module_dir / "__init__.py"
    init_file.write_text("""
from radio_station.sub_agents.researcher.flow_agent import ResearchFlowAgent
agent = ResearchFlowAgent(name="ResearchFlowAgent")
""")

    # 研究結果をモック
    with patch.dict("sys.modules"):
        # テスト用のモジュールをsys.pathに追加
        sys.path.append(str(test_files["test_dir"]))

        # 評価を実行
        try:
            AgentEvaluator.evaluate(
                module_dir.name.replace("/", "."),
                str(test_files["evalset_file"]),
                initial_session_file=str(test_files["session_file"]),
            )
        except Exception as e:
            pytest.fail(f"Agent evaluation failed: {e}")
