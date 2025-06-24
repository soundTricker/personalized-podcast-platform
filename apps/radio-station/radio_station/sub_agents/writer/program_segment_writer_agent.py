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
from typing import Optional
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.genai import types
from pydantic import Field

from radio_station.constants import THINKING_MODEL
from radio_station.model.talk_script import TalkScriptSegment
from radio_station.state_keys import GlobalState, WriterState
from radio_station.utils.instruction_provider import secret_instruction


class ProgramSegmentWriterAgent(Agent):
    """
    番組コーナー作家Agent。
    ラジオ内でキャストが読む台本を作成する。
    """

    task_id: str = Field(description="Task ID")

    def __init__(self, task_id: str, **kwargs):
        """
        ProgramSegmentWriterAgentを初期化します。

        Args:
            task_id: タスクID。
            **kwargs: Agentコンストラクタに渡す追加の引数。
        """
        super().__init__(
            task_id=task_id,
            model=THINKING_MODEL,
            name=f"ProgramSegmentWriterAgent_{task_id}",
            instruction=secret_instruction(
                "program_segment_writer_instruction",
                """
            You are an AI radio program writer. Your task is to create a script for the speaker(radio cast) to read within a radio program.
A radio program has multiple segments.
You will create a talk script for one of the segments.
""",
            ),
            before_model_callback=self.add_instruction,
            output_schema=TalkScriptSegment,
            output_key=WriterState.task_talk_script_segment(task_id),
            generate_content_config=types.GenerateContentConfig(
                temperature=0.7,
                frequency_penalty=-2.0,
                max_output_tokens=60000,
                safety_settings=[
                    types.SafetySetting(
                        category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                    ),
                    types.SafetySetting(
                        category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                    ),
                    types.SafetySetting(
                        category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                    ),
                    types.SafetySetting(
                        category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                    ),
                ],
            ),
            include_contents="none",
            **kwargs,
        )

    def add_instruction(self, callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
        """
        番組コーナー詳細情報とリスナープログラム情報を追加してモデルのコンテキストを準備します。

        Args:
            callback_context: コールバックのコンテキスト。
            llm_request: LLMへのリクエスト。

        Returns:
            Optional[LlmResponse]: モデル呼び出しを続行するためにNoneを返します。
        """
        llm_request.append_instructions([f"[Task ID]\n{self.task_id}"])

        task_id = self.task_id

        previous_segment_plan = WriterState.get_previous_segment(callback_context.state, task_id)
        next_segment_plan = WriterState.get_next_segment(callback_context.state, task_id)
        research_result_dicts = callback_context.state.get(WriterState.task_research_results(task_id), [])
        talk_script_segments = WriterState.get_talk_script_segments(callback_context.state)

        radio_casts = GlobalState.get_radio_casts(callback_context.state)

        talk_scripts = []
        for tss in talk_script_segments:
            talk_scripts.append(tss.to_talk_script_text(radio_casts))

        # Stateから番組コーナー詳細情報を取得
        segment_plan = WriterState.get_segment(callback_context.state, task_id)
        if not segment_plan:
            raise ValueError(f"Segment plan not found for task_id: {task_id}")

        listener_program = GlobalState.get_listener_program(callback_context.state)

        radio_casts = segment_plan.radio_casts

        callback_context.state.update({WriterState.task_radio_cast(task_id): radio_casts})

        # モデルの指示に情報を追加

        if WriterState.task_continue_prev_segment(task_id) in callback_context.state:
            prev = WriterState.get_continue_prev_segment(callback_context.state, task_id)
            llm_request.contents.append(
                types.UserContent(
                    parts=[
                        types.Part.from_text(
                            text=f"""
                <Previous on the way Segment>
                <Hands Over>
                {prev.hand_over}
                </Hands Over>
    
                <Previous Talk Scripts>
                {prev.to_talk_script_text(radio_casts)}
                </Previous Talk Scripts>
                </Previous on the way Segment>
                """
                        )
                    ],
                )
            )
            callback_context.state[WriterState.task_continue_prev_segment(task_id)] = None

        llm_request.contents.append(
            types.UserContent(
                parts=[
                    types.Part.from_text(
                        text=f"""
    [Current Time]
    {datetime.datetime.now(tz=ZoneInfo("Asia/Tokyo")).isoformat()}
    
    [Program]
    {listener_program.to_llm_text()}
    
    [Current Segment Plan]
    {segment_plan.to_llm_text()}
    
    [Current Segment Research Results]
    {json.dumps(research_result_dicts, ensure_ascii=False)}
    
    [Number of Radio Casts]
    {len(radio_casts)}
    
    [Radio Casts]
    {"\n".join([cast.to_llm_text() for cast in radio_casts])}
    
    <The Talk Scripts so far>
    {"\n".join(talk_scripts)}
    </The Talk Scripts so far>
    
    [Previous Segment]
    {previous_segment_plan.to_llm_text() if previous_segment_plan else "Nothing"}
    
    [Next Segment]
    {next_segment_plan.to_llm_text() if next_segment_plan else "Nothing"}
    """
                    )
                ]
            )
        )

        return None
