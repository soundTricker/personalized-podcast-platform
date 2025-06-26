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
import os
from typing import Optional

import google.auth
from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ClientCreds, UserCreds
from aiogoogle.excs import AiogoogleError
from google.adk.agents import Agent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.planners import BuiltInPlanner
from google.adk.tools import ToolContext
from google.auth.transport.requests import Request
from google.genai import types
from google.oauth2.credentials import Credentials
from pydantic import Field

from radio_station.constants import THINKING_MODEL, GoogleApiScope
from radio_station.model.base_model import BaseModel
from radio_station.model.listener_program_segment import ListenerProgramCalendarSegment
from radio_station.state_keys import GlobalState, ResearcherState
from radio_station.tools.geolocation_tool import geolocation_tool
from radio_station.tools.weather_tool import weather_tool
from radio_station.utils.crypto import decrypt

logger = logging.getLogger(__name__)


class CalendarEvent(BaseModel):
    summary: str = Field(description="Event summary")
    description: str | None = Field(description="Event description", default=None)
    start_time: str = Field(description="Event start time in ISO format")
    end_time: str = Field(description="Event end time in ISO format")
    location: str | None = Field(description="Event location", default=None)
    weather_summary: str | None = Field(description="This event date and location's weather summary if available", default=None)


class CalendarResearchResult(BaseModel):
    summary: str = Field(description="Summary of the calendar events")
    events: list[CalendarEvent] = Field(description="List of calendar events")


async def list_calendar_events(
    calendar_id: str,
    start_time: str,
    end_time: str,
    limit: int,
    tool_context: ToolContext,
) -> list[dict]:
    """
    Search for calendar events.

    Example:

        flights = get_calendar_events(
            calendar_id='joedoe@gmail.com',
            start_time='2024-09-17T06:00:00',
            end_time='2024-09-17T12:00:00',
            limit=10
        )
        # Returns up to 10 calendar events between 6:00 AM and 12:00 PM on
        September 17, 2024.

    Args:
        calendar_id (str|None): the calendar ID to search for events, if it set None, calendar_id will be 'primary', which means the primary calendar.
        start_time (str): The start of the time range (format is YYYY-MM-DDTHH:MM:SS).
        end_time (str): The end of the time range (format is YYYY-MM-DDTHH:MM:SS).
        limit (int): The maximum number of results to return.

    Returns:
        list[dict]: A list of events that match the search criteria.
    """
    creds = None

    # Check if the tokes were already in the session state, which means the user
    # has already gone through the OAuth flow and successfully authenticated and
    # authorized the tool to access their calendar.
    if "calendar_tool_tokens" in tool_context.state:
        creds = Credentials.from_authorized_user_info(tool_context.state["calendar_tool_tokens"], ["https://www.googleapis.com/auth/calendar"])
    elif (
        (listener := GlobalState.get_listener(tool_context.state))
        and GoogleApiScope.CalendarReadOnly in listener.scopes
        and listener.encrypted_google_access_token
        and listener.encrypted_google_refresh_token
    ):
        creds = UserCreds(access_token=decrypt(listener.encrypted_google_access_token), refresh_token=decrypt(listener.encrypted_google_refresh_token))

    if not creds or not creds.valid:
        # If the access token is expired, refresh it with the refresh token.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds, _ = google.auth.default()
        tool_context.state["calendar_tool_tokens"] = json.loads(creds.to_json())

    try:
        async with Aiogoogle(user_creds=creds, client_creds=ClientCreds(client_id=os.getenv("GOOGLE_CLIENT_ID"), client_secret=os.getenv("GOOGLE_CLIENT_SECRET"))) as aiogoogle_client:
            service = await aiogoogle_client.discover("calendar", "v3")
            request = service.events.list(
                calendarId=calendar_id,
                timeMin=start_time + "Z" if start_time else None,
                timeMax=end_time + "Z" if end_time else None,
                maxResults=limit,
                singleEvents=True,
                orderBy="startTime",
            )
            response = await aiogoogle_client.as_user(request)
            events = response.get("items", [])
            return events
    except AiogoogleError as e:
        logger.exception(f"Got error err:{e}")
        return []


