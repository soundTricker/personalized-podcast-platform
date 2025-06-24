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

# tests/unittests/sub_agents/composer/test_composer_agent.py

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from google.adk import Runner
from google.adk.runners import InMemoryRunner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from radio_station.sub_agents.composer.composer_agent import ComposerAgent

# generate_music_tool は ComposerAgent の __init__ で直接参照されるため、
# パッチを適用する際には、それが参照される場所 (composer_agent モジュール内) を指定します。
# from radio_station.sub_agents.composer.tools import generate_music_tool # テスト内で直接は使わない

# ComposerAgentが初期化時に参照するgenerate_music_toolをモック化するための正しいパッチターゲット
PATCH_TARGET_GENERATE_MUSIC_TOOL = 'radio_station.sub_agents.composer.composer_agent.generate_music_tool'
PATCH_TARGET_LLM_GENERATE_CONTENT = 'google.genai.GenerativeModel.generate_content_async'


class TestComposerAgent:
    """ComposerAgentクラスのユニットテスト"""

    @pytest.fixture
    def music_plan_fixture(self):
        """テスト用の音楽プランを提供するフィクスチャ"""
        return {
            "title": "Sunset Chill Beats",
            "description": "A relaxing lofi hip hop track perfect for watching the sunset.",
            "segment_seconds": 45,
        }

    @pytest.fixture
    def composer_agent_instance(self, music_plan_fixture):
        """テスト用のComposerAgentインスタンスを提供するフィクスチャ"""
        return ComposerAgent(task_id="test_task_init", music_plan=music_plan_fixture)

    def test_init(self, composer_agent_instance, music_plan_fixture):
        """初期化のテスト"""
        agent = composer_agent_instance
        task_id = "test_task_init" # composer_agent_instance で使用した task_id

        assert agent.task_id == task_id
        assert agent.music_plan == music_plan_fixture

        # instructionにmusic_planの内容が含まれているか確認
        assert music_plan_fixture.get('title') in agent.instruction
        assert music_plan_fixture.get('description') in agent.instruction
        assert str(music_plan_fixture.get('segment_seconds')) in agent.instruction

        # toolsにgenerate_music_toolが含まれているか確認
        # ComposerAgent内で `from .tools import generate_music_tool` としている場合、
        # `agent.tools[0]` はそのインポートされたオブジェクトを指す。
        # ここでは、そのオブジェクトの `name` 属性で確認する（より堅牢）。
        assert len(agent.tools) == 1
        assert agent.tools[0].name == "generate_music_tool"


    @pytest.mark.asyncio
    async def test_real(self):
        runner = InMemoryRunner(
            app_name="test",
            agent=ComposerAgent("task_id", {"title": "カフェで流れる朝にぴったりなピアノジャズ", "description": "カフェで流れる朝にぴったりなピアノジャズ", "segment_seconds": 45}),
        )
        session_service = runner.session_service
        session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
            },
        )

        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            print("------------------")
            print(event.model_dump())
            print("------------------")


        part = await runner.artifact_service.load_artifact(app_name="test",user_id="test",session_id="test", filename=f"generated_audio_task_id_0.mp3")
        with open("test_audio.mp3", "wb") as f:
            f.write(part.inline_data.data)
