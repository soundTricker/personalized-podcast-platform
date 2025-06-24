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

import typing

import google.auth
import google.oauth2.credentials
import google.oauth2.id_token
import httpx
from google.auth.transport.requests import Request as AuthRequest
from httpx import Request, Response

from ppp.settings import Settings


class GoogleJWTAuth(httpx.Auth):
    def __init__(self, settings: Settings):
        self.settings = settings

    def auth_flow(self, request: Request) -> typing.Generator[Request, Response, None]:
        creds, _ = google.auth.default()

        creds.refresh(AuthRequest())
        if isinstance(creds, google.oauth2.credentials.Credentials):
            creds.apply(request.headers, creds.id_token)
        else:
            # maybe run on cloud run
            auth_req = google.auth.transport.requests.Request()  # ty: ignore[unresolved-attribute]
            aud = self.settings.BACKEND_URL
            id_token = google.oauth2.id_token.fetch_id_token(auth_req, aud)
            request.headers["Authorization"] = f"Bearer {id_token}"
        yield request
