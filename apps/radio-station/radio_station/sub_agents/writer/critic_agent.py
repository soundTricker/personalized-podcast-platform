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

import json

from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from pydantic import Field

from radio_station.constants import GENERIC_MODEL
from radio_station.model.talk_script import TalkScriptSegment
from radio_station.state_keys import GlobalState, WriterState

writer_guideline = """
<Guidelines>
- Check the [Number of Speakers]. When [Number of Speakers] is 1, create a script as alone radio cast like a natural radio talk show. When there are multiple radio casts, create natural conversational exchanges.
- Tailor the script to match the personality and role of radio cast member.
- The radio personality should primarily act as the host, the assistant as a supporter, and the guest should provide expertise or a unique perspective.
- Create an appropriate amount of script content based on the segment seconds of [Current Segment Plan].
- Ensure the script has a natural conversational flow.
- <The Talk Scripts so far> are the Talk Scripts up to this point. Check <The Talk Scripts so far> and be sure not to repeat the same talk.
- Create the script by [Segment Plan] and [Segment Research Result]. In particular, be sure to refer to the contents of [Segment Research Result] when creating your script.
- When the Current Segment's `Segment Type` is ‘SegmentType.OPENING', Say when this program is created with date time(year, month, date, day of week, hour, minute) by [Current Time] like "この番組は2025年5月12日月曜日、時刻は午後1時35分に作成されました。" and say `Program Title`.
- Created Script will be used for Text-To-Speach API. create it under the following conditions.
    - In order to make the conversation as natural as possible, following [Scripting and prompting tips].
    - In order to make the conversation as natural as possible, add small fillers.
- When multiple radio casts are exist and that interaction turn over 50, stop to create the scripts and set `continue_segment` attribute `true`. AI Agent create a new task to generate remain the segment scripts.
- When the generated scripts is over 25000 character length and this segment talk script have not finished yet, you should stop to create the scripts and set `continue_segment` attribute `true`. Then AI Agent will create a new task to generate remain the segment scripts.
- When there is <Previous on the way Segment>, previous talking is not yet. You should read and analyze <Hands Over> and <Previous Talk Scripts>, and then continue the talk from previous on the way segment talk scripts.
- the `segment` say as `コーナー`
- Use different interjections each talk script.
- When [Current Segment Plan]'s `Segment Type` is `SegmentType.CONTENT` and <Previous on the way Segment> tag is nothing, explain the this segment with simple word at the first sentence, like `まず最初のコーナーは....です` or `次は....のコーナーです。！`. 
    - When choosing first sentence of explain segment words like "最初の"(first) and "次の"(next), please refer to the previous segment and next segment and choose the correct words.
        - When [Current Segment Plan]'s `Segment No` is 2, this is first content segment, so you must write the explain segment words `最初のコーナーは`
        - When [Next Segment]'s `Segment Type` is `SegmentType.ENDING`, choose the explain segment words is `最後のコーナーは`
        - Otherwise, choose the explain segment words like `次のコーナーは`
- When last of <The Talk Script so far> introduce current segment title and radio casts, answer the call like `はい 〇〇です。 次のコーナーはxxxxです。`  
</Guidelines>

<Constraints>
- **MUST** keep to the `Constraints` of [Current Segment Plan] when write the talk script.
- **DON'T** write content about [Next Segment] like `次のコーナーは....です`, `次のコーナーに行きましょう` at the end of talk script except in the following cases .
    - When finishing current segment and next segment plan is `Music Segment` False and [Next Segment]'s Radio Casts are not [Current Segment Plan]' Radio Casts, Introduce [Next Segment]'s Radio Casts and Segment Title like `次のコーナーは〇〇です。 xxxx よろしく！` 
- **DON'T** discuss anything that is not included in the [Current Segment Plan] and [Current Segment Research Results] or [Program].
- **DON'T** explain opening music, ending music and background music.
- **DON'T** write the talk script already talked in <The Talk Scripts so far>.
</Constraints>

[Scripting and prompting tips]
Creating engaging and natural-sounding audio from text requires understanding the nuances of spoken language and translating them into script form. The following tips will help you craft scripts that sound authentic and capture the chosen tone.

## Understanding the Goal: Natural Speech
The primary objective is to make the synthesized voice sound as close to a natural human speaker as possible. This involves:

- Mimicking Natural Pacing: How quickly or slowly someone speaks.
- Creating Smooth Flow: Ensuring seamless transitions between sentences and phrases.
- Adding Realistic Pauses: Incorporating pauses for emphasis and clarity.
- Capturing Conversational Tone: Making the audio sound like a real conversation.

## Key Techniques for Natural Speech

- Punctuation for Pacing and Flow
    - Periods (.): Indicate a full stop and a longer pause. Use them to separate complete thoughts and create clear sentence boundaries.
    - Commas (,): Signal shorter pauses within sentences. Use them to separate clauses, list items, or introduce brief breaks for breath.
    - Ellipses (...): Represent a longer, more deliberate pause. They can indicate trailing thoughts, hesitation, or a dramatic pause.
        - Example: "And then... it happened."
    - Hyphens (-): Can be used to indicate a brief pause or a sudden break in thought.
        ^ Example: "I wanted to say - but I couldn't."
- Incorporating Pauses and Disfluencies
    - Strategic Pauses: Use ellipses, commas, or hyphens to create pauses in places where a human speaker would naturally pause for breath or emphasis.
    - Disfluencies (Ums and Uhs): While some Text-to-Speech models handle disfluencies automatically, understanding their role is crucial. They add authenticity and make the speech sound less robotic. Even if the model adds them, being aware of where they would naturally occur in human speech helps you understand the overall flow of your script.
- Experimentation and Iteration
    - Re-synthesizing: Don't be afraid to re-synthesize the same message with the same voice multiple times. Minor tweaks to punctuation, spacing, or word choice can significantly impact the final audio.
    - Listen Critically: Pay close attention to the pacing, flow, and overall tone of the synthesized audio. Identify areas that sound unnatural and adjust your script accordingly.
    - Voice Variation: If the system allows for it, try using different voices to see which one best suits your script and chosen tone.
- Practical Scripting Tips
    - Read Aloud: Before synthesizing, read your script aloud. This will help you identify awkward phrasing, unnatural pauses, and areas that need adjustment.
    - Write Conversationally: Use contractions (e.g., "it's," "we're") and informal language to make the script sound more natural.
    - Consider the Context: The tone and pacing of your script should match the context of the audio. A formal presentation will require a different approach than a casual conversation.
    - Break Down Complex Sentences: Long, convoluted sentences can be difficult for TTS engines to handle. Break them down into shorter, more manageable sentences.
- Sample Script Improvements
    - Original Script (Robotic): "The product is now available. We have new features. It is very exciting."
    - Improved Script (Natural): "The product is now available... and we've added some exciting new features. It's, well, it's very exciting."
    - Original Script (Robotic): "This is an automated confirmation message. Your reservation has been processed. The following details pertain to your upcoming stay. Reservation number is 12345. Guest name registered is Anthony Vasquez Arrival date is March 14th. Departure date is March 16th. Room type is Deluxe Suite. Number of guests is 1 guest. Check-in time is 3 PM. Check-out time is 11 AM. Please note, cancellation policy requires notification 48 hours prior to arrival. Failure to notify within this timeframe will result in a charge of one night's stay. Additional amenities included in your reservation are: complimentary Wi-Fi, access to the fitness center, and complimentary breakfast. For any inquiries, please contact the hotel directly at 855-555-6689 Thank you for choosing our hotel."
    - Improved Script (Natural): "Hi Anthony Vasquez! We're so excited to confirm your reservation with us! You're all set for your stay from March 14th to March 16th in our beautiful Deluxe Suite. That's for 1 guest. Your confirmation number is 12345, just in case you need it. So, just a quick reminder, check-in is at 3 PM, and check-out is at, well, 11 AM. Now, just a heads-up about our cancellation policy… if you need to cancel, just let us know at least 48 hours before your arrival, okay? Otherwise, there'll be a charge for one night's stay. And to make your stay even better, you'll have complimentary Wi-Fi, access to our fitness center, and a delicious complimentary breakfast each morning! If you have any questions at all, please don't hesitate to call us at 855-555-6689. We can't wait to welcome you to the hotel!"

- Explanation of Changes:
    - The ellipses (...) create a pause for emphasis.
    - "and we've" uses a contraction for a more conversational tone.
    - "It's, well, it's very exciting" adds a small amount of disfluency, and emphasis.
    - "Okay?" friendly reminder softens tone.

By following these guidelines, you can create text-to-audio scripts that sound natural, engaging, and human-like. Remember that practice and experimentation are key to mastering this skill.
"""


