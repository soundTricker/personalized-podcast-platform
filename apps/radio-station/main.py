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
from typing import Optional

import click
import uvicorn
from google.adk.cli.cli_tools_click import adk_services_options, fast_api_common_options
from google.adk.cli.fast_api import get_fast_api_app
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


@click.group(context_settings={"max_content_width": 240})
@click.version_option("0.0.1")
def main():
    """Agent Development Kit CLI tools."""
    pass


@main.command("api_server")
@click.option(
    "--host",
    type=str,
    help="Optional. The binding host of the server",
    default="127.0.0.1",
    show_default=True,
)
@click.option(
    "--enable_cloud_logging",
    is_flag=True,
    type=bool,
    help="Optional, enable cloud logging",
    default=False,
    show_default=True,
)
@fast_api_common_options()
@adk_services_options()
# The directory of agents, where each sub-directory is a single agent.
# By default, it is the current working directory
@click.argument(
    "agents_dir",
    type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    default=os.getcwd(),
)
def cli_api_server(
    agents_dir: str,
    log_level: str = "INFO",
    allow_origins: Optional[list[str]] = None,
    host: str = "127.0.0.1",
    port: int = 8000,
    reload: bool = True,
    session_service_uri: Optional[str] = None,
    artifact_service_uri: Optional[str] = None,
    memory_service_uri: Optional[str] = None,
    eval_storage_uri: Optional[str] = None,
    trace_to_cloud: bool = False,
    enable_cloud_logging: bool = False,
    a2a: bool = False,
):
    # logs.setup_adk_logger(getattr(logging, log_level.upper()))

    if trace_to_cloud:
        from radio_station import tracing

        tracing.setup()

    app = get_fast_api_app(
        agents_dir=agents_dir,
        session_service_uri=session_service_uri,
        artifact_service_uri=artifact_service_uri,
        memory_service_uri=memory_service_uri,
        eval_storage_uri=eval_storage_uri,
        allow_origins=allow_origins,
        web=False,
        trace_to_cloud=False,
        a2a=a2a,
    )
    if trace_to_cloud:
        FastAPIInstrumentor.instrument_app(app)

    if enable_cloud_logging:
        import google.cloud.logging

        client = google.cloud.logging.Client()
        client.setup_logging(
            log_level=log_level,
            excluded_loggers=(
                "google_adk",
                "httpx",
                "google.api_core.bidi",
                "werkzeug",
                "google_genai._api_client",
            ),
        )

    config = uvicorn.Config(
        app,
        host=host,
        port=port,
        reload=reload,
    )
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    main()
