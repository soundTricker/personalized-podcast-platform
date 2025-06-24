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

from pydantic import EmailStr, Field

from ppp.models.base import BaseModel


class Listener(BaseModel):
    """
    Listener model representing a user of the application.

    This model is used to store information about listeners in Firestore.
    """

    __collection__ = "listeners"

    # Listener ID
    id: str = Field(description="The ID of the listener")  # Firebase Auth UID

    # User information
    email: EmailStr = Field(description="The email of the listener")
    display_name: str | None = None

    scopes: list[str] = Field(description="The list of scopes the listener belongs to", default_factory=list)
    encrypted_google_access_token: str | None = Field(description="The encrypted Google access token of the listener", default=None)
    encrypted_google_refresh_token: str | None = Field(description="The encrypted Google refresh token of the listener", default=None)
