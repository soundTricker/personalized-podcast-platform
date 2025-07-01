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
from typing import AsyncIterable
from zoneinfo import ZoneInfo

from fastapi import Depends, HTTPException, status
from google.adk.events import Event
from google.adk.sessions import Session
from pydantic_core._pydantic_core import ValidationError

from ppp.models.listener_program import ListenerProgram, ProgramStatus
from ppp.models.listener_program_segment import ListenerProgramSegment
from ppp.models.program_broadcast_history import ProgramBroadcastHistory, ProgramBroadcastHistoryStatus
from ppp.services.chat import ChatAPI, get_chat_api
from ppp.services.listener import ListenerService, get_listener_service
from ppp.services.listener_program import ListenerProgramService, get_listener_program_service
from ppp.services.listener_program_segment import ListenerProgramSegmentService, get_listener_program_segment_service
from ppp.services.program_broadcast_history import ProgramBroadcastHistoryService, get_program_broadcast_history_service
from ppp.services.radio_cast import RadioCastService, get_radio_cast_service

logger = logging.getLogger(__name__)


class RadioService:
    def __init__(
        self,
        listener_service: ListenerService,
        listener_program_service: ListenerProgramService,
        listener_program_segment_service: ListenerProgramSegmentService,
        program_broadcast_history_service: ProgramBroadcastHistoryService,
        radio_cast_service: RadioCastService,
        chat_api: ChatAPI,
    ):
        self.listener_service = listener_service
        self.listener_program_service = listener_program_service
        self.listener_program_segment_service = listener_program_segment_service
        self.program_broadcast_history_service = program_broadcast_history_service
        self.radio_cast_service = radio_cast_service
        self.chat_api = chat_api

    async def generate_podcast(self, listener_program_id: str, listener_id: str, history_id: str | None = None, dry_run=False):
        # Verify that the program belongs to the current user
        program = await self.listener_program_service.verify_program_ownership(listener_program_id, listener_id)
        if program is None:
            logger.error(f"Listener program with ID {listener_program_id} not found or you don't have permission to this program")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Listener program with ID {listener_program_id} not found or you don't have permission to this program")

        segments = await self.listener_program_segment_service.get_segments_by_program_id(program.id)
        if len(segments) == 0:
            logger.error(f"Listener program with ID {listener_program_id} is not configured with any segments")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Listener program with ID {listener_program_id} is not configured with any segments")

        radio_cast_id_set = {radio_cast_id for radio_cast_id in program.base_radio_cast_ids}

        for seg in segments:
            radio_cast_id_set.update(seg.override_radio_casts)

        radio_casts = await self.radio_cast_service.get_radio_casts_by_ids(list(radio_cast_id_set))

        if len(radio_casts) == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Radio Casts not found")

        if history_id is not None:
            history = await self.program_broadcast_history_service.get_broadcast_history_by_id(program.id, history_id)
            session = await self.chat_api.get_session(user_id=listener_id, session_id=history.session_id)

            if session:
                # check session state keys
                if not self._valid_session(session):
                    await self.chat_api.delete_session(user_id=listener_id, session_id=history.session_id)
                    session = None

            if session is None or (history.dry_run and dry_run):
                if session is not None:
                    await self.chat_api.delete_session(user_id=listener_id, session_id=history.session_id)
                session = await self.make_session(dry_run, listener_id, program, radio_casts, segments)
                history.session_id = session.id
                history.app_name = session.app_name
                history.news_letter_contents = None
                history.talk_script = None
            elif history.dry_run and not dry_run:
                state = session.state
                if session is not None:
                    await self.chat_api.delete_session(user_id=listener_id, session_id=history.session_id)
                session = await self.make_session(dry_run, listener_id, program, radio_casts, segments, origin_state=state)
                history.session_id = session.id
                history.app_name = session.app_name
                history.news_letter_contents = None
                history.talk_script = None

            if (history.dry_run and history.status == ProgramBroadcastHistoryStatus.GENERATING) or (
                not history.dry_run and not (history.status == ProgramBroadcastHistoryStatus.PREPARE or history.status == ProgramBroadcastHistoryStatus.FAILURE)
            ):
                logger.error(f"History with ID {history} is invalid state, dry_run:{history.dry_run}  status:{history.status}")
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"History with ID {history} already exists")
            history.status = ProgramBroadcastHistoryStatus.GENERATING
            history.dry_run = dry_run
            history.error = None
            await history.save()

        else:
            history, session = await self.make_history(listener_id, program, segments, radio_casts, dry_run=dry_run)

        if not self._valid_session(session):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid session state: {session.state}")

        return self.event_generator(listener_id, session, history, program, segments, dry_run=dry_run)

    async def generate_podcast_sse(self, listener_program_id: str, listener_id: str, history_id: str | None = None, dry_run=False):
        async for event in await self.generate_podcast(listener_program_id, listener_id, history_id, dry_run=dry_run):
            yield f"data: {event.model_dump_json(exclude_unset=True, exclude_none=True, by_alias=True)}\n\n"

    def _valid_session(self, session):
        return all([key in session.state for key in ["listener", "listener_program", "radio_casts", "listener_program_segments"]])

    async def make_history(self, listener_id, program, segments, radio_casts, status=ProgramBroadcastHistoryStatus.GENERATING, dry_run=False):
        session = await self.make_session(dry_run, listener_id, program, radio_casts, segments)
        history = await self.program_broadcast_history_service.create_broadcast_history(
            program_id=program.id, no=program.number_of_broadcast, app_name=session.app_name, listener_id=listener_id, session_id=session.id, status=status, dry_run=dry_run
        )
        return history, session

    async def make_session(self, dry_run, listener_id, program, radio_casts, segments, origin_state: dict | None = None):
        listener = await self.listener_service.get_listener_by_id(listener_id)
        listener_program = program.model_dump(mode="json")
        listener_program["base_radio_casts"] = [r.model_dump(mode="json") for r in radio_casts if r.id in program.base_radio_cast_ids]
        listener_program_segments = []
        for s in segments:
            sd = s.model_dump(mode="json")
            sd["override_radio_casts"] = [r.model_dump(mode="json") for r in radio_casts if r.id in s.override_radio_casts]
            listener_program_segments.append(sd)

        if origin_state is not None:
            state = origin_state.copy()
            del state["dry_run"]
        else:
            state = {
                "listener": listener.model_dump(mode="json"),
                "listener_program": listener_program,
                "radio_casts": [r.model_dump(mode="json") for r in radio_casts],
                "listener_program_segments": listener_program_segments,
            }

        if dry_run:
            state["dry_run"] = True

        session = await self.chat_api.create_session(
            user_id=listener.id,
            state=state,
        )

        logger.info(f"Create new session session_id:{session.id} app_name:{session.app_name} state:{session.state}")

        return session

    def __handle_error(self, event_dict: dict) -> Event | None:
        if "error" in event_dict:
            if isinstance(event_dict["error"], dict) and "message" in event_dict["error"]:
                return Event(author="system", error_message=event_dict["error"]["message"])
            else:
                return Event(author="system", error_message=str(event_dict["error"]))
        return None

    async def event_generator(
        self, listener_id: str, session: Session, history: ProgramBroadcastHistory, program: ListenerProgram, segments: list[ListenerProgramSegment], dry_run=False
    ) -> AsyncIterable[Event]:
        try:
            await history.reload()
            async for event_dict in self.chat_api.async_stream_query(message="generate radio", user_id=listener_id, session_id=session.id):
                logger.debug(f"event_dict: {event_dict} ")

                if err := self.__handle_error(event_dict):
                    history.status = ProgramBroadcastHistoryStatus.FAILURE
                    history.error = json.dumps(event_dict)
                    await history.save()
                    yield err
                    return

                try:
                    event = Event.model_validate(event_dict)
                except ValidationError as e:
                    history.status = ProgramBroadcastHistoryStatus.FAILURE
                    history.error = json.dumps(event_dict)
                    await history.save()
                    yield Event(author="system", error_message=f"Got Error: {e}, {event_dict}", error_code="500")
                    return

                if event.error_message or event.error_code:
                    history.status = ProgramBroadcastHistoryStatus.FAILURE
                    history.error = json.dumps(event_dict)
                    await history.save()
                    yield event
                    return

                yield event

            yield Event(author="done", invocation_id="done")

            new_session = await self.chat_api.get_session(user_id=listener_id, session_id=session.id)
            await history.reload()
            history.status = ProgramBroadcastHistoryStatus.SUCCESS
            if not dry_run:
                history.artifact_id = "audio.mp3"
                artifact = await self.chat_api.load_artifact(user_id=listener_id, session_id=new_session.id, artifact_id=history.artifact_id)
                history.size = len(artifact.inline_data.data)

            history.news_letter_contents = new_session.state.get("news_letter_writer__contents")
            history.talk_script = new_session.state.get("talk_script")
            await history.save()

            if dry_run:
                return

            segment_dicts = new_session.state.get("listener_program_segments")

            for segment in segment_dicts:
                seg = next((seg for seg in segments if seg.id == segment["id"]))
                await seg.reload()
                seg.override_radio_casts = [cast["id"] for cast in segment["override_radio_casts"]]
                seg.last_read_timestamp = segment["last_read_timestamp"]
                await seg.save()

            await program.reload()

            if program.number_of_broadcast == 0:
                programs = await self.listener_program_service.get_listener_programs_by_listener_id(listener_id)

                active_programs = [p for p in programs if p.status == ProgramStatus.ACTIVE and p.id != program.id]
                if len(active_programs) > 0:
                    program.status = ProgramStatus.PAUSE
                else:
                    program.status = ProgramStatus.ACTIVE

            program.number_of_broadcast += 1
            program.last_broadcasted_At = datetime.datetime.now(tz=ZoneInfo("Asia/Tokyo"))
            await program.save()

        except Exception as e:
            logger.exception("Error in event_generator: %s", e)

            await history.reload()
            history.status = ProgramBroadcastHistoryStatus.FAILURE
            history.error = str(e)
            await history.save()

            # You might want to yield an error event here
            yield Event(author="system", error_message=str(e))
            return


def get_radio_service(
    listener_service: ListenerService = Depends(get_listener_service),
    listener_program_service: ListenerProgramService = Depends(get_listener_program_service),
    listener_program_segment_service: ListenerProgramSegmentService = Depends(get_listener_program_segment_service),
    program_broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    radio_cast_service: RadioCastService = Depends(get_radio_cast_service),
    chat_api: ChatAPI = Depends(get_chat_api),
) -> RadioService:
    return RadioService(
        listener_service=listener_service,
        listener_program_service=listener_program_service,
        listener_program_segment_service=listener_program_segment_service,
        program_broadcast_history_service=program_broadcast_history_service,
        radio_cast_service=radio_cast_service,
        chat_api=chat_api,
    )
