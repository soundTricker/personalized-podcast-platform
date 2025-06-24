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

# global state keys
from typing import Any, Final, Type, final

from google.adk.sessions import State

from radio_station.model.base_model import BaseModel
from radio_station.model.listener import Listener
from radio_station.model.listener_program import ListenerProgram
from radio_station.model.listener_program_segment import ListenerProgramSegment
from radio_station.model.music_plan import MusicPlan
from radio_station.model.program_plan import ProgramPlan, SegmentPlan
from radio_station.model.radio_cast import RadioCast
from radio_station.model.talk_script import TalkScriptSegment

StateKey = Final[str]


def _get_model[T: BaseModel](t: Type[T], data: Any | None) -> T | None:
    if data is None:
        return None
    return t.model_validate(data)


def _get_model_list[T: BaseModel](t: Type[T], data: list[dict] | None) -> list[T]:
    if not data:
        return []
    return [t.model_validate(d) for d in data]


@final
class GlobalState:
    LISTENER: StateKey = "listener"
    LISTENER_PROGRAM: StateKey = "listener_program"
    RADIO_CASTS: StateKey = "radio_casts"
    LISTENER_PROGRAM_SEGMENTS: StateKey = "listener_program_segments"
    STATE: StateKey = "state"
    DRY_RUN = "dry_run"
    TALK_SCRIPT = "talk_script"

    @classmethod
    def get_listener_program(cls, state: State) -> ListenerProgram | None:
        return _get_model(ListenerProgram, state.get(cls.LISTENER_PROGRAM))

    @classmethod
    def get_radio_casts(cls, state: State | dict) -> list[RadioCast]:
        return _get_model_list(RadioCast, state.get(cls.RADIO_CASTS))

    @classmethod
    def get_listener_program_segments(cls, state: State) -> list[ListenerProgramSegment]:
        return _get_model_list(ListenerProgramSegment, state.get(cls.LISTENER_PROGRAM_SEGMENTS))

    @classmethod
    def get_listener(cls, state: State) -> Listener | None:
        return _get_model(Listener, state.get(cls.LISTENER))


@final
class ResearcherState:
    _PREFIX: StateKey = "research__"

    TASK_IDS: StateKey = f"{_PREFIX}task_ids"
    RESULTS: StateKey = f"{_PREFIX}results"

    @classmethod
    def task_info(cls, task_id):
        return f"{cls._PREFIX}{task_id}__task_info"

    @classmethod
    def get_task_info(cls, state: State | dict[str, Any], task_id: str):
        return state.get(cls.task_info(task_id), {})

    @classmethod
    def research_result(cls, task_id):
        return f"{cls._PREFIX}{task_id}__research_result"

    # RSS
    @classmethod
    def task_feed(cls, task_id):
        return f"{cls._PREFIX}{task_id}__feed"

    # Calendar
    @classmethod
    def task_calendar_info(cls, task_id):
        return f"{State.TEMP_PREFIX}{cls._PREFIX}{task_id}__calendar_info"

    @classmethod
    def task_gmail_query_info(cls, task_id):
        return f"{State.TEMP_PREFIX}{cls._PREFIX}{task_id}__gmail_query_info"

    @classmethod
    def get_task_gmail_query_info(cls, state: State, task_id: str):
        return state.get(cls.task_gmail_query_info(task_id), {})


@final
class ProgramPlannerState:
    _PREFIX: StateKey = "program__"
    PROGRAM_STRUCTURE: StateKey = f"{_PREFIX}structure"

    @classmethod
    def get_program_structure(cls, state: State | dict[str, Any]) -> ProgramPlan | None:
        return ProgramPlan(**state.get(cls.PROGRAM_STRUCTURE)) if state.get(cls.PROGRAM_STRUCTURE) else None


