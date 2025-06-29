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
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from google.adk import Runner
from google.adk.agents.invocation_context import InvocationContext
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService, Session
from google.genai import types
from pydub import AudioSegment

from radio_station.model.program_plan import ProgramPlan, SegmentPlan, SegmentType
from radio_station.model.talk_script import TalkScript, TalkScriptSegment
from radio_station.state_keys import ComposerState, ProgramPlannerState, RecorderState, WriterState
from radio_station.sub_agents.mastering.agent import MasteringAgent

logger = logging.getLogger(__name__)


@pytest.fixture
def mock_context():
    """モックのInvocationContextを提供するフィクスチャ"""
    context = MagicMock(spec=InvocationContext)
    context.invocation_id = "test_invocation_id"
    context.session = MagicMock(spec=Session)
    context.session.state = {}
    return context


@pytest.fixture
def mock_audio_segment():
    """AudioSegmentのモックを提供するフィクスチャ"""
    segment = MagicMock(spec=AudioSegment)
    segment.dBFS = -20  # dBFSのデフォルト値を設定
    segment.__len__ = MagicMock(return_value=10000)  # 10秒の長さ
    segment.__add__ = MagicMock(return_value=segment)  # + 演算子
    segment.__mul__ = MagicMock(return_value=segment)  # * 演算子
    segment.fade = MagicMock(return_value=segment)
    segment.fade_out = MagicMock(return_value=segment)
    segment.overlay = MagicMock(return_value=segment)
    segment.append = MagicMock(return_value=segment)
    segment.apply_gain = MagicMock(return_value=segment)

    # exportメソッドのモック
    def mock_export(buf, format):
        buf.write(b"fake_mp3_data")

    segment.export = MagicMock(side_effect=mock_export)
    return segment


@pytest.fixture
def sample_program_plan():
    """サンプルのプログラムプランを提供するフィクスチャ"""
    return ProgramPlan(
        title="テスト番組",
        description="テスト用の番組です",
        program_seconds=1800,
        segments=[
            SegmentPlan(
                title="オープニング",
                program_segment_ids=[1],
                segment_no=1,
                segment_seconds=300,
                is_music=False,
                description="番組のオープニング",
                segment_type=SegmentType.OPENING,
                background_music="アップビートな音楽",
                music_bpm=120.0,
                radio_casts=[],
            ),
            SegmentPlan(
                title="メインコンテンツ",
                program_segment_ids=[2],
                segment_no=2,
                segment_seconds=900,
                is_music=False,
                description="メインの話題",
                segment_type=SegmentType.CONTENT,
                background_music="落ち着いた音楽",
                music_bpm=80.0,
                radio_casts=[],
            ),
        ],
    )


@pytest.fixture
def sample_talk_script_segments():
    """サンプルのトークスクリプトセグメントを提供するフィクスチャ"""
    return [
        TalkScriptSegment(
            id="tss_1",
            task_id="1",
            scripts=[
                TalkScript(
                    radio_cast_id="1",
                    content="皆さん、こんにちは！",
                    speaking_rate=1.0,
                )
            ],
            continue_segment=False,
        ),
        TalkScriptSegment(
            id="tss_2",
            task_id="2",
            scripts=[
                TalkScript(
                    radio_cast_id="2",
                    content="今日のメインテーマについてお話しします。",
                    speaking_rate=1.0,
                )
            ],
            continue_segment=False,
        ),
    ]


