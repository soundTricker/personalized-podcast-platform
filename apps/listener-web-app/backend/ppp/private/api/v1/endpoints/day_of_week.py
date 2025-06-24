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
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Query

from ppp.schemas.day_of_week import DayOfWeekResponse

router = APIRouter()


@router.get("", response_model=DayOfWeekResponse)
async def get_day_of_week(target_timestamp: float = Query(..., description="Target timestamp to get day of week for")) -> DayOfWeekResponse:
    """
    Get day of week for a given timestamp.

    Args:
        target_timestamp: Unix timestamp to get day of week for

    Returns:
        DayOfWeekResponse: Contains day_of_week (1=Monday, 7=Sunday)
    """
    target = datetime.fromtimestamp(target_timestamp, tz=ZoneInfo("Asia/Tokyo"))
    return DayOfWeekResponse(day_of_week=target.isoweekday())
