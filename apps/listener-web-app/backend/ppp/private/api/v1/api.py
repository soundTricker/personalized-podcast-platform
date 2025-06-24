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

from fastapi import APIRouter

from ppp.private.api.v1.endpoints import day_of_week, listener_programs

# Create private API router
private_api_router = APIRouter()

# Include routers from endpoints
private_api_router.include_router(
    day_of_week.router,
    prefix="/day-of-week",
    tags=["private-day-of-week"],
)
private_api_router.include_router(
    listener_programs.router,
    prefix="/listener-programs",
    tags=["private-listener-programs"],
)