@final
class WriterState:
    _PREFIX: StateKey = "writer__"
    PREVIOUS_TALK_SCRIPT_SEGMENTS: StateKey = f"{_PREFIX}previous_talk_script_segments"
    TALK_SCRIPT_SEGMENTS: StateKey = f"{_PREFIX}talk_script_segments"
    STATE = f"{_PREFIX}state"

    @classmethod
    def task_continue_prev_segment(cls, task_id):
        return f"{State.TEMP_PREFIX}{cls._PREFIX}{task_id}__continue_prev_segment"

    @classmethod
    def task_radio_cast(cls, task_id):
        return f"{State.TEMP_PREFIX}{cls._PREFIX}{task_id}__radio_cast"

    @classmethod
    def task_segment(cls, task_id):
        return f"{State.TEMP_PREFIX}{cls._PREFIX}{task_id}__segment"

    @classmethod
    def task_previous_segment(cls, task_id):
        return f"{State.TEMP_PREFIX}{cls._PREFIX}{task_id}__prev_segment"

    @classmethod
    def task_next_segment(cls, task_id):
        return f"{State.TEMP_PREFIX}{cls._PREFIX}{task_id}__next_segment"

    @classmethod
    def task_research_results(cls, task_id):
        return f"{State.TEMP_PREFIX}{cls._PREFIX}{task_id}__research_results"

    @classmethod
    def task_talk_script_segment(cls, task_id):
        return f"{cls._PREFIX}{task_id}__talk_script_segment"

    @classmethod
    def task_revised_talk_scripts(cls, task_id):
        return f"{cls._PREFIX}{task_id}__revised_talk_scripts"

    @classmethod
    def task_criticism(cls, task_id):
        return f"{cls._PREFIX}{task_id}__criticism"

    @classmethod
    def get_continue_prev_segment(cls, state: State, task_id: str) -> TalkScriptSegment | None:
        return _get_model(TalkScriptSegment, state.get(cls.task_continue_prev_segment(task_id)))

    @classmethod
    def get_segment(cls, state: State, task_id) -> SegmentPlan | None:
        return _get_model(SegmentPlan, state.get(cls.task_segment(task_id)))

    @classmethod
    def get_previous_segment(cls, state: State, task_id) -> SegmentPlan | None:
        return _get_model(SegmentPlan, state.get(cls.task_previous_segment(task_id)))

    @classmethod
    def get_next_segment(cls, state: State, task_id) -> SegmentPlan | None:
        return _get_model(SegmentPlan, state.get(cls.task_next_segment(task_id)))

    @classmethod
    def get_talk_script_segment(cls, state: State, task_id) -> TalkScriptSegment | None:
        return _get_model(TalkScriptSegment, state.get(cls.task_talk_script_segment(task_id)))

    @classmethod
    def get_talk_script_segments(cls, state: State) -> list[TalkScriptSegment]:
        return _get_model_list(TalkScriptSegment, state.get(cls.TALK_SCRIPT_SEGMENTS))


@final
class ComposerState:
    _PREFIX: StateKey = "composer__"
    TASK_IDS: StateKey = f"{_PREFIX}task_ids"

    @classmethod
    def task_music_plan(cls, task_id):
        return f"{cls._PREFIX}{task_id}__music_plan"

    @classmethod
    def get_music_plan(cls, state: State | dict[str, Any], task_id: str):
        return _get_model(MusicPlan, state.get(cls.task_music_plan(task_id)))

    @classmethod
    def task_music_artifact_key(cls, task_id):
        return f"{cls._PREFIX}{task_id}__music.mp3"


@final
class RecorderState:
    _PREFIX: StateKey = "recorder__"
    TASK_STATE: StateKey = f"{_PREFIX}state"
    TEMP_TASK_IDS: StateKey = f"{_PREFIX}task_ids"
    TALK_SCRIPT: StateKey = f"{_PREFIX}talk_script"

    @classmethod
    def task_redio_cast(cls, task_id: str):
        return f"{cls._PREFIX}{task_id}__redio_cast"

    @classmethod
    def task_talk_script(cls, task_id: str):
        return f"{cls._PREFIX}{task_id}__talk_script"

    @classmethod
    def task_artifact_key(cls, task_id):
        return f"{cls._PREFIX}{task_id}__audio.mp3"


@final
class NewsLetterWriterState:
    _PREFIX: StateKey = "news_letter_writer__"
    CONTENTS: StateKey = f"{_PREFIX}contents"
