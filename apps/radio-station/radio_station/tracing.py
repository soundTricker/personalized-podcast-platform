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

import logging
import os

import google.auth
import google.auth.transport.grpc
import google.auth.transport.requests
import grpc
from google.auth.transport.grpc import AuthMetadataPlugin
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.sdk.resources import SERVICE_INSTANCE_ID, SERVICE_NAME, SERVICE_VERSION, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

logger = logging.getLogger(__name__)


def setup():
    # Retrieve and store Google application-default credentials
    credentials, project_id = google.auth.default()
    # Request used to refresh credentials upon expiry
    request = google.auth.transport.requests.Request()

    auth_metadata_plugin = AuthMetadataPlugin(credentials=credentials, request=request)

    # Initialize gRPC channel credentials using the AuthMetadataPlugin
    channel_creds = grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(),
        grpc.metadata_call_credentials(auth_metadata_plugin),
    )

    otlp_grpc_exporter = OTLPSpanExporter(credentials=channel_creds)

    resource = Resource.create(
        attributes={
            "gcp.project_id": project_id,
            SERVICE_NAME: os.environ.get("K_SERVICE", "unknown"),
            SERVICE_VERSION: os.environ.get("K_REVISION", "unknown"),
            SERVICE_INSTANCE_ID: os.environ.get("K_CONFIGURATION", "unknown"),
        }
    )

    trace_provider = TracerProvider(resource=resource)
    trace_provider.add_span_processor(BatchSpanProcessor(otlp_grpc_exporter))
    trace.set_tracer_provider(trace_provider)

    logger.info("Finished set up tracing")
