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

import os
from typing import Final

from google.adk.models.lite_llm import LiteLlm

os.environ["VERTEXAI_PROJECT"] = os.environ["GOOGLE_CLOUD_PROJECT"]
os.environ["VERTEXAI_LOCATION"] = "global"


GENERIC_MODEL = LiteLlm(model="vertex_ai/gemini-2.5-flash-lite-preview-06-17")
THINKING_MODEL = "gemini-2.5-flash"


class GoogleApiScope:
    GmailReadOnly: Final[str] = "https://www.googleapis.com/auth/gmail.readonly"
    CalendarReadOnly: Final[str] = "https://www.googleapis.com/auth/calendar.events.readonly"
