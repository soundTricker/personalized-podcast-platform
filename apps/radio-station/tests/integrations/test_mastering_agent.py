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

import io
import logging
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from google.adk import Runner
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService
from google.genai import types
from pydub import AudioSegment

from radio_station.model.program_plan import ProgramPlan, SegmentPlan, SegmentType
from radio_station.model.radio_cast import RadioCast, RadioCastRole
from radio_station.model.talk_script import TalkScript, TalkScriptSegment
from radio_station.state_keys import ComposerState, ProgramPlannerState, RecorderState, WriterState
from radio_station.sub_agents.mastering.agent import MasteringAgent

logger = logging.getLogger(__name__)


class TestMasteringAgent:
    """MasteringAgentの統合テスト"""

    @pytest.fixture
    def radio_casts(self):
        """ラジオキャストのテストデータ"""
        return [
            RadioCast(id="1", name="田中太郎", role=RadioCastRole.RadioPersonality, personality="明るく元気なパーソナリティ", voice_name="ja-JP-Wavenet-C"),
            RadioCast(id="2", name="佐藤花子", role=RadioCastRole.Assistant, personality="落ち着いた優しいアシスタント", voice_name="ja-JP-Wavenet-A"),
        ]

    @pytest.fixture
    def program_plan(self):
        """プログラムプランのテストデータ"""
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
                SegmentPlan(
                    title="エンディング",
                    program_segment_ids=[3],
                    segment_no=3,
                    segment_seconds=600,
                    is_music=False,
                    description="番組のエンディング",
                    segment_type=SegmentType.ENDING,
                    background_music="穏やかな音楽",
                    music_bpm=90.0,
                    radio_casts=[],
                ),
            ],
        )

    @pytest.fixture
    def talk_script_segments(self, radio_casts):
        """トークスクリプトセグメントのテストデータ"""
        return [
            TalkScriptSegment(
                id="tss_1",
                task_id="1",
                scripts=[
                    TalkScript(
                        radio_cast_id="1",
                        content="皆さん、こんにちは！今日も素晴らしい番組をお届けします。",
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
            TalkScriptSegment(
                id="tss_3",
                task_id="3",
                scripts=[
                    TalkScript(
                        radio_cast_id="1",
                        content="今日の番組はいかがでしたか？また次回もお楽しみに！",
                        speaking_rate=1.0,
                    )
                ],
                continue_segment=False,
            ),
        ]

    @pytest.fixture
    def mock_audio_data(self):
        """モック音声データを生成"""
        # 10秒間の無音データを作成（クロスフェード処理に対応するため長めに設定）
        audio = AudioSegment.silent(duration=10000)
        buffer = io.BytesIO()
        audio.export(buffer, format="wav")
        return buffer.getvalue()

    @pytest.mark.asyncio
    async def test_real(self, radio_casts, program_plan, talk_script_segments, mock_audio_data):
        """実際の動作のテスト"""

        session_service = InMemorySessionService()
        artifact_service = InMemoryArtifactService()

        logger.info("MasteringAgentのテストを開始します")

        # セッションを作成し、必要な状態データを設定
        session = await session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                # 録音されたタスクIDのリスト
                RecorderState.TEMP_TASK_IDS: ["1", "2", "3"],
                # 作曲されたタスクIDのリスト
                ComposerState.TASK_IDS: ["1", "2", "3"],
                # トークスクリプトセグメント
                WriterState.TALK_SCRIPT_SEGMENTS: [tss.model_dump() for tss in talk_script_segments],
                # プログラム構造
                ProgramPlannerState.PROGRAM_STRUCTURE: program_plan.model_dump(),
            },
        )

        # 必要なアーティファクトを事前に作成
        # 録音データのアーティファクト
        for tss in talk_script_segments:
            artifact_key = RecorderState.task_artifact_key(tss.id)
            await artifact_service.save_artifact(app_name="test", user_id="test", session_id="test", filename=artifact_key, artifact=types.Part.from_bytes(data=mock_audio_data, mime_type="audio/wav"))
            logger.info(f"録音データアーティファクトを作成: {artifact_key}")

        # 背景音楽のアーティファクト
        for task_id in ["1", "2", "3"]:
            artifact_key = ComposerState.task_music_artifact_key(task_id)
            await artifact_service.save_artifact(app_name="test", user_id="test", session_id="test", filename=artifact_key, artifact=types.Part.from_bytes(data=mock_audio_data, mime_type="audio/wav"))
            logger.info(f"背景音楽アーティファクトを作成: {artifact_key}")

        # MasteringAgentを実行
        runner = Runner(app_name="test", agent=MasteringAgent(), session_service=session_service, artifact_service=artifact_service)

        # エージェントを実行
        events = []
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            events.append(event)
            logger.info(f"イベント: {event.content.parts[0].text if event.content.parts else 'No content'}")

        # 実行後の状態を確認
        session = await session_service.get_session(app_name="test", user_id="test", session_id="test")
        logger.info(f"最終状態: {session.state}")

        # 生成されたアーティファクトを確認
        keys = await artifact_service.list_artifact_keys(app_name="test", user_id="test", session_id="test")
        logger.info(f"生成されたアーティファクト: {keys}")

        # audio.mp3が生成されていることを確認
        assert "audio.mp3" in keys, "audio.mp3が生成されていません"

        # 生成されたMP3ファイルを確認
        audio_mp3 = await artifact_service.load_artifact(app_name="test", user_id="test", session_id="test", filename="audio.mp3")
        assert audio_mp3 is not None, "audio.mp3の内容が空です"
        assert len(audio_mp3.inline_data.data) > 0, "audio.mp3のデータサイズが0です"

        logger.info("MasteringAgentのテストが正常に完了しました")

    @pytest.mark.asyncio
    async def test_already_finished_task(self, radio_casts, program_plan, talk_script_segments, mock_audio_data):
        """既にaudio.mp3が存在する場合のテスト"""

        session_service = InMemorySessionService()
        artifact_service = InMemoryArtifactService()

        # セッションを作成
        session = await session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={
                RecorderState.TEMP_TASK_IDS: ["1", "2", "3"],
                ComposerState.TASK_IDS: ["1", "2", "3"],
                WriterState.TALK_SCRIPT_SEGMENTS: [tss.model_dump() for tss in talk_script_segments],
                ProgramPlannerState.PROGRAM_STRUCTURE: program_plan.model_dump(),
            },
        )

        # 事前にaudio.mp3を作成
        await artifact_service.save_artifact(app_name="test", user_id="test", session_id="test", filename="audio.mp3", artifact=types.Part.from_bytes(data=mock_audio_data, mime_type="audio/mp3"))

        # MasteringAgentを実行
        runner = Runner(app_name="test", agent=MasteringAgent(), session_service=session_service, artifact_service=artifact_service)

        events = []
        async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
            events.append(event)

        # "already finished this task"メッセージが返されることを確認
        assert len(events) > 0, "イベントが生成されていません"
        assert any("already finished this task" in event.content.parts[0].text for event in events if event.content.parts), "既に完了済みのメッセージが返されていません"

    @pytest.mark.asyncio
    async def test_missing_task_ids(self):
        """task_idsが存在しない場合のテスト"""

        session_service = InMemorySessionService()
        artifact_service = InMemoryArtifactService()

        # task_idsを設定せずにセッションを作成
        session = await session_service.create_session(
            app_name="test",
            user_id="test",
            session_id="test",
            state={},
        )

        runner = Runner(app_name="test", agent=MasteringAgent(), session_service=session_service, artifact_service=artifact_service)

        # ValueErrorが発生することを確認
        with pytest.raises(ValueError, match="task_ids not found in state"):
            async for event in runner.run_async(user_id="test", session_id="test", new_message=types.Content(parts=[types.Part(text="")])):
                pass
