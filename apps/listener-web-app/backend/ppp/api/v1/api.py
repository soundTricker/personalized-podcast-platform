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

from ppp.api.v1.endpoints import (
    agents,
    google_oauth2,
    listener_program_segments,
    listener_programs,
    listeners,
    podcast,
    program_broadcast_history,
    radio_casts,
)

# Create API router
api_router = APIRouter()

# Include routers
api_router.include_router(listeners.router, prefix="/listeners", tags=["listeners"])
api_router.include_router(listener_programs.router, prefix="/listener-programs", tags=["listener-programs"])
api_router.include_router(listener_program_segments.router, prefix="/listener-programs", tags=["listener-program-segments"])
api_router.include_router(program_broadcast_history.router, prefix="/listener-programs", tags=["program-broadcast-history"])
api_router.include_router(radio_casts.router, prefix="/radio-casts", tags=["radio-casts"])
api_router.include_router(podcast.router, prefix="/podcast", tags=["podcast"])
api_router.include_router(google_oauth2.router, tags=["google-oauth2"])

api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
