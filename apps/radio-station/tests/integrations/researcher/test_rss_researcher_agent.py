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

from radio_station.sub_agents.researcher.rss_researcher_agent import RssFeedResearchAgent

agent = RssFeedResearchAgent("test")


@pytest.fixture
def mock_feedparser():
    """feedparserをモックするフィクスチャ"""
    with patch("feedparser.parse") as mock_parse:
        # モックの設定
        mock_feed = MagicMock()
        mock_feed.title = "Test Feed"
        mock_feed.link = "https://example.com"
        mock_feed.description = "Test Description"
        mock_feed.updated = "2023-02-01"
        mock_feed.updated_parsed = datetime.datetime(2023, 2, 1).timetuple()

        mock_entry = MagicMock()
        mock_entry.title = "Test Entry"
        mock_entry.link = "https://example.com/entry"
        mock_entry.description = "Test Entry Description"
        mock_entry.updated = "2023-02-01"
        mock_entry.updated_parsed = datetime.datetime(2023, 2, 1).timetuple()

        mock_parse.return_value = MagicMock(feed=mock_feed, entries=[mock_entry])
        yield mock_parse


@pytest.fixture
def create_test_files(tmp_path):
    """テスト用のファイルを作成するフィクスチャ"""
    # テスト用のディレクトリを作成
    test_dir = tmp_path / "test_rss_researcher"
    test_dir.mkdir()

    # テスト用のセッションファイルを作成
    session_file = test_dir / "initial.session.json"
    session_data = {
        "id": "test_session",
        "app_name": "radio_station",
        "user_id": "test_user",
        "state": {
            f"{State.TEMP_PREFIX}test:task_info": {
                "feed_url": "https://example.com/rss",
                "last_read_timestamp": datetime.datetime(2023, 1, 1).timestamp(),
            }
        },
        "events": [],
        "last_update_time": datetime.datetime.now().timestamp(),
    }
    session_file.write_text(json.dumps(session_data))

    # テスト用のevalsetファイルを作成
    evalset_file = test_dir / "rss_researcher.test.json"
    evalset_data = [
        {
            "query": "RSSフィードの要約を作成してください",
            "expected_tool_use": [],
            "expected_intermediate_agent_responses": [],
            "reference": json.dumps(
                {
                    "summary": "テストフィードのコンテンツです。最新の更新は2023年2月1日に行われました。エントリは一つで、タイトルは「Test Entry」、リンクはhttps://example.com/entryです。",
                    "detail": "このテストフィードは、example.comで提供されています。2023年2月1日に更新され、一つのエントリが含まれています。そのエントリのタイトルは「Test Entry」で、詳細な説明は「Test Entry Description」とされています。エントリへのリンクはhttps://example.com/entryです。",
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
def test_rss_researcher_agent_integration(create_test_files, mock_feedparser):
    """RssFeedResearchAgentの統合テスト"""
    test_files = create_test_files

    # モジュールパスを作成（テスト用のモジュールを動的に作成）
    module_dir = test_files["test_dir"] / "agent_module"
    module_dir.mkdir()

    # __init__.pyファイルを作成
    init_file = module_dir / "__init__.py"
    init_file.write_text("""
from radio_station.sub_agents.researcher.rss_researcher_agent import RssFeedResearchAgent

# テスト用のルートエージェントを作成
agent = RssFeedResearchAgent("test")
""")

    sys.path.append(str(test_files["test_dir"]))

    # 評価を実行
    try:
        AgentEvaluator.evaluate(
            module_dir.name.replace("/", "."),
            str(test_files["evalset_file"]),
            initial_session_file=str(test_files["session_file"]),
            # config_file_path=str(test_files["config_file"])
        )
    except Exception as e:
        pytest.fail(f"Agent evaluation failed: {e}")
