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

"""
リスナープログラムとリサーチ結果に基づいてプログラム構造を作成するProgramPlannerAgent。
"""

import json
from typing import Optional

from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.sessions import State
from google.genai import types

from radio_station.constants import THINKING_MODEL
from radio_station.model.program_plan import ProgramPlan, SegmentPlan
from radio_station.state_keys import GlobalState, ProgramPlannerState, ResearcherState
from radio_station.utils.instruction_provider import secret_instruction


def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    """
    リスナープログラムと調査結果を追加してモデルのコンテキストを準備します。

    Args:
        callback_context: コールバックのコンテキスト。
        llm_request: LLMへのリクエスト。

    Returns:
        Optional[LlmResponse]: モデル呼び出しを続行するためにNoneを返します。
    """
    # Stateからリスナープログラムを取得
    listener_program = GlobalState.get_listener_program(callback_context.state)

    # Stateから調査結果を取得
    research_results = callback_context.state.get(ResearcherState.RESULTS)

    # リスナープログラムと調査結果をモデルの指示に追加
    llm_request.contents.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=f"""
[Program]
{listener_program.to_llm_text()}

[Segments]
{json.dumps(research_results, ensure_ascii=False)}
"""
                )
            ],
        )
    )

    return None


class ProgramPlannerAgent(Agent):
    """
    リスナープログラムと調査結果に基づいてプログラム構造を作成するエージェント。

    このエージェントはリスナープログラムの設定と調査結果を分析し、
    番組コーナーと音楽（有効な場合）を含む構造化されたプログラムを作成します。
    """

    def __init__(self, name="ProgramPlannerAgent", **kwargs):
        """
        ProgramPlannerAgentを初期化します。

        Args:
            **kwargs: Agentコンストラクタに渡す追加の引数。
        """
        super().__init__(
            model=THINKING_MODEL,
            name=name,
            instruction=secret_instruction(
                "program_planner_instruction",
                """"
You are a Radio Program Planner AI that creates a structured program based on listener preferences and investigation results.
""",
            ),
            before_agent_callback=self.check_resume,
            before_model_callback=before_model_callback,
            generate_content_config=types.GenerateContentConfig(
                temperature=1,
                frequency_penalty=-2.0,
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
            output_schema=ProgramPlan,
            output_key=ProgramPlannerState.PROGRAM_STRUCTURE,
            after_agent_callback=self.update_state,
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
            include_contents="none",
            **kwargs,
        )

    def check_resume(self, callback_context: CallbackContext) -> types.Content | None:
        pp = ProgramPlannerState.get_program_structure(callback_context.state)
        if pp is not None:
            return types.ModelContent(parts=[types.Part.from_text(text="already finished this task")])
        return None

    async def update_state(self, callback_context: CallbackContext) -> types.Content | None:
        pp = ProgramPlannerState.get_program_structure(callback_context.state)

        for i, sp in enumerate(pp.segments):
            sp.segment_no = i + 1
            sp.radio_casts = detect_radio_casts(callback_context.state, sp)

        callback_context.state.update({ProgramPlannerState.PROGRAM_STRUCTURE: pp.model_dump()})
        return None


def detect_radio_casts(state: State, segment_plan: SegmentPlan):
    # Stateからリスナープログラム情報を取得
    listener_program = GlobalState.get_listener_program(state)
    if not listener_program:
        raise ValueError("Listener program not found")
    # Stateから番組コーナー情報を取得
    listener_program_segments = GlobalState.get_listener_program_segments(state)
    listener_program_segment = next((s for s in listener_program_segments if s.id in segment_plan.program_segment_ids), None)
    radio_casts = listener_program.base_radio_casts or []
    if listener_program_segment:
        if listener_program_segment.override_radio_casts:
            radio_casts = listener_program_segment.override_radio_casts
        if listener_program_segment.additional_guests:
            radio_casts.extend(listener_program_segment.additional_guests)
    if not radio_casts:
        raise ValueError("No radio casts found")
    return radio_casts


# default agent instance
agent = ProgramPlannerAgent()
