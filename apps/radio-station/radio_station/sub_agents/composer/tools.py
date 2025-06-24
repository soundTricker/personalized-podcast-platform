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

import base64
import io
import logging
import math

import google.auth
from google.adk.tools import ToolContext
from google.cloud import aiplatform
from google.genai import types
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
from pydub import AudioSegment

from radio_station.state_keys import ComposerState
from radio_station.utils.audio import export_wav

loggger = logging.getLogger(__name__)


async def generate_music_tool(task_id: str, prompt: str, negative_prompt: str, seed: int, seconds: float, tool_context: ToolContext):
    """
    Generates music based on the provided prompts by utilizing Google's AI
    Platform services and the lyria-002 model. The function is responsible for setting
    up the client, creating request instances and parameters, and executing the request
    to retrieve generated samples. The responses consist of generated musical data
    predictions.

    The generated music will be saved to artifact, The filename will be like 'generated_audio_{sample_number}.mp3'.

    :param task_id: this task_id
    :param prompt: The prompt to use for generating music in English, it sends to Lyria model.
    :param negative_prompt: The negative prompt for avoiding specific features in the
        generated music. When you don't need passing, you can set the empty string.
    :param seed: The random seed for initialization to control the variability in
        output. When you don't need passing, you can set -1.
    :param tool_context: An object representing the contextual or environmental
        information required for the tool's execution.
    :param seconds: generate music seconds
    :return: list of the generated music_id, when it returns None, the process is failed. please retry again with changing the prompt.
    """

    try:
        client_options = {"api_endpoint": "aiplatform.googleapis.com"}
        client = aiplatform.gapic.PredictionServiceAsyncClient(client_options=client_options)

        params: dict[str, str | int] = {"prompt": prompt}

        if negative_prompt:
            params["negative_prompt"] = negative_prompt

        if seed > 0:
            params["seed"] = seed

        params["sample_count"] = 1

        loggger.info(f"Generate music params: {params}")

        instance = json_format.ParseDict(params, Value())
        instances = [instance]

        parameters_dict = {}
        parameters = json_format.ParseDict(parameters_dict, Value())

        _, project_id = google.auth.default()

        endpoint_path = f"projects/{project_id}/locations/us-central1/publishers/google/models/lyria-002"
        loggger.info(f"endpoint path {endpoint_path}")

        response = await client.predict(endpoint=endpoint_path, instances=instances, parameters=parameters)
        predictions = response.predictions
        loggger.info(f"Returned {len(predictions)} samples")

        mp3_list = []
        for pred in predictions:
            bytes_b64 = dict(pred)["bytesBase64Encoded"]
            decoded_audio_data = base64.b64decode(bytes_b64)
            audio_segment = AudioSegment.from_wav(io.BytesIO(decoded_audio_data))

            if len(audio_segment) < seconds * 1000:
                audio_segment = audio_segment * math.ceil(seconds * 1000 / len(audio_segment))
            audio_segment = audio_segment[: seconds * 1000]
            wav = export_wav(audio_segment)
            part = types.Part.from_bytes(data=wav, mime_type="audio/wav")
            artifact_id = ComposerState.task_music_artifact_key(task_id)
            await tool_context.save_artifact(artifact_id, part)
            mp3_list.append(artifact_id)

        tool_context.state.update({"music_artifact_list": mp3_list})

        return mp3_list
    except Exception as e:
        loggger.exception(f"failed to create the music. {e}")
        return None
