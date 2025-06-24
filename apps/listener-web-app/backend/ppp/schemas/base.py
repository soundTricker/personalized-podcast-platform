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

from datetime import datetime

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class Base(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class BaseSchema(Base):
    """
    Base schema for all schemas in the application.

    This class provides common fields and functionality for all schemas.
    """

    id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class BaseCreateSchema(Base):
    """
    Base schema for creating resources.

    This class provides common fields for creating resources.
    """

    pass


class BaseUpdateSchema(Base):
    """
    Base schema for updating resources.

    This class provides common fields for updating resources.
    """
