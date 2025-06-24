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

from unittest.mock import MagicMock, patch

import pytest
from google.adk import Runner
from google.adk.agents import ParallelAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.adk.sessions import InMemorySessionService, Session, State
from google.genai import types

from radio_station.model.listener_program_segment import (
    ListenerProgramRSSSegment,
    ListenerProgramWeatherSegment,
)
from radio_station.sub_agents.researcher.flow_agent import ResearchFlowAgent
from radio_station.sub_agents.researcher.rss_researcher_agent import RssFeedResearchAgent


class TestResearchFlowAgent:
    """ResearchFlowAgentクラスのユニットテスト"""

    @pytest.fixture
    def mock_context(self):
        """テスト用のコンテキストを作成するフィクスチャ"""
        session = MagicMock(spec=Session)
        session.state = {}
        ctx = MagicMock(spec=InvocationContext)
        ctx.session = session
        return ctx

    @pytest.fixture
    def rss_segment(self):
        """テスト用のRSSセグメントを作成するフィクスチャ"""
        return ListenerProgramRSSSegment(id=1, listener_id=100, listener_program_id=200, title="Test RSS Feed", description="Test RSS Description", feed_url="https://example.com/rss")

    @pytest.fixture
    def rss_segment2(self):
        """テスト用のRSSセグメントを作成するフィクスチャ"""
        return ListenerProgramRSSSegment(id=2, listener_id=101, listener_program_id=201, title="Test RSS Feed2", description="Test RSS Description2", feed_url="https://example.com/rss")

    @pytest.fixture
    def weather_segment(self):
        """テスト用の天気セグメントを作成するフィクスチャ"""
        return ListenerProgramWeatherSegment(id=2, listener_id=100, listener_program_id=200, title="Test Weather", description="Test Weather Description", area="Tokyo")

    def test_init(self):
        """初期化のテスト"""
        # 実行
        agent = ResearchFlowAgent(name="TestResearchFlow")

        # 検証
        assert agent.name == "TestResearchFlow"
        assert isinstance(agent, ResearchFlowAgent)

    @pytest.mark.asyncio
    async def test_run_async_impl_with_rss_segment(self, mock_context, rss_segment):
        """RSSセグメントを処理するテスト"""
        # モックの設定
        mock_context.session.state["listener_program_segments"] = [rss_segment.model_dump()]

        # ParallelAgentのrun_asyncをモック
        mock_event = Event(author="ParallelResearchAgent", content=types.Content(role="ParallelResearchAgent", parts=[types.Part(text="Test event")]))

        with patch("radio_station.sub_agents.researcher.flow_agent.ParallelAgent", autospec=True) as mock_parallel_agent_class:
            # ParallelAgentのインスタンスとrun_asyncメソッドをモック
            mock_parallel_agent = MagicMock(spec=ParallelAgent)
            mock_parallel_agent_class.return_value = mock_parallel_agent

            # run_asyncメソッドが非同期ジェネレータを返すようにモック
            async def mock_run_async(*args, **kwargs):
                yield mock_event

            mock_parallel_agent.run_async = mock_run_async

            # 実行
            agent = ResearchFlowAgent(name="TestResearchFlow")

            # task_infoをセッション状態に設定
            mock_context.session.state[f"{State.TEMP_PREFIX}1:task_info"] = rss_segment.model_dump()

            # 研究結果をセッションに設定
            mock_context.session.state["research:1:research_result"] = {"summary": "Test summary", "detail": "Test detail", "description": "Test detail", "entries": []}

            events = [event async for event in agent._run_async_impl(mock_context)]

            # 検証
            assert len(events) == 2
            assert events[0] == mock_event
            assert events[1].author == "TestResearchFlow"
            assert "Research Result (Segment:1)" in events[1].content.parts[0].text
            assert "Test summary" in events[1].content.parts[0].text
            assert "Test detail" in events[1].content.parts[0].text

            # ParallelAgentが正しく作成されたことを検証
            mock_parallel_agent_class.assert_called_once()
            args, kwargs = mock_parallel_agent_class.call_args
            assert kwargs["name"] == "ParallelResearchAgent"
            assert len(kwargs["sub_agents"]) == 1
            assert isinstance(kwargs["sub_agents"][0], RssFeedResearchAgent)
            assert kwargs["sub_agents"][0].name == "RssFeedResearchAgent_1"

            # セッション状態が正しく更新されたことを検証
            assert mock_context.session.state["research:task_ids"] == [1]

    @pytest.mark.asyncio
    async def test_run_async_impl_with_multiple_segments(self, mock_context, rss_segment, weather_segment):
        """複数のセグメントを処理するテスト"""
        # モックの設定
        mock_context.session.state["listener_program_segments"] = [rss_segment.model_dump(), weather_segment.model_dump()]

        # ParallelAgentのrun_asyncをモック
        mock_event = Event(author="ParallelResearchAgent", content=types.Content(role="ParallelResearchAgent", parts=[types.Part(text="Test event")]))

        with patch("radio_station.sub_agents.researcher.flow_agent.ParallelAgent", autospec=True) as mock_parallel_agent_class:
            # ParallelAgentのインスタンスとrun_asyncメソッドをモック
            mock_parallel_agent = MagicMock(spec=ParallelAgent)
            mock_parallel_agent_class.return_value = mock_parallel_agent

            # run_asyncメソッドが非同期ジェネレータを返すようにモック
            async def mock_run_async(*args, **kwargs):
                yield mock_event

            mock_parallel_agent.run_async = mock_run_async

            # 実行
            agent = ResearchFlowAgent(name="TestResearchFlow")

            # task_infoをセッション状態に設定
            mock_context.session.state[f"{State.TEMP_PREFIX}1:task_info"] = rss_segment.model_dump()
            mock_context.session.state[f"{State.TEMP_PREFIX}2:task_info"] = weather_segment.model_dump()

            # 研究結果をセッションに設定
            mock_context.session.state["research:1:research_result"] = {"summary": "RSS summary", "detail": "RSS detail", "description": "RSS detail", "entries": []}
            # 2つ目のセグメントの研究結果も設定
            mock_context.session.state["research:2:research_result"] = {"summary": "Weather summary", "detail": "Weather detail", "description": "Weather detail", "entries": []}

            events = [event async for event in agent._run_async_impl(mock_context)]

            # 検証
            assert len(events) == 2
            assert events[0] == mock_event
            assert events[1].author == "TestResearchFlow"
            assert "Research Result (Segment:1)" in events[1].content.parts[0].text
            assert "RSS summary" in events[1].content.parts[0].text
            # 2つ目のセグメントの検証
            assert len(events[1].content.parts) == 2
            assert "Research Result (Segment:2)" in events[1].content.parts[1].text
            assert "Weather summary" in events[1].content.parts[1].text

            # ParallelAgentが正しく作成されたことを検証
            mock_parallel_agent_class.assert_called_once()
            args, kwargs = mock_parallel_agent_class.call_args
            assert kwargs["name"] == "ParallelResearchAgent"
            assert len(kwargs["sub_agents"]) == 1  # 現在はRSSセグメントのみ処理される
            assert isinstance(kwargs["sub_agents"][0], RssFeedResearchAgent)

            # セッション状態が正しく更新されたことを検証
            assert set(mock_context.session.state["research:task_ids"]) == {1, 2}

    @pytest.mark.asyncio
    async def test_run_async_impl_with_no_segments(self, mock_context):
        """セグメントがない場合のテスト"""
        # モックの設定
        mock_context.session.state["listener_program_segments"] = []

        with patch("radio_station.sub_agents.researcher.flow_agent.ParallelAgent", autospec=True) as mock_parallel_agent_class:
            # ParallelAgentのインスタンスとrun_asyncメソッドをモック
            mock_parallel_agent = MagicMock(spec=ParallelAgent)
            mock_parallel_agent_class.return_value = mock_parallel_agent

            # run_asyncメソッドが非同期ジェネレータを返すようにモック
            async def mock_run_async(*args, **kwargs):
                return
                yield  # この行は実行されない

            mock_parallel_agent.run_async = mock_run_async

            # 実行
            agent = ResearchFlowAgent(name="TestResearchFlow")
            events = [event async for event in agent._run_async_impl(mock_context)]

            # 検証
            assert len(events) == 1
            assert events[0].author == "TestResearchFlow"
            assert len(events[0].content.parts) == 0

            # ParallelAgentが正しく作成されたことを検証
            mock_parallel_agent_class.assert_called_once()
            args, kwargs = mock_parallel_agent_class.call_args
            assert kwargs["name"] == "ParallelResearchAgent"
            assert len(kwargs["sub_agents"]) == 0

            # セッション状態が正しく更新されたことを検証
            assert mock_context.session.state["research:task_ids"] == []

    @pytest.mark.asyncio
    async def test_real(self):
        session_service = InMemorySessionService()
        runner = Runner(
            app_name="test",
            agent=ResearchFlowAgent(name="ResearchFlowAgent"),
            session_service=session_service,
        )
        session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                "listener_program_segments": [
                    ListenerProgramRSSSegment(
                        id=1,
                        listener_id=100,
                        listener_program_id=200,
                        title="Vertex AIの最新ニュース",
                        description="Vertex AIの最新ニュースを説明するコーナーです。",
                        feed_url="https://cloud.google.com/feeds/vertex-ai-product-group-release-notes.xml",
                    ).model_dump(),
                    ListenerProgramRSSSegment(
                        id=2,
                        listener_id=101,
                        listener_program_id=201,
                        title="Zennのトレンド",
                        description="技術系ブログZennのトレンドフィードから最近の技術トレンドを説明するコーナー",
                        feed_url="https://zenn.dev/feed",
                    ).model_dump(),
                ]
            },
        )

        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            print("------------------")
            print(event.model_dump())
            print("------------------")

        session = runner.session_service.get_session(app_name="test", user_id="test", session_id="test")

        print(session.state.get('research:task_ids'))
        print(session.state.get('research:results'))
