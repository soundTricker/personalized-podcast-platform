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
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService, State
from google.cloud import texttospeech
from google.genai import types

from radio_station.model.radio_cast import RadioCast, RadioCastRole
from radio_station.model.talk_script import TalkScript
from radio_station.sub_agents.recoder.recorder_agent import RecorderAgent


class TestRecorderAgent:
    """RecorderAgentクラスのユニットテスト"""

    @pytest.fixture
    def radio_cast(self):
        """テスト用のRadioCastを作成するフィクスチャ"""
        return RadioCast(id=1, name="Test Cast", role=RadioCastRole.RadioPersonality, personality="明るく元気")

    @pytest.fixture
    def talk_script(self):
        """テスト用のTalkScriptを作成するフィクスチャ"""
        return TalkScript(content="こんにちは。テストです。", radio_cast_id=1)

    @pytest.mark.asyncio
    async def test_run_async_impl(self, mock_context, talk_script, radio_cast):
        """基本的な動作のテスト"""
        # モックの設定
        task_id = "1"
        mock_context.session.state[f"{State.TEMP_PREFIX}recorder:{task_id}:redio_cast"] = radio_cast.model_dump()
        mock_context.session.state[f"{State.TEMP_PREFIX}recorder:{task_id}:talk_script"] = talk_script.model_dump()
        mock_context.session.id = "1"

        artifact_service = InMemoryArtifactService()
        mock_context.artifact_service = artifact_service

        # TextToSpeechClientのモック
        mock_response = MagicMock()
        mock_response.audio_content = b"test audio content"
        with patch("google.cloud.texttospeech.TextToSpeechClient") as MockTTSClient:
            mock_tts_client = MagicMock()
            MockTTSClient.return_value = mock_tts_client
            mock_tts_client.synthesize_speech.return_value = mock_response

            # 実行
            agent = RecorderAgent(task_id=task_id)
            events = [event async for event in agent._run_async_impl(mock_context)]

            # 検証
            assert len(events) == 1
            assert events[0].author == f"RecorderAgent_{task_id}"
            assert "Generated audio for: こんにちは。テストです。" in events[0].content.parts[0].text
            assert events[0].content.parts[1].inline_data.data == b"test audio content"
            assert events[0].content.parts[1].inline_data.mime_type == "audio/mp3"

            # TextToSpeechClientが正しく呼び出されたことを検証
            mock_tts_client.synthesize_speech.assert_called_once()
            args, kwargs = mock_tts_client.synthesize_speech.call_args
            assert kwargs["input"].markup == "こんにちは。テストです。"
            assert kwargs["voice"].language_code == "ja-JP"
            assert kwargs["voice"].name == "ja-JP-Chirp3-HD-Achird"
            assert kwargs["audio_config"].audio_encoding == texttospeech.AudioEncoding.MP3

    @pytest.mark.asyncio
    async def test_real(self, radio_cast):
        """実際のエージェント実行テスト"""
        # セッションサービスとランナーの設定
        session_service = InMemorySessionService()
        artifact_service = InMemoryArtifactService()
        runner = Runner(
            app_name="test",
            agent=RecorderAgent(task_id="test_task_id"),
            session_service=session_service,
            artifact_service=artifact_service
        )

        # セッションの作成と状態の設定
        session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                "temp:recorder:test_task_id:redio_cast": radio_cast.model_dump(),
                "temp:recorder:test_task_id:talk_script":  {'radio_cast_id': 1, 'speaking_rate': 1.0, 'content': 'ええ。さらに4月30日には、Model GardenでLlama 4 MaverickとScoutモデルが利用可能になりました。他にも、HiDream-I1、Llama Guard 4、Llama Prompt Guard 2、Qwen3といったモデルが追加されています。', 'custom_pronunciations': {'pronunciations': [{'phrase': 'Model Garden', 'pronunciation': 'モデルガーデン'}, {'phrase': 'Llama 4 Maverick', 'pronunciation': 'ラマフォーマベリック'}, {'phrase': 'Scout', 'pronunciation': 'スカウト'}, {'phrase': 'HiDream-I1', 'pronunciation': 'ハイドリームアイワン'}, {'phrase': 'Qwen3', 'pronunciation': 'クウェンスリー'}]}},
            },
        )

        # エージェントの実行
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            print("------------------")
            print(event.model_dump())
            print("------------------")

        mp3file = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename="audio_test_task_id.mp3")

        with open("test_audio.mp3", "wb") as f:
            f.write(mp3file.inline_data.data)
