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
from google.adk.agents import RunConfig
from google.adk.sessions import InMemorySessionService, State
from google.genai import types

from radio_station.constants import GENERIC_MODEL
from radio_station.model.listener_program_segment import ListenerProgramRSSSegment
from radio_station.state_keys import ResearcherState
from radio_station.sub_agents.researcher.rss_researcher_agent import RssFeedResearchAgent


class TestRssFeedResearchAgent:
    """RssFeedResearchAgentクラスのユニットテスト"""

    def test_init(self):
        """初期化のテスト"""
        # 実行
        agent = RssFeedResearchAgent(task_id="test")

        # 検証
        assert agent.name == "RssFeedResearchAgent_test"
        assert agent.model == GENERIC_MODEL
        assert agent.output_key == "research:test:research_result"
        assert "summary" in agent.instruction
        assert "JSON" in agent.instruction
        assert "Output Format" in agent.instruction
        assert "Output Schema" in agent.instruction

    def test_init_with_custom_params(self):
        """カスタムパラメータでの初期化テスト"""
        # 実行
        # RssFeedResearchAgentの実装では、model引数とoutput_key引数は内部で上書きされるため、
        # 他のカスタムパラメータをテストする必要がある
        # ここではカスタムパラメータを使用せず、基本的な初期化のみをテスト
        agent = RssFeedResearchAgent(task_id="custom_name")

        # 検証
        assert agent.name == "RssFeedResearchAgent_custom_name"
        assert agent.model == GENERIC_MODEL
        assert agent.output_key == "research:custom_name:research_result"

    @pytest.mark.asyncio
    async def test_real(self):
        session_service = InMemorySessionService()
        runner = Runner(
            app_name="test",
            agent=RssFeedResearchAgent(task_id="task_id"),
            session_service=session_service,
        )
        session = session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                ResearcherState.task_info("task_id"): ListenerProgramRSSSegment(
                    id=1, listener_id=1, listener_program_id=1, title="Test Feed", description="Test Description", feed_url="https://cloud.google.com/feeds/vertex-ai-product-group-release-notes.xml"
                ).model_dump()
            },
        )

        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")]), run_config=RunConfig()):
            print("------------------")
            print(event.model_dump())
            print("------------------")
        print(session.state)
