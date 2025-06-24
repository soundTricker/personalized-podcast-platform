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

# tests/unittests/sub_agents/recorder/test_synthesis_agent.py

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from google.adk import Runner
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService
from google.genai import types as genai_types
from pydub import AudioSegment

from radio_station.state_keys import ComposerState, RecorderState
from radio_station.sub_agents.mastering.synthesis_agent import RecordingSynthesisAgent


@pytest.fixture
def mock_audio_segment():
    """AudioSegmentのモックを提供するフィクスチャ"""
    segment = MagicMock(spec=AudioSegment)
    segment.dBFS = -20  # dBFSのデフォルト値を設定
    segment.__len__ = MagicMock(return_value=10000) # 10秒の長さ
    segment.__add__ = MagicMock(return_value=segment) # + 演算子
    segment.__mul__ = MagicMock(return_value=segment) # * 演算子
    segment.fade = MagicMock(return_value=segment)
    segment.fade_out = MagicMock(return_value=segment)
    segment.overlay = MagicMock(return_value=segment)
    segment.append = MagicMock(return_value=segment)

    # exportメソッドのモック
    def mock_export(buf, format):
        buf.write(b"fake_mp3_data")
    segment.export = MagicMock(side_effect=mock_export)
    return segment

class TestRecordingSynthesisAgent:
    """RecordingSynthesisAgentクラスのユニットテスト"""

    @pytest.mark.asyncio
    async def test_run_async_impl_no_task_ids(self, mock_context):
        """task_idsがstateにない場合にValueErrorを発生させることをテスト"""
        agent = RecordingSynthesisAgent()
        mock_context.session.state = {} # task_idsを空にする

        with pytest.raises(ValueError, match="task_ids not found in state."):
            async for _ in agent._run_async_impl(mock_context):
                pass

    @pytest.mark.asyncio
    @patch("radio_station.sub_agents.recoder.synthesis_agent.load_artifact", new_callable=AsyncMock)
    @patch("radio_station.sub_agents.recoder.synthesis_agent.save_artifact", new_callable=AsyncMock)
    @patch("radio_station.sub_agents.recoder.synthesis_agent.AudioSegment.from_mp3")
    @patch("radio_station.sub_agents.recoder.synthesis_agent.AudioSegment.silent")
    @patch("radio_station.sub_agents.recoder.synthesis_agent.normalize")
    @patch("radio_station.sub_agents.recoder.synthesis_agent.compress_dynamic_range")
    async def test_run_async_impl_success(
        self,
        mock_compress,
        mock_normalize,
        mock_silent,
        mock_from_mp3,
        mock_save_artifact,
        mock_load_artifact,
        mock_context,
        mock_audio_segment # モックされたAudioSegmentを使用
    ):
        """正常系のテスト: _run_async_implがmixingを呼び出し、イベントを生成することを確認"""
        task_ids = ["task1", "task2"]
        mock_context.session.state[RecorderState.TEMP_TASK_IDS] = task_ids
        mock_context.session.state[ComposerState.TASK_IDS] = ["task1"] # task1のみBGMあり

        # モックの設定
        mock_from_mp3.return_value = mock_audio_segment
        mock_silent.return_value = mock_audio_segment
        mock_normalize.return_value = mock_audio_segment
        mock_compress.return_value = mock_audio_segment

        # load_artifactのモック設定 (2回呼び出される: recoding_audio と backend_music)
        mock_recoding_artifact = genai_types.Part.from_bytes(mime_type="audio/mp3", data=b"fake_rec_data")
        mock_music_artifact = genai_types.Part.from_bytes(mime_type="audio/mp3", data=b"fake_music_data")
        mock_load_artifact.side_effect = [mock_recoding_artifact, mock_music_artifact, mock_recoding_artifact] # task2はBGMなしなのでrecodingのみ

        agent = RecordingSynthesisAgent()

        events = []
        async for event in agent._run_async_impl(mock_context):
            events.append(event)

        assert len(events) == 1
        event = events[0]
        assert event.author == "RecordingSynthesisAgent"
        assert event.content.role == "model"
        assert event.content.parts[0].text == f"Generated merged audio for: {task_ids}"

        # mixingが呼び出されたことを確認 (直接呼び出す代わりに、内部の処理が実行されたかで判断)
        assert mock_load_artifact.call_count >= 1 # 少なくとも1回は呼ばれる
        mock_save_artifact.assert_called_once()
        # save_artifactに渡された引数を検証
        args, kwargs = mock_save_artifact.call_args
        assert args[0] == mock_context
        assert args[1] == "audio.mp3"
        assert isinstance(args[2], genai_types.Part)
        assert args[2].inline_data.mime_type == "audio/mp3"

        # AudioSegment.from_mp3 の呼び出し回数確認
        # task1 (recoding + music), task2 (recoding)
        assert mock_from_mp3.call_count == 3

        # AudioSegment.silent の呼び出し回数確認 (task2のBGM用)
        assert mock_silent.call_count == 3

        # normalizeとcompress_dynamic_rangeが呼ばれたか
        mock_normalize.assert_called_once()
        assert mock_compress.call_count == 1

    @pytest.mark.asyncio
    async def test_real(self):
        """実際の動作のテスト"""
        session_service = InMemorySessionService()
        artifact_service = InMemoryArtifactService()
        runner = Runner(
            app_name="test",
            agent=RecordingSynthesisAgent(),
            session_service=session_service,
            artifact_service=artifact_service
        )

        composer_task_ids = ["1", "2", "3", "4", "5"]
        task_ids = ["1", "2", "3", "4", "5"]

        # セッションの作成と状態の設定
        session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                ComposerState.TASK_IDS: composer_task_ids,
                RecorderState.TEMP_TASK_IDS: task_ids,
            },
        )

        for task_id in composer_task_ids:

            with open(ComposerState.task_music_artifact_key(task_id), "rb") as f:
                await artifact_service.save_artifact(app_name="test",
                                               user_id="test",
                                               session_id="test",
                                               filename=ComposerState.task_music_artifact_key(task_id),
                                               artifact=genai_types.Part.from_bytes(data=f.read(), mime_type="audio/mp3")
                                               )
        for task_id in task_ids:
            with open(RecorderState.task_artifact_key(task_id), "rb") as f:
                await artifact_service.save_artifact(app_name="test",
                                               user_id="test",
                                               session_id="test",
                                               filename=RecorderState.task_artifact_key(task_id),
                                               artifact=genai_types.Part.from_bytes(data=f.read(), mime_type="audio/mp3")
                                               )

        # エージェントの実行
        async for event in runner.run_async(user_id="test", session_id="test", new_message=genai_types.Content(parts=[genai_types.Part(text="")])):
            print("------------------")
            print(event.model_dump())
            print("------------------")

        mp3file = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename="audio.mp3")

        with open("test_audio.mp3", "wb") as f:
            f.write(mp3file.inline_data.data)

