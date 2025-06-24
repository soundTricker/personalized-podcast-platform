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
import logging

import pytz
from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from radio_station.state_keys import GlobalState, NewsLetterWriterState, ProgramPlannerState, ResearcherState, WriterState

logger = logging.getLogger(__name__)


class NewsLetterWriterAgent(LlmAgent):
    def __init__(self):
        super().__init__(
            model=LiteLlm(model="vertex_ai/gemini-2.5-flash-lite-preview-06-17"),
            name="NewsLetterWriterAgent",
            description="The AI Generate News Letter Writer Agent by this radio program",
            instruction="""
            You are AI New Letter Writer Agent for this radio program.
            Your task is writing a new letter contents for this radio program.
            The writing new letter contents should be based on this radio program talk scripts, program plan, and research results.
            
            # Tasks
            1. Read and analyze <ProgramPlan>PROGRAM_PLAN</ProgramPlan>
            2. Read and analyze <ResearchResult>RESEARCH_RESULT</ResearchResult>
            3. Read and analyze <TalkScripts>TALK_SCRIPTS</TalkScripts>
            4. Read and analyze <RadioCasts>RADIO_CASTS</RadioCasts>
            5. Generate a news letter contents based on 1.-4. documents.

            # Guidelines
            - The program has already been distributed. Write under the assumption that the content has already been distributed.
            - Explain the program title and number of broadcast like "第0回" and segment titles and what talked in this program and segments.
            - This new letter is published with e-mail, write as e-mail body text.
            - When research result includes URL and contents, and that is explained in talk scripts, write introducing URL and title.
            - Don't write radio cast name.
            - The `Segment`say as 'コーナー'
            - Don't write a mail subject.

            # Output
            Japanese, Github Favorite Markdown style.
            """,
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
            before_model_callback=self.insert_content,
            after_model_callback=self.save_content,
        )

    def insert_content(self, callback_context: CallbackContext, llm_request: LlmRequest):
        state = callback_context.state
        radio_casts = GlobalState.get_radio_casts(state)
        program_structure = ProgramPlannerState.get_program_structure(state)
        research_results = state.get(ResearcherState.RESULTS)
        talk_script_segments = WriterState.get_talk_script_segments(state)
        llm_request.contents.append(
            types.UserContent(
                parts=[
                    types.Part.from_text(
                        text=f"""
        <CurrentTime>{datetime.datetime.now(tz=pytz.timezone("Asia/Tokyo")).isoformat()}</CurrentTime>
        <ProgramPlan>{program_structure.to_llm_text(include_segments=True)}</ProgramPlan>
        <ResearchResult>{json.dumps(research_results, ensure_ascii=False)}</ResearchResult>
        <RadioCasts>{"\n=========".join([radio_cast.to_llm_text() for radio_cast in radio_casts])}</RadioCasts>
        <TalkScripts>
            {"\n=========".join([tss.to_talk_script_text(radio_casts) for tss in talk_script_segments])}
        </TalkScripts>
        """
                    )
                ]
            )
        )

    def save_content(self, callback_context: CallbackContext, llm_response: LlmResponse) -> None:
        logger.info(f"Generated New Letter: {llm_response.content.parts[-1].text}")
        callback_context.state.update({NewsLetterWriterState.CONTENTS: llm_response.content.parts[-1].text})