class CalendarResearchAgent(Agent):
    task_id: str | int = Field(description="The task id")
    task: ListenerProgramCalendarSegment = Field(description="my task")

    def __init__(self, task_id: str, task: ListenerProgramCalendarSegment, **kwargs):
        # calendar_tool_set = CalendarToolset(os.getenv("GOOGLE_CLIENT_ID"), os.getenv("GOOGLE_CLIENT_SECRET"))

        super().__init__(
            task_id=task_id,
            task=task,
            model=THINKING_MODEL,
            name=f"CalendarResearchAgent_{task_id}",
            instruction=f"""
                You are an AI Calendar Schedule Summarization Assistant specializing in creating radio program segments.

                Your tasks are:
                1. Fetch calendar events for a specified period by using the list_calendar_events tool
                    - Searching period and calendar id in `Calendar Information`
                    - You must use list_calendar_events tool to fetch calendar events.
                2. Process each events
                    - When the event has a location.
                        2-1. search geolocation by using `get_geolocation_for_place` tool.
                        2-2. If geolocation can be obtained, Get a weather for event date and geolocation.
                3. Create a summary of the events within the target period based on Task Info.
                    - When Calendar Information is not found or got error, please return JSON Object like `{{"summary": "No event found in this schedule."}}`
                    - When weather can be obtained, please add weather information to summary.
                    
                Constrains:
                - **USE** the list_calendar_events tool **ONLY ONCE**.

                Output Format:
                JSON, Japanese.

                Output Schema:
                Make a JSON with below attributes.

                - 'summary': A short summary of the calendar events.
                - 'events': A list of events, each with:
                    - 'summary': A short summary of the event.
                    - 'description': A detailed description of the event (if available).
                    - 'start_time': The start time of the event in ISO format.
                    - 'end_time': The end time of the event in ISO format.
                    - 'weather_summary': This event date and location's weather summary if available

                Calendar Information:
                {{{ResearcherState.task_calendar_info(task_id)}}}
            """,
            tools=[list_calendar_events, geolocation_tool, weather_tool],
            generate_content_config=types.GenerateContentConfig(
                max_output_tokens=24000,
                frequency_penalty=-2.0,
            ),
            before_model_callback=self.insert_task_info,
            before_agent_callback=self.make_calendar_info,
            after_agent_callback=self.log_content,
            output_key=ResearcherState.research_result(task_id),
            include_contents="none",
            **kwargs,
        )

    def log_content(self, callback_context: CallbackContext) -> Optional[LlmResponse]:
        research_results = callback_context.state[ResearcherState.research_result(self.task_id)]
        logger.info(f"calendar result result: {research_results}")

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
                    )
                ],
            )
        )

    def make_calendar_info(self, callback_context: CallbackContext) -> Optional[LlmResponse]:
        current_time = datetime.datetime.now()

        start_date = current_time + datetime.timedelta(days=self.task.start_offset_days)
        end_date = current_time + datetime.timedelta(days=self.task.end_offset_days)

        calendar_info = {
            "calendar_id": self.task.calendar_id,
            "time_min": start_date.isoformat(),
            "time_max": end_date.isoformat(),
        }

        callback_context.state[ResearcherState.task_calendar_info(self.task_id)] = calendar_info


class FormatAgent(Agent):
    task_id: str | int = Field(description="The task id")

    def __init__(self, task_id, **kwargs):
        super().__init__(
            task_id=task_id,
            model=THINKING_MODEL,
            name=f"CalendarResearchResultFormatAgent_{task_id}",
            instruction=f"""
            You are an agent that formats the answers from CalendarResearchAgent_{task_id} agent.

            # Your task
            Read data from session state with key '{ResearcherState.research_result(task_id)}' and format'
            """,
            planner=BuiltInPlanner(thinking_config=types.ThinkingConfig(thinking_budget=0, include_thoughts=False)),
            output_schema=CalendarResearchResult,
            output_key=ResearcherState.research_result(task_id),
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
            **kwargs,
        )


class CalendarResearchFlowAgent(SequentialAgent):
    task_id: str | int = Field(description="The task id")
    task: ListenerProgramCalendarSegment = Field(description="my task")

    def __init__(self, task_id, task: ListenerProgramCalendarSegment, **kwargs):
        super().__init__(
            task_id=task_id,
            task=task,
            name=f"CalendarResearchFlowAgent_{task_id}",
            sub_agents=[
                CalendarResearchAgent(task_id=task_id, task=task),
                FormatAgent(task_id=task_id),
            ],
            **kwargs,
        )
