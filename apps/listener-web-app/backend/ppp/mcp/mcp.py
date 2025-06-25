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

from ppp.mcp.endpoints import google_oauth2, listener, listener_program, listener_program_segments, radio_casts

# Create MCP router
mcp_router = APIRouter()

# Include routers
mcp_router.include_router(listener.router, prefix="/listener", tags=["mcp-listener"])
mcp_router.include_router(listener_program.router, prefix="/listener-programs", tags=["mcp-listener-programs"])
mcp_router.include_router(listener_program_segments.router, prefix="/listener-program-segments", tags=["mcp-listener-program-segments"])
mcp_router.include_router(radio_casts.router, prefix="/radio-casts", tags=["mcp-radio-casts"])
mcp_router.include_router(google_oauth2.router, tags=["mcp-google-oauth2"])
