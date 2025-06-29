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

import asyncio
import io
import logging
import math
import os
from typing import AsyncGenerator, Optional

import websockets
from google import genai
from google.adk import Agent
from google.adk.agents import BaseAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.adk.models import LlmRequest, LlmResponse
from google.genai import types
from google.genai.live_music import AsyncMusicSession
from pydantic import Field
from pydub import AudioSegment

from radio_station.constants import GENERIC_MODEL, THINKING_MODEL
from radio_station.model.music_plan import MusicPlan
from radio_station.state_keys import ComposerState
from radio_station.sub_agents.composer.tools import generate_music_tool
from radio_station.utils.audio import export_wav

API_KEY = os.environ.get("GEMINI_API_KEY")

BUFFER_SECONDS = 1
MODEL = "models/lyria-realtime-exp"

logger = logging.getLogger(__name__)


class MusicPlanningAgent(Agent):
    task_id: str = Field(description="The task id")
    music_plan: str = Field(description="The music plan")
    seconds: int | float = Field(description="The number of seconds")

    def __init__(self, task_id: str, music_plan: str, seconds: int | float):
        super().__init__(
            task_id=task_id,
            music_plan=music_plan,
            seconds=seconds,
            name=f"MusicPlanningAgent_{task_id}",
            model=THINKING_MODEL,
            description="An AI music Composer Agent.",
            instruction="""
You are an AI Composer agent that create parameters for Lyria RealTime based on provided music plan.
The music plan can be very abstract, your role is to create specific prompts,music plan and chord progression even if the music plan is abstract.

Your task is to:
1. Read a [Music Plan] and [Music Duration Second] to understand what music to create.
2. Read a [Parameter Guide] to create good parameters for Lyria RealTime.
3. Create a parameters.
    1. Decide Main Music Genre
        - use adjectives describing with genre.
        - the main music genre always is included in prompt like {"text": "Upbeat Progressive House", "weight": 2.0}
        - about music genre, reference "### Prompt Guide for Lyria RealTime". 
    2. Decide Main Mood/Description
        - the main mood/description almost is included in prompt like {"text": "Driving", "weight": 1.0}, {"text": "Upbeat", "weight": 1.0}, {"text": "Danceable", "weight": 1.0}
        - about Mood/Description, reference "### Prompt Guide for Lyria RealTime".
    3. Decide Instruments
        - about Instruments, reference "### Prompt Guide for Lyria RealTime".
        - When instruments change each stanza,
    4. Make stanzas.
        - Note that the model transitions can be a bit abrupt when drastically changing the prompts so it's recommended to implement some kind of cross-fading by sending intermediate weight values to the model.
        - Vary the prompts appropriately to keep the music from becoming monotonous.
4. Save the parameters to the session state with `music_plan` key

[Output Format]
JSON

[Parameter Guide]
## Lyria RealTime Music Generation Parameters

### Updating the Configuration

You can update music generation parameters in real-time. It's crucial to understand that you **cannot update individual parameters**. Instead, you **must set the entire configuration** each time. If you only provide values for a few fields, the others will revert to their default values.

For significant changes, such as modifying the **BPM** or the **scale**, you'll also need to explicitly tell the model to reset its context by calling `session.reset_context()`. This ensures the new configuration is fully applied. While this won't stop the audio stream, it will result in a noticeable "hard transition" in the music. For other parameters, a context reset isn't necessary.
---

### Prompt Guide for Lyria RealTime

Lyria RealTime responds to a wide range of textual prompts. Here's a non-exhaustive list of categories and examples you can use:

* **Instruments**: `303 Acid Bass`, `808 Hip Hop Beat`, `Accordion`, `Alto Saxophone`, `Bagpipes`, `Balalaika Ensemble`, `Banjo`, `Bass Clarinet`, `Bongos`, `Boomy Bass`, `Bouzouki`, `Buchla Synths`, `Cello`, `Charango`, `Clavichord`, `Conga Drums`, `Didgeridoo`, `Dirty Synths`, `Djembe`, `Drumline`, `Dulcimer`, `Fiddle`, `Flamenco Guitar`, `Funk Drums`, `Glockenspiel`, `Guitar`, `Hang Drum`, `Harmonica`, `Harp`, `Harpsichord`, `Hurdy-gurdy`, `Kalimba`, `Koto`, `Lyre`, `Mandolin`, `Maracas`, `Marimba`, `Mbira`, `Mellotron`, `Metallic Twang`, `Moog Oscillations`, `Ocarina`, `Persian Tar`, `Pipa`, `Precision Bass`, `Ragtime Piano`, `Rhodes Piano`, `Shamisen`, `Shredding Guitar`, `Sitar`, `Slide Guitar`, `Smooth Pianos`, `Spacey Synths`, `Steel Drum`, `Synth Pads`, `Tabla`, `TR-909 Drum Machine`, `Trumpet`, `Tuba`, `Vibraphone`, `Viola Ensemble`, `Warm Acoustic Guitar`, `Woodwinds`, ...
* **Music Genre**: `Acid Jazz`, `Afrobeat`, `Alternative Country`, `Baroque`, `Bengal Baul`, `Bhangra`, `Bluegrass`, `Blues Rock`, `Bossa Nova`, `Breakbeat`, `Celtic Folk`, `Chillout`, `Chiptune`, `Classic Rock`, `Contemporary R&B`, `Cumbia`, `Deep House`, `Disco Funk`, `Drum & Bass`, `Dubstep`, `EDM`, `Electro Swing`, `Funk Metal`, `G-funk`, `Garage Rock`, `Glitch Hop`, `Grime`, `Hyperpop`, `Indian Classical`, `Indie Electronic`, `Indie Folk`, `Indie Pop`, `Irish Folk`, `Jam Band`, `Jamaican Dub`, `Jazz Fusion`, `Latin Jazz`, `Lo-Fi Hip Hop`, `Marching Band`, `Merengue`, `New Jack Swing`, `Minimal Techno`, `Moombahton`, `Neo-Soul`, `Orchestral Score`, `Piano Ballad`, `Polka`, `Post-Punk`, `60s Psychedelic Rock`, `Psytrance`, `R&B`, `Reggae`, `Reggaeton`, `Renaissance Music`, `Salsa`, `Shoegaze`, `Ska`, `Surf Rock`, `Synthpop`, `Techno`, `Trance`, `Trap Beat`, `Trip Hop`, `Vaporwave`, `Witch house`, ...
* **Mood/Description**: `Acoustic Instruments`, `Ambient`, `Bright Tones`, `Chill`, `Crunchy Distortion`, `Danceable`, `Dreamy`, `Echo`, `Emotional`, `Ethereal Ambience`, `Experimental`, `Fat Beats`, `Funky`, `Glitchy Effects`, `Huge Drop`, `Live Performance`, `Lo-fi`, `Ominous Drone`, `Psychedelic`, `Rich Orchestration`, `Saturated Tones`, `Subdued Melody`, `Sustained Chords`, `Swirling Phasers`, `Tight Groove`, `Unsettling`, `Upbeat`, `Virtuoso`, `Weird Noises`, ...

These examples are just a starting point; Lyria RealTime can do much more. Feel free to experiment with your own creative prompts!

---

### Best Practices for Client Applications

To ensure a smooth user experience with Lyria RealTime:

* **Robust Audio Buffering**: Your client application should implement strong audio buffering. This helps manage network jitter and slight variations in generation latency, ensuring continuous, uninterrupted playback.
* **Effective Prompting**:
    * **Be Descriptive**: Use adjectives and detailed descriptions for mood, genre, and instrumentation. The more specific your prompt, the better the output.
    * **Iterate and Steer Gradually**: Instead of drastically changing a prompt, try adding or modifying elements incrementally. This allows the music to morph more smoothly over time.
    * **Experiment with `WeightedPrompt`**: This feature lets you influence how strongly a new prompt affects the ongoing music generation. Adjusting its weight can fine-tune the transition and blend of musical ideas.

---

#### Controls

Music generation can be influenced in real-time by sending messages containing:

* **`WeightedPrompt`**: A text string describing a musical idea, genre, instrument, mood, or characteristic. You can supply multiple prompts to blend influences. Refer to the "Prompt Guide" above for examples and best practices on effective prompting.
* **`MusicGenerationConfig`**: This configuration influences the characteristics of the output audio. Its parameters include:
    * **`bpm`**: (`int`) Range: `[60, 200]`. Sets the Beats Per Minute for the generated music. A `reset_context()` call is required for the model to take this new BPM into account.
    * **`scale`**: (`Enum`) Sets the musical scale (Key and Mode) for the generation. You must use the `Scale` enum values provided by the SDK. Like `bpm`, changing the scale requires a `reset_context()` call to take effect.

---

### Scale Enum Values

Here are all the musical scale values that the model can accept:

| Enum Value                | Scale / Key           |
| :------------------------ | :-------------------- |
| `C_MAJOR_A_MINOR`         | C major / A minor     |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | D♭ major / B♭ minor   |
| `D_MAJOR_B_MINOR`         | D major / B minor     |
| `E_FLAT_MAJOR_C_MINOR`    | E♭ major / C minor    |
| `E_MAJOR_D_FLAT_MINOR`    | E major / C♯/D♭ minor |
| `F_MAJOR_D_MINOR`         | F major / D minor     |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | G♭ major / E♭ minor   |
| `G_MAJOR_E_MINOR`         | G major / E minor     |
| `A_FLAT_MAJOR_F_MINOR`    | A♭ major / F minor    |
| `A_MAJOR_G_FLAT_MINOR`    | A major / F♯/G♭ minor |
| `B_FLAT_MAJOR_G_MINOR`    | B♭ major / G minor    |
| `B_MAJOR_A_FLAT_MINOR`    | B major / G♯/A♭ minor |
| `SCALE_UNSPECIFIED`       | Default / The model decides |

The model can guide the notes that are played, but it doesn't distinguish between relative keys. Thus, each enum value corresponds to both the relative major and minor key. For example, `C_MAJOR_A_MINOR` corresponds to all the white keys of a piano, and `F_MAJOR_D_MINOR` would include all the white keys except B flat.

---

### Limitations

* **Instrumental Only**: The model exclusively generates instrumental music; it does not produce vocals.
* **Safety Filters**: Prompts are checked by internal safety filters. If a prompt triggers these filters, it will be ignored, and an explanation will be provided in the output's `filtered_prompt` field.
* **Watermarking**: All output audio is automatically watermarked for identification purposes, aligning with our Responsible AI principles.


### Stanza

There should be no abrupt changes in prompts between stanzas.

Output Example
<Bad Example>
There are abrupt changes between stanzas.


{"title": "test", "stanzas" [
{
"prompts": [{"text": "deep house", "weight": 1}, {"text": "808 beat", "weight": 1}], seconds: 30

},
{
"prompts": [{"text": "hip hop", "weight": 1}, {"text": "Buchla Synths", "weight": 1}], seconds: 30
},
]}
</Bad Example>
<Good Example>
If you want to change it, change the weight parameter gradually for small reasons and crossfade

{"title": "test", "stanzas" [
{
"prompts": [{"text": "deep house", "weight": 1}, {"text": "808 beat", "weight": 1}], seconds: 20
},
{
"prompts": [{"text": "deep house", "weight": 0.8}, {"text": "808 beat", "weight": 0.8}, {"text": "hip hop", "weight": 0.2}, {"text": "Buchla Synths", "weight": 0.2}], seconds: 5 
}, 
{ 
"prompts": [{"text": "deep house", "weight": 0.6}, {"text": "808 beat", "weight": 0.6}, {"text": "hip hop", "weight": 0.4}, {"text": "Buchla Synths", "weight": 0.4}], seconds: 5 
}, 
{ 
"prompts": [{"text": "deep house", "weight": 0.4}, {"text": "808 beat", "weight": 0.4}, {"text": "hip hop", "weight": 0.6}, {"text": "Buchla Synths", "weight": 0.6}], seconds: 5 
}, 
{ 
"prompts": [{"text": "deep house", "weight": 0.2}, {"text": "808 beat", "weight": 0.2}, {"text": "hip hop", "weight": 0.8}, {"text": "Buchla Synths", "weight": 0.8}], seconds: 5 
}, 
{ 
"prompts": [{"text": "hip hop", "weight": 1}, {"text": "Buchla Synths", "weight": 1}], seconds: 20 
},
]}
</Good Example>

```
    """,
            before_agent_callback=self.check_invocation,
            before_model_callback=self.insert_user_content,
            output_schema=MusicPlan,
            output_key=ComposerState.task_music_plan(task_id),
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
            include_contents="none",
        )

    def check_invocation(self, callback_context: CallbackContext) -> Optional[types.Content]:
        if ComposerState.task_music_plan(self.task_id) in callback_context.state:
            return types.Content(parts=[types.Part.from_text(text="already finished this task")])
        return None

    def insert_user_content(self, callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
        llm_request.contents.append(
            types.UserContent(
                parts=[
                    types.Part.from_text(
                        text=f"""
[Your Task ID]
{self.task_id}

[Music Plan]
{self.music_plan}

[Music Duration Second]
{self.seconds} sec
"""
                    )
                ]
            )
        )


class ComposerAgent(BaseAgent):
    task_id: str = Field(description="The unique identifier for the composer task.")
    music_plan: str = Field(description="The music plan")
    seconds: int | float = Field(description="The number of seconds")
    audio_byte_array: bytearray = bytearray()

    def __init__(self, task_id: str, music_plan: str, seconds: int | float, **kwargs):
        super().__init__(
            name=f"ComposerAgent_{task_id}",
            task_id=task_id,
            music_plan=music_plan,
            seconds=seconds,
            **kwargs,
        )

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        if ComposerState.task_music_artifact_key(task_id=self.task_id) in ctx.artifact_service.list_artifact_keys(app_name=ctx.app_name, user_id=ctx.user_id, session_id=ctx.session.id):
            yield Event(invocation_id=ctx.invocation_id, content=types.Content(parts=[types.Part(text=f"Already generated music for: {self.task_id}")]), author=self.name)

        agent = MusicPlanningAgent(task_id=self.task_id, music_plan=self.music_plan, seconds=self.seconds)
        async for event in agent.run_async(ctx):
            yield event

        yield Event(invocation_id=ctx.invocation_id, content=await self.generate_music(ctx), author=self.name)

    async def generate_music(self, ctx: InvocationContext) -> types.Content | None:
        client = genai.Client(vertexai=False, api_key=API_KEY, http_options={"api_version": "v1alpha"})

        music_plan = ComposerState.get_music_plan(ctx.session.state, self.task_id)

        initial = True

        async def receive_audio(session: AsyncMusicSession):
            """Example background task to process incoming audio."""

            chunks_count = 0
            logger.info("start receive music")

            try:
                async for message in session.receive():
                    chunks_count += 1
                    if chunks_count == 1:
                        # Introduce a delay before starting playback to have a buffer for network jitter.
                        await asyncio.sleep(BUFFER_SECONDS)

                    if message.server_content:
                        audio_data = message.server_content.audio_chunks[0].data
                        self.audio_byte_array.extend(audio_data)
                    elif message.filtered_prompt:
                        logger.info(f"Prompt was filtered out: {message.filtered_prompt}")
                    else:
                        logger.info(f"Unknown error occured with message: {message}")

                    await asyncio.sleep(10**-12)
            except websockets.exceptions.ConnectionClosedOK:
                # nothing to do
                pass
            except Exception as e:
                logger.exception(f"got error {e}")

        prev_config = None
        async with (
            asyncio.TaskGroup() as tg,
            client.aio.live.music.connect(model="models/lyria-realtime-exp") as session,
        ):
            # Set up task to receive server messages.
            tg.create_task(receive_audio(session))
            for stanza in music_plan.stanzas:
                logger.info(f"next stanza {stanza}")
                # Send initial prompts and config
                await session.set_weighted_prompts(prompts=stanza.to_gemini_prompts())
                if prev_config != stanza.config:
                    logger.info(f"set music config {stanza.config}")
                    await session.set_music_generation_config(config=stanza.to_gemini_config())
                    await session.reset_context()

                prev_config = stanza.config
                if initial:
                    # Start streaming music
                    logger.info("start session")
                    await session.play()
                    initial = False
                logger.info(f"sleep {stanza.seconds}")
                await asyncio.sleep(stanza.seconds)

            logger.info("session stop")
            await session.pause()

        logger.info("save audio")
        return await self.save_audio(ctx)

    async def save_audio(self, ctx: InvocationContext) -> types.Content:
        music_plan = ComposerState.get_music_plan(ctx.session.state, self.task_id)
        bpm = sum([s.config.bpm for s in music_plan.stanzas]) / len(music_plan.stanzas)
        audio_segment = AudioSegment.from_raw(io.BytesIO(self.audio_byte_array), sample_width=2, frame_rate=48000, channels=2)

        one_bar_length = 1 * 4 / (bpm / 60) * 1000
        music_length = len(audio_segment)
        music_bar_length = math.floor(music_length / one_bar_length)

        # cut
        audio_segment = audio_segment[: music_bar_length * one_bar_length]
        part = types.Part.from_bytes(data=export_wav(audio_segment), mime_type="audio/wav")

        artifact_id = ComposerState.task_music_artifact_key(task_id=self.task_id)
        await ctx.artifact_service.save_artifact(app_name=ctx.app_name, user_id=ctx.user_id, session_id=ctx.session.id, filename=artifact_id, artifact=part)
        return types.Content(parts=[types.Part(text=f"generate music for:{artifact_id}")])


class ShortComposerAgent(Agent):
    task_id: str
    music_plan: str
    seconds: int | float

    def __init__(self, task_id: str, music_plan: str, seconds: int | float):
        super().__init__(
            task_id=task_id,
            music_plan=music_plan,
            seconds=seconds,
            model=GENERIC_MODEL,
            tools=[generate_music_tool],
            name=f"ShortComposerAgent_{task_id}",
            description="An AI music Composer Agent.",
            instruction="""
You are an AI Composer agent that create a prompt for Lyria based on provided music plan, and create a music by using `generate_music_tool`.
The music plan can be very abstract, your role is to create specific prompts and create the music even if the music plan is abstract.

Your task is to:
1. Read a intent to understand what music to create in [Music Plan].
2. Read a [Prompt Guide] to create good prompts for Lyria.
3. Create a prompt to passing to `generate_music_tool`.
4. Generate a music title.
5. Generate a music by `generate_music_tool`.
    - the task_id is written in below.
    - When you get a error from the tool, try again with changing the prompt.
6. Display the generated music by inserting a line "<artifact>music_id</artifact>" and inserting a line "<title>music_title</title>" in your message where
        replacing music_id with the real music_id you received and replacing music_title with generated music title by you.

[Prompt Guide]
# Lyria Music Generation Prompt Guide

This guide provides information on creating music and audio soundscapes using Lyria and how to modify prompts to achieve different results.

## Prompt Guide Overview

**Lyria** is a **foundation model for high-quality audio generation**.
It is capable of creating diverse soundscapes and musical pieces from text prompts.
To use Lyria, you provide a text description (a prompt) of what you want the generative AI model to generate.
**Lyria produces instrumental music**.

## Safety Information

Lyria applies **safety filters** across Vertex AI to help ensure generated audio doesn't contain offensive content or violate usage guidelines.
Prompts that violate responsible AI guidelines are blocked.
Lyria also includes recitation checking and artist intent checks.
You can report suspected abuse of Lyria or generated output containing inappropriate material or inaccurate information using the provided form.

## Basics for Writing Prompts

**Good prompts are descriptive and clear**.
To get your generated music closer to your desired output, identify your core musical idea and refine it by adding keywords and modifiers.

The following elements should be considered for your prompt:

1.  **Genre & Style:** The primary musical category (e.g., *electronic dance*, *classical*, *jazz*, *ambient*) and stylistic characteristics (e.g., *8-bit*, *cinematic*, *lo-fi*).
2.  **Mood & Emotion:** The desired feeling the music should evoke (e.g., *energetic*, *melancholy*, *peaceful*, *tense*).
3.  **Instrumentation:** Key instruments you want to hear (e.g., *piano*, *synthesizer*, *acoustic guitar*, *string orchestra*, *electronic drums*).
4.  **Tempo & Rhythm:** The pace (e.g., *fast tempo*, *slow ballad*, *120 BPM*) and rhythmic character (e.g., *driving beat*, *syncopated rhythm*, *gentle waltz*).
5.  (Optional) **Arrangement/Structure:** How the music progresses or layers (e.g., *starts with a solo piano, then strings enter*, *crescendo into a powerful chorus*).
6.  (Optional) **Soundscape/Ambiance:** Background sounds or overall sonic environment (e.g., *rain falling*, *city nightlife*, *spacious reverb*, *underwater feel*).
7.  (Optional) **Production Quality:** Desired audio fidelity or recording style (e.g., *high-quality production*, *clean mix*, *vintage recording*, *raw demo feel*).

## Examples of Prompts and Generated Output

This section presents examples showing how the level of detail affects the generated music.

### Energetic Electronic Track Example

This example demonstrates using several elements:
> Prompt: An energetic (mood) electronic dance track (genre) with a fast tempo (tempo) and a driving beat (rhythm), featuring prominent synthesizers (instrumentation) and electronic drums (instrumentation). High-quality production (production quality).
> *Description: A 30-second instrumental track with a clear, punchy electronic sound, upbeat rhythm, and a focus on synth melodies and a strong drum presence.*

### Evolving Ambient Soundscape Examples

These examples demonstrate revising your prompt for more specific results.

Minimal Prompt Example:
> Prompt: Ambient music with synthesizers.
> *Description: A basic ambient piece primarily using synth pads. The mood and structure are very general.*
Analysis: This is the first generated audio based on a minimal prompt.

More Detailed Prompt Example:
> Prompt: A calm and dreamy (mood) ambient soundscape (genre/style) featuring layered synthesizers (instrumentation) and soft, evolving pads (instrumentation/arrangement). Slow tempo (tempo) with a spacious reverb (ambiance/production). Starts with a simple synth melody, then adds layers of atmospheric pads (arrangement).
> *Description: A more developed ambient track. The audio evokes a peaceful, dreamy state with clear synth layers building slowly. The spacious reverb enhances the atmospheric quality.*
Analysis: A more detailed prompt results in music that is more focused, with a richer sonic environment and clear progression.

### Refined Prompts Focusing on Specific Elements

These examples show how to refine prompts by focusing on specific musical elements.

Genre & Style Focus:
> Prompt: A cinematic orchestral piece in a heroic, fantasy adventure style, with a grand, sweeping melody.
> *Description: Expect a full-sounding orchestral track with dramatic swells and a strong, memorable theme, reminiscent of a film score.*

Mood & Instrumentation Focus:
> Prompt: A peaceful and serene acoustic guitar piece, featuring a fingerpicked style, perfect for meditation.
> *Description: A gentle, calming instrumental track featuring a solo acoustic guitar playing a simple, soothing melody.*

Tempo & Rhythm Focus:
> Prompt: A tense, suspenseful underscore with a very slow, creeping tempo and a sparse, irregular rhythm. Primarily uses low strings and subtle percussion.
> *Description: An atmospheric piece designed to build tension, characterized by its slow pace, unsettling rhythmic elements, and dark string textures.*

## More Tips for Writing Prompts

The following tips help you write effective prompts for Lyria:

*   **Be descriptive and specific:** Use adjectives and adverbs to paint a clear sonic picture. The more detail, the better Lyria can understand your intent.
*   **Reference genres, moods, and styles:** Clearly state the musical category, desired feeling, and any stylistic characteristics.
*   **Specify key instruments and rhythms:** Mention important instruments and describe the desired pace and rhythmic feel.
*   **Iterate and experiment:** If the first result isn't perfect, modify your prompt by adding, removing, or changing keywords.

## Negative Prompts

**Negative prompts help specify elements to exclude from the music**. Describe what you want to discourage the model from generating.
The API parameter for this is `negative_prompt`.
You can list elements to exclude, e.g., `negative_prompt: "vocals, excessive cymbal crashes, distorted guitar"`.

Example Scenario:

Without Negative Prompt:
> Prompt: "A calm, relaxing piano piece for studying." *(Without negative prompt)*
> *Description: The piano piece is generally calm, but might include some unexpected louder dynamics or complex runs that could be distracting for study.*

With Negative Prompt:
> Prompt: "A calm, relaxing piano piece for studying."
> Negative Prompt: "complex melodies, loud dynamics, sudden changes, drums, vocals"
> *Description: The resulting piano piece is consistently calm and simple, avoiding distracting elements. The mood is more even and suitable for background focus.*
            """
            + f"""
[task_id]
{task_id}

[Music Plan]
{music_plan}

[Music Length]
{seconds} seconds
""",
        )
