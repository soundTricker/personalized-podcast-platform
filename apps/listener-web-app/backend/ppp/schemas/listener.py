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

from typing import Optional

from pydantic import EmailStr, Field

from ppp.schemas.base import BaseCreateSchema, BaseSchema, BaseUpdateSchema


class ListenerSchema(BaseSchema):
    """
    Schema for Listener response.
    """

    id: str
    email: EmailStr
    display_name: Optional[str] = None
    scopes: list[str] = Field(default_factory=list)


class ListenerCreateSchema(BaseCreateSchema):
    """
    Schema for creating a Listener.

    This schema is used for the signup API.
    """

    # No fields needed as we get the data from Firebase Auth
    pass


class ListenerUpdateSchema(BaseUpdateSchema):
    """
    Schema for updating a Listener.
    """

    email: Optional[EmailStr] = None
    display_name: Optional[str] = None
