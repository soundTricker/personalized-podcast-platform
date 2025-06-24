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

from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types
from pydantic import Field

from radio_station.constants import GENERIC_MODEL
from radio_station.model.base_model import BaseModel
from radio_station.model.talk_script import TalkScript, TalkScriptSegment
from radio_station.state_keys import WriterState

logger = logging.getLogger(__name__)

class RevisedTalkScripts(BaseModel):
    scripts: list[TalkScript] = Field(description="Revised Talk Script List", default_factory=lambda : [])

class ReviserAgent(Agent):
    task_id: str = Field(description="Task ID")
    def __init__(self, task_id):
        super().__init__(
            task_id=task_id,
            name=f"ReviserAgent_{task_id}",
            model=GENERIC_MODEL,
            instruction=f"""You are a radio program's talk script reviser. 
            Revise the talk script(`scripts` property) provided in <Talk Scripts>', based on the criticism in <Criticism>.
            Output only the revised talk script. You can only change `content` property of the output schema.

<Criticism>
{{{WriterState.task_criticism(task_id)}}}
</Criticism>

<Talk Scripts>
{{{WriterState.task_talk_script_segment(task_id)}}}
</Talk Scripts>
""",
            output_schema=RevisedTalkScripts,
            output_key=WriterState.task_revised_talk_scripts(task_id),
            after_agent_callback=self.update_script,
        )

    async def update_script(self, callback_context: CallbackContext) -> types.Content | None:

        talk_script_dicts = callback_context.state.get(WriterState.task_talk_script_segment(self.task_id))
        revised_talk_script_dict = callback_context.state.get(WriterState.task_revised_talk_scripts(self.task_id))
        talk_script_segment = TalkScriptSegment(**talk_script_dicts)
        origin = talk_script_segment.to_talk_script_text()
        talk_script_dicts["scripts"] = revised_talk_script_dict["scripts"]
        new_talk_script_segment = TalkScriptSegment(**talk_script_dicts)
        revised = new_talk_script_segment.to_talk_script_text()

        callback_context.state.update({WriterState.task_talk_script_segment(self.task_id): talk_script_dicts})

        criticism = callback_context.state.get(WriterState.task_criticism(self.task_id))
        logger.info(f"criticism: {criticism}")
        logger.info(f"origin: {origin}")
        logger.info(f"revised: {revised}")
