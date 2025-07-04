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

import logging
import sys

import pytest
from google.adk.runners import InMemoryRunner
from google.genai import types

from radio_station.model.talk_script import TalkScriptSegment
from radio_station.state_keys import GlobalState
from radio_station.sub_agents.recoder.llm_tts_recorder_agent import LLMTTSRecorderAgent

file_handler = logging.FileHandler("test.log")
file_handler.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout), file_handler])  # noqa: F821
logger = logging.getLogger(__name__)


class TestLLMTTSRecorderAgent:
    """LLMRecorderAgentクラスのユニットテスト"""

    @pytest.mark.asyncio
    async def test_real(self, radio_casts, talk_scripts_dicts, listener_program):
        talk_script_segments = [TalkScriptSegment(**tsd) for tsd in talk_scripts_dicts]
        talk_script_segment = talk_script_segments[0]

        """実際のエージェント実行テスト"""
        # セッションサービスとランナーの設定
        runner = InMemoryRunner(
            app_name="test",
            agent=LLMTTSRecorderAgent(task_id="test_task_id", talk_script_segment=talk_script_segment, radio_casts=radio_casts, seed=0),
        )

        session_service = runner.session_service
        artifact_service = runner.artifact_service

        # セッションの作成と状態の設定
        await session_service.create_session(app_name="test", user_id="test", session_id="test", state={GlobalState.LISTENER_PROGRAM: listener_program.model_dump()})

        # エージェントの実行
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="speech")])):
            logger.info("----------")
            logger.info(event)

        mp3file = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename="audio_test_task_id.mp3")

        if not mp3file:
            logger.info("[MISSING FILE]")
            return

        with open("test_audio.mp3", "wb") as f:
            f.write(mp3file.inline_data.data)
