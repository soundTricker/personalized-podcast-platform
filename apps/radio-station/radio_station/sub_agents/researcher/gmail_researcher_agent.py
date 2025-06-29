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
from typing import Optional

from google.adk.agents import Agent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.planners import PlanReActPlanner
from google.genai import types
from pydantic import Field

from radio_station.constants import GENERIC_MODEL
from radio_station.model.base_model import BaseModel
from radio_station.model.listener_program_segment import ListenerProgramGmailSegment
from radio_station.state_keys import ResearcherState
from radio_station.tools.gmail_tool import list_gmail_messages


class GmailEvent(BaseModel):
    title: str = Field(description="Mail Title")
    summary: str | None = Field(description="Mail summary", default=None)
    description: str | None = Field(description="Mail description", default=None)
    received_at: str = Field(description="Mail received date-time in ISO format")


class GmailResearchResult(BaseModel):
    summary: str = Field(description="Summary of the mails")
    mails: list[GmailEvent] = Field(description="List of mail")


class GmailResearchAgent(Agent):
    task_id: str | int = Field(description="The task id")

    def __init__(self, task_id, **kwargs):
        super().__init__(
            task_id=task_id,
            model=GENERIC_MODEL,
            name=f"GmailResearchAgent_{task_id}",
            instruction="""
                You are an AI Gmail thread Summarization Assistant specializing in creating radio program segments.

                Your tasks are:
                1. Search gmail messages for a specified period by using the `list_gmail_messages` tool
                    - Searching query in `Gmail Query Information`
                    - You must use `list_gmail_messages` tool to search gmail mails. max_results should be 100
                    - `list_gmail_messages`
                2. Create a summary of the mail within on Task Info.
                    - When Gmail Query Information is not found, please return JSON Object like `{"summary": "no messages found in this query"}`

                Constrains:
                - **USE** the list_gmail_messages tool **ONLY ONCE**.

                Output Format:
                JSON, Japanese.

                Output Schema:
                Make a JSON with below attributes.

                - 'summary': A short summary of the gmail messages.
                - 'mails': A list of mails, each with:
                    - 'title': A mail subject.
                    - 'summary': A short summary of the mail.
                    - 'description': A detailed description of the mail (if available).
                    - 'received_at': The mail received date in ISO format.
            """,
            tools=[list_gmail_messages],
            generate_content_config=types.GenerateContentConfig(
                max_output_tokens=8000,
                frequency_penalty=-2.0,
            ),
            before_model_callback=self.insert_task_info,
            before_agent_callback=self.make_gmail_info,
            output_key=ResearcherState.research_result(task_id),
            planner=PlanReActPlanner(),
            disallow_transfer_to_parent=True,
            include_contents="none",
            **kwargs,
        )

    def insert_task_info(self, callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
        llm_request.contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(
                        text=f"""
                            Task Info:
                            {ResearcherState.get_task_info(callback_context.state, self.task_id)}
                            """
                    ),
                    types.Part.from_text(
                        text=f"""
                            Gmail Query Information:
                            {{{ResearcherState.get_task_gmail_query_info(callback_context.state, self.task_id)}}}
                        """
                    ),
                ],
            )
        )

    def make_gmail_info(self, callback_context: CallbackContext) -> Optional[LlmResponse]:
        task_info_dict = callback_context.state.get(ResearcherState.task_info(self.task_id))
        task_info = ListenerProgramGmailSegment(**task_info_dict)

        current_time = datetime.datetime.now()

        start_date = current_time + datetime.timedelta(days=task_info.start_offset_days)
        end_date = current_time + datetime.timedelta(days=task_info.end_offset_days)

        query_info = {"query": f"{task_info.filter} after: {start_date.strftime('%Y/%m/%d')} before: {end_date.strftime('%Y/%m/%d')}"}

        callback_context.state[ResearcherState.task_gmail_query_info(self.task_id)] = query_info
        return None


class FormatAgent(Agent):
    task_id: str | int = Field(description="The task id")

    def __init__(self, task_id, **kwargs):
        super().__init__(
            task_id=task_id,
            model=GENERIC_MODEL,
            name=f"GmailResearchResultFormatAgent_{task_id}",
            instruction=f"""
            You are an agent that formats the answers from GmailResearchAgent_{task_id} agent.

            # Your task
            Read data from session state with key '{ResearcherState.research_result(task_id)}' and format'
            """,
            output_schema=GmailResearchResult,
            output_key=ResearcherState.research_result(task_id),
            **kwargs,
        )


class GmailResearchFlowAgent(SequentialAgent):
    task_id: str | int = Field(description="The task id")

    def __init__(self, task_id, **kwargs):
        super().__init__(
            task_id=task_id,
            name=f"GmailResearchFlowAgent_{task_id}",
            sub_agents=[
                GmailResearchAgent(task_id=task_id),
                FormatAgent(task_id=task_id),
            ],
            **kwargs,
        )
