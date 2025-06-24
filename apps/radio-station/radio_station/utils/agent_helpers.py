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

from google.adk.auth import AuthConfig
from google.adk.events import Event
from google.genai import types


def get_auth_request_function_call(event: Event) -> types.FunctionCall | None:
    # Get the special auth request function call from the event
    if not event.content or not event.content.parts:
        return None
    for part in event.content.parts:
        if (
            part
            and part.function_call
            and part.function_call.name == 'adk_request_credential'
            and event.long_running_tool_ids
            and part.function_call.id in event.long_running_tool_ids
        ):
            return part.function_call
    return None

def get_auth_config(auth_request_function_call: types.FunctionCall) -> AuthConfig:
    # Extracts the AuthConfig object from the arguments of the auth request function call
    if not auth_request_function_call.args or not (auth_config := auth_request_function_call.args.get('authConfig')):
        raise ValueError(f'Cannot get auth config from function call: {auth_request_function_call}')

    if isinstance(auth_config, dict):
        auth_config = AuthConfig(**auth_config)

    if not isinstance(auth_config, AuthConfig):
        raise ValueError(f'Cannot get auth config {auth_config} is not an instance of AuthConfig.')
    return auth_config
