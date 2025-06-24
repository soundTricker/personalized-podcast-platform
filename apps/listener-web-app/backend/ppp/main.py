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

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ppp import logging
from ppp.api.v1.api import api_router
from ppp.firestore.client import configure_firedantic


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_firedantic()
    yield


logging.setup()

# Create FastAPI application instance
app = FastAPI(title="PPP Listener Web API", description="API for Personalized Podcast Platform Listener Web App", version="0.1.0", lifespan=lifespan)

is_mcp_mode = "MCP_MODE" in os.environ


# Check if in batch mode
is_batch_mode = "BATCH_MODE" in os.environ

# Include API router only if not in batch mode
if not is_mcp_mode and not is_batch_mode:
    app.include_router(api_router, prefix="/api/v1")

# Include tasks router only if in batch mode
if not is_mcp_mode and is_batch_mode:
    from ppp.private.api.v1.api import private_api_router
    from ppp.tasks.api import tasks_router

    app.include_router(tasks_router, prefix="/__tasks__")
    # Include private API router
    app.include_router(private_api_router, prefix="/private/api/v1")

if is_mcp_mode:
    from ppp.mcp.mcp import mcp_router

    app.include_router(mcp_router, prefix="/mcp")

if "K_SERVICE" in os.environ:
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

    from ppp import tracing

    tracing.setup()
    FastAPIInstrumentor.instrument_app(app)


@app.get("/")
async def root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to PPP Listener Web API"}


if is_mcp_mode:
    from fastapi_mcp import FastApiMCP

    mcp = FastApiMCP(
        app,
        name="Personalized Podcast Platform MCP",
        describe_all_responses=True,
        describe_full_response_schema=True,
    )
    mcp.mount()
