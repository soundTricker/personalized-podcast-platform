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

from firedantic import AsyncModel, AsyncSubModel
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel


class BaseModel(AsyncModel):
    """
    Base model for all models in the application.

    This class extends AsyncModel from firedantic to provide common functionality
    for all models in the application.

    Includes common timestamp fields (created_at and updated_at) for all models.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    # Timestamps
    created_at: datetime = datetime.utcnow()
    updated_at: datetime | None = None


class BaseSubModel(AsyncSubModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    created_at: datetime = datetime.utcnow()
    updated_at: datetime | None = None