class TestMasteringAgent:
    """MasteringAgentクラスのユニットテスト"""

    @pytest.mark.asyncio
    @patch("radio_station.sub_agents.mastering.agent.list_artifact", new_callable=AsyncMock)
    async def test_run_async_impl_already_finished(self, mock_list_artifact, mock_context):
        """audio.mp3が既に存在する場合のテスト"""
        mock_list_artifact.return_value = ["audio.mp3"]

        agent = MasteringAgent()
        events = []
        async for event in agent._run_async_impl(mock_context):
            events.append(event)

        assert len(events) == 1
        event = events[0]
        assert event.author == "MasteringAgent"
        assert "already finished this task" in event.content.parts[0].text

    @pytest.mark.asyncio
    @patch("radio_station.sub_agents.mastering.agent.list_artifact", new_callable=AsyncMock)
    async def test_run_async_impl_no_task_ids(self, mock_list_artifact, mock_context):
        """task_idsがstateにない場合にValueErrorを発生させることをテスト"""
        mock_list_artifact.return_value = []
        mock_context.session.state = {}  # task_idsを空にする

        agent = MasteringAgent()
        with pytest.raises(ValueError, match="task_ids not found in state"):
            async for _ in agent._run_async_impl(mock_context):
                pass

    @pytest.mark.asyncio
    @patch("radio_station.sub_agents.mastering.agent.list_artifact", new_callable=AsyncMock)
    @patch("radio_station.sub_agents.mastering.agent.save_artifact", new_callable=AsyncMock)
    @patch("radio_station.sub_agents.mastering.agent.convert_mp3")
    @patch.object(MasteringAgent, "mixing", new_callable=AsyncMock)
    @patch.object(MasteringAgent, "mastering", new_callable=AsyncMock)
    async def test_run_async_impl_success(
        self, mock_mastering, mock_mixing, mock_convert_mp3, mock_save_artifact, mock_list_artifact, mock_context, sample_program_plan, sample_talk_script_segments, mock_audio_segment
    ):
        """正常系のテスト: _run_async_implが正常に動作することを確認"""
        mock_list_artifact.return_value = []
        mock_convert_mp3.return_value = b"fake_mp3_data"
        mock_mixing.return_value = mock_audio_segment
        mock_mastering.return_value = mock_audio_segment

        task_ids = ["1", "2"]
        mock_context.session.state = {
            RecorderState.TEMP_TASK_IDS: task_ids,
            ComposerState.TASK_IDS: ["1"],
            WriterState.TALK_SCRIPT_SEGMENTS: [tss.model_dump() for tss in sample_talk_script_segments],
            ProgramPlannerState.PROGRAM_STRUCTURE: sample_program_plan.model_dump(),
        }

        agent = MasteringAgent()

        events = []
        async for event in agent._run_async_impl(mock_context):
            events.append(event)

        # 4つのイベントが生成されることを確認
        assert len(events) == 4

        # 各イベントの内容を確認
        assert "Start generating for:" in events[0].content.parts[0].text
        assert "Finished mixing for:" in events[1].content.parts[0].text
        assert "Finished mastering for:" in events[2].content.parts[0].text
        assert "Generated merged audio for:" in events[3].content.parts[0].text

        # mixingとmasteringが呼び出されたことを確認
        mock_mixing.assert_called_once_with(mock_context)
        mock_mastering.assert_called_once_with(mock_audio_segment)

        # save_artifactが呼び出されたことを確認
        mock_save_artifact.assert_called_once()
        args, kwargs = mock_save_artifact.call_args
        assert args[0] == mock_context
        assert args[1] == "audio.mp3"

    @pytest.mark.asyncio
    @patch("radio_station.sub_agents.mastering.agent.load_artifact", new_callable=AsyncMock)
    @patch("radio_station.sub_agents.mastering.agent.AudioSegment.from_wav")
    @patch("radio_station.sub_agents.mastering.agent.AudioSegment.silent")
    @patch("radio_station.sub_agents.mastering.agent.is_run_on_agent_engine")
    async def test_mixing_method(self, mock_is_run_on_agent_engine, mock_silent, mock_from_wav, mock_load_artifact, mock_context, sample_program_plan, sample_talk_script_segments, mock_audio_segment):
        """mixingメソッドの単体テスト"""
        mock_is_run_on_agent_engine.return_value = False
        mock_from_wav.return_value = mock_audio_segment
        mock_silent.return_value = mock_audio_segment

        # モックアーティファクトの設定
        mock_artifact = types.Part.from_bytes(mime_type="audio/wav", data=b"fake_audio_data")
        mock_load_artifact.return_value = mock_artifact

        task_ids = ["1", "2"]
        mock_context.session.state = {
            ComposerState.TASK_IDS: ["1"],  # task1のみBGMあり
            RecorderState.TEMP_TASK_IDS: task_ids,
            WriterState.TALK_SCRIPT_SEGMENTS: [tss.model_dump() for tss in sample_talk_script_segments],
            ProgramPlannerState.PROGRAM_STRUCTURE: sample_program_plan.model_dump(),
        }

        agent = MasteringAgent()
        result = await agent.mixing(mock_context)

        # 結果がAudioSegmentのモックであることを確認
        assert result == mock_audio_segment

        # load_artifactが呼び出されたことを確認
        assert mock_load_artifact.call_count >= 1

    @pytest.mark.asyncio
    @patch("radio_station.sub_agents.mastering.agent.compress_dynamic_range")
    @patch("radio_station.sub_agents.mastering.agent.normalize")
    async def test_mastering_method(self, mock_normalize, mock_compress, mock_audio_segment):
        """masteringメソッドの単体テスト"""
        mock_compress.return_value = mock_audio_segment
        mock_normalize.return_value = mock_audio_segment

        agent = MasteringAgent()
        result = await agent.mastering(mock_audio_segment)

        # 結果がAudioSegmentのモックであることを確認
        assert result == mock_audio_segment

        # compress_dynamic_rangeとnormalizeが呼び出されたことを確認
        mock_compress.assert_called_once_with(mock_audio_segment, threshold=-20, ratio=2.5, attack=5, release=50)
        mock_normalize.assert_called_once_with(mock_audio_segment)

    @pytest.mark.asyncio
    @patch("radio_station.sub_agents.mastering.agent.load_artifact", new_callable=AsyncMock)
    @patch("radio_station.sub_agents.mastering.agent.AudioSegment.from_wav")
    @patch("radio_station.sub_agents.mastering.agent.AudioSegment.silent")
    async def test_mixing_with_different_segment_types(self, mock_silent, mock_from_wav, mock_load_artifact, mock_context, mock_audio_segment):
        """異なるセグメントタイプでのmixingテスト"""
        mock_from_wav.return_value = mock_audio_segment
        mock_silent.return_value = mock_audio_segment

        # モックアーティファクトの設定
        mock_artifact = types.Part.from_bytes(mime_type="audio/wav", data=b"fake_audio_data")
        mock_load_artifact.return_value = mock_artifact

        # 音楽セグメントを含むプログラムプラン
        program_plan_with_music = ProgramPlan(
            title="テスト番組",
            description="音楽セグメントを含む番組",
            program_seconds=1800,
            segments=[
                SegmentPlan(
                    title="音楽セグメント",
                    program_segment_ids=[],
                    segment_no=1,
                    segment_seconds=300,
                    is_music=True,
                    description="音楽のみのセグメント",
                    segment_type=SegmentType.MUSIC,
                    radio_casts=[],
                ),
            ],
        )

        talk_script_segments = [
            TalkScriptSegment(
                id="tss_1",
                task_id="1",
                scripts=[],
                continue_segment=False,
            ),
        ]

        mock_context.session.state = {
            ComposerState.TASK_IDS: ["1"],
            RecorderState.TEMP_TASK_IDS: ["1"],
            WriterState.TALK_SCRIPT_SEGMENTS: [tss.model_dump() for tss in talk_script_segments],
            ProgramPlannerState.PROGRAM_STRUCTURE: program_plan_with_music.model_dump(),
        }

        agent = MasteringAgent()
        result = await agent.mixing(mock_context)

        # 結果がAudioSegmentのモックであることを確認
        assert result == mock_audio_segment

        # 音楽セグメントの処理が実行されたことを確認
        assert mock_load_artifact.call_count >= 1

    @pytest.mark.asyncio
    async def test_real(self, program_plan, talk_scripts_dicts):
        session_service = InMemorySessionService()
        artifact_service = InMemoryArtifactService()

        session = await session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                RecorderState.TEMP_TASK_IDS: ["1", "2", "3", "4"],
                ComposerState.TASK_IDS: ["1", "2", "3", "4"],
                WriterState.TALK_SCRIPT_SEGMENTS: talk_scripts_dicts,
                ProgramPlannerState.PROGRAM_STRUCTURE: program_plan.model_dump(),
            },
        )

        for task_id in ["1", "2", "3", "4"]:
            with open(f"./{ComposerState.task_music_artifact_key(task_id)}", "rb") as f:
                await artifact_service.save_artifact(
                    app_name="test",
                    user_id="test",
                    session_id="test",
                    filename=ComposerState.task_music_artifact_key(task_id),
                    artifact=types.Part.from_bytes(data=f.read(), mime_type="audio/wav"),
                )
            with open(f"./{RecorderState.task_artifact_key(task_id)}", "rb") as f:
                await artifact_service.save_artifact(
                    app_name="test",
                    user_id="test",
                    session_id="test",
                    filename=RecorderState.task_artifact_key(task_id),
                    artifact=types.Part.from_bytes(data=f.read(), mime_type="audio/wav"),
                )

        agent = MasteringAgent()
        runner = Runner(app_name="test", agent=agent, session_service=session_service, artifact_service=artifact_service)
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            pass

        mp3file = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename="audio.mp3")
        with open("audio.mp3", "wb") as f:
            f.write(mp3file.inline_data.data)