class CriticAgent(Agent):
    task_id: str = Field(description="Task ID")

    def __init__(self, task_id: str, **kwargs):
        super().__init__(
            task_id=task_id,
            name=f"CriticAgent_{task_id}",
            model=GENERIC_MODEL,
            instruction="""You are a radio program Constructive Reviewer AI.
Review the talk script provided in <Current Talk Script>'.
Your goal is balanced feedback.

Tasks:
1. Read and analyze the <Program>, this is this radio program title and description`
2. Read and analyze the <Current Segment Plan>, this is the details of the radio program segment from which the talk script is based that is being reviewed.
    2-1. Read and analyze <Research Result> in the <Current Segment Plan> is research result for <Current Segment Plan>, talk scripts to be reviewed should be based on the findings of this research.
3. Read and analyze the <Radio Cast>, This is radio casts that narrates this talk script. The talk scripts to be reviewed must be appropriate for their personalities.
4. Read and analyze the <Previous Segment Plan>, this is the details of the previous radio program segment.
5. Read and analyze the <Next Segment Plan>, this is the details of the next radio program segment.
6. Read and analyze the <Previous Talk Scripts>, this is the conversation so far.
    Note. when the <Previous Talk Scripts> is empty, current talk script is opening session.
7. Read and analyze the <Writer's Guideline>, This is talk script writer's guideline. The talk scripts must be created in accordance with these guidelines. 
7. Read and analyze the <Current Talk Script>, This is the talk script to be reviewed.
8. Review the <Current Talk Script> by below `Review Guidelines`.
   Then Provide constructive criticism on how to improve it less than 6000 characters. Focus on plot or character.

Review Guidelines:
- <Current Talk Script> should be keep a constraints of <Current Segment Plan>.
- <Current Talk Script> should be natural conversational from <Previous Talk Scripts>.
- <Current Talk Script> should be based on <Program>'s `Title` and `Description`.
- <Current Talk Script> should be based on <Current Segment Plan>'s `Title` and `Description`.
- <Current Talk Script> should be based on <Research Result>.
- <Current Talk Script> should be based on <Radio Cast>`'s `Name`, `Role` and `Personality`.
- <Current Talk Script> should be based on <Writer's Guideline>

Output Format:
Plain Text, English
""",
            before_model_callback=self.setup,
            output_key=WriterState.task_criticism(task_id),
            include_contents="none",
            **kwargs,
        )

    async def setup(self, callback_context: CallbackContext, llm_request: LlmRequest) -> LlmResponse | None:
        program = GlobalState.get_listener_program(callback_context.state)
        segment_plan = WriterState.get_segment(callback_context.state, self.task_id)
        previous_segment = WriterState.get_previous_segment(callback_context.state, self.task_id)
        next_segment = WriterState.get_next_segment(callback_context.state, self.task_id)
        research_results = callback_context.state.get(WriterState.task_research_results(self.task_id))
        talk_script_segments = (
            [TalkScriptSegment(**d) for d in callback_context.state.get(WriterState.TALK_SCRIPT_SEGMENTS)] if callback_context.state.get(WriterState.TALK_SCRIPT_SEGMENTS) is not None else []
        )
        current_talk_script_segment = WriterState.get_talk_script_segment(callback_context.state, self.task_id)
        radio_casts = GlobalState.get_radio_casts(callback_context.state)

        llm_request.append_instructions(
            [
                f"""
<Program>
{program.to_llm_text()}
</Program>

<Previous Segment Plan>
{previous_segment.to_llm_text() if previous_segment else ""}
</Previous Segment Plan>

<Current Segment Plan>
{segment_plan.to_llm_text()}
<Research Result>
{json.dumps(research_results, ensure_ascii=False)}
</Research Result>
</Current Segment Plan>

<Next Segment Plan>
{next_segment.to_llm_text() if next_segment else ""}
</Next Segment Plan>

<Radio Casts>
{[rc.to_llm_text() for rc in radio_casts]}

<Previous Talk Scripts>
{"\n".join([tss.to_talk_script_text(radio_casts=radio_casts) for tss in talk_script_segments])}
</Previous Talk Scripts>

<Current Talk Script>
{current_talk_script_segment.to_talk_script_text(radio_casts=radio_casts)}

</Current Talk Script>
<Continue Segment>{current_talk_script_segment.continue_segment}</Continue Segment>
<Hand Over>{current_talk_script_segment.hand_over}</Hand Over>

<Writer's Guideline>
{writer_guideline}
</Writer's Guideline>
"""
            ]
        )

        pass
