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
from datetime import datetime, timedelta
from typing import Optional

import google.auth
import google.auth.transport.requests
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import RedirectResponse, Response

from ppp.models.listener_program import PublishSetting
from ppp.services.chat import ChatAPI, get_chat_api
from ppp.services.listener_program import ListenerProgramService, get_listener_program_service
from ppp.services.program_broadcast_history import ProgramBroadcastHistoryService, get_program_broadcast_history_service
from ppp.services.rss import RSSService, get_rss_service

try:
    from google.cloud import storage

    GCS_AVAILABLE = True
except ImportError:
    GCS_AVAILABLE = False

router = APIRouter()


@router.get("/rss/{program_id}")
async def get_podcast_rss(
    program_id: str,
    private_key: Optional[str] = Query(None, description="Private key for limited access"),
    rss_service: RSSService = Depends(get_rss_service),
) -> Response:
    """
    Get RSS feed for a podcast program.

    This is a public API endpoint that generates RSS feeds for podcasts.

    Args:
        program_id: The ID of the program.
        private_key: The private key for limited access (optional).

    Returns:
        RSS feed as XML response.

    Raises:
        HTTPException:
            - 404 if program not found
            - 400 if program is private or invalid private key for limited access
    """
    try:
        rss_xml = await rss_service.generate_rss_feed(program_id, private_key)

        return Response(
            content=rss_xml,
            media_type="application/rss+xml",
            headers={
                "Content-Type": "application/rss+xml; charset=utf-8",
                "Cache-Control": "public, max-age=3600",  # Cache for 1 hour
            },
        )
    except HTTPException:
        # Re-raise HTTPExceptions from the service
        raise
    except Exception as e:
        # Handle any other unexpected errors
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/cover/{program_id}")
async def get_podcast_cover(
    program_id: str,
    private_key: Optional[str] = Query(None, description="Private key for limited access"),
    listener_program_service: ListenerProgramService = Depends(get_listener_program_service),
) -> Response:
    """
    Get cover art image for a podcast program.

    This endpoint serves the cover art images for podcasts.
    This is a public API endpoint that requires access control based on program settings.

    Args:
        program_id: The ID of the program.
        private_key: The private key for limited access (optional).

    Returns:
        Image file response or redirect to signed URL.

    Raises:
        HTTPException:
            - 404 if program not found or cover art not available
            - 400 if program is private or invalid private key for limited access
    """
    try:
        # 1. Get ListenerProgram by program_id
        program = await listener_program_service.get_by_id(program_id)
        if not program:
            raise HTTPException(status_code=404, detail="Program not found")

        # 2. Check if cover art is available
        if not program.cover_art_uri:
            raise HTTPException(status_code=404, detail="Cover art not available")

        # 3. Check publish_setting (same logic as audio endpoint)
        if program.publish_setting == PublishSetting.PRIVATE:
            raise HTTPException(status_code=400, detail="Program is private")

        if program.publish_setting == PublishSetting.LIMITED:
            if not private_key or private_key != program.private_key:
                raise HTTPException(status_code=400, detail="Invalid private key")

        # 4. Check if K_SERVICE is in environment (Cloud Run environment) and cover art is GCS URI
        if "K_SERVICE" in os.environ and GCS_AVAILABLE and program.cover_art_uri.startswith("gs://"):
            # Use GCS signed URL approach
            try:
                credentials, _ = google.auth.default()
                credentials.refresh(google.auth.transport.requests.Request())

                # Parse GCS URI (gs://bucket/path)
                gcs_path = program.cover_art_uri[5:]  # Remove 'gs://' prefix
                bucket_name, blob_path = gcs_path.split("/", 1)

                # Create GCS client and get signed URL
                client = storage.Client()
                bucket = client.bucket(bucket_name)
                blob = bucket.blob(blob_path)

                # Generate signed URL with 10 minutes expiration
                signed_url = blob.generate_signed_url(
                    version="v4",
                    expiration=datetime.now() + timedelta(minutes=10),
                    method="GET",
                    service_account_email=credentials.service_account_email,
                    access_token=credentials.token
                )

                # Redirect to signed URL
                return RedirectResponse(url=signed_url, status_code=302)

            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Failed to generate signed URL: {str(e)}")
        else:
            # For non-GCS URIs or local development, return the URI directly as redirect
            return RedirectResponse(url=program.cover_art_uri, status_code=302)

    except HTTPException:
        # Re-raise HTTPExceptions
        raise
    except Exception as e:
        # Handle any other unexpected errors
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/audio/{program_id}/{broadcast_history_id}")
async def get_podcast_audio(
    program_id: str,
    broadcast_history_id: str,
    private_key: Optional[str] = Query(None, description="Private key for limited access"),
    listener_program_service: ListenerProgramService = Depends(get_listener_program_service),
    broadcast_history_service: ProgramBroadcastHistoryService = Depends(get_program_broadcast_history_service),
    chat_api: ChatAPI = Depends(get_chat_api),
) -> Response:
    """
    Get audio file for a podcast episode.

    This endpoint serves the actual audio files referenced in the RSS feed enclosure tags.
    This is a public API endpoint that requires access control based on program settings.

    Args:
        program_id: The ID of the program.
        broadcast_history_id: The ID of the broadcast history.
        private_key: The private key for limited access (optional).

    Returns:
        Audio file response or redirect to signed URL.

    Raises:
        HTTPException:
            - 404 if program or broadcast history not found
            - 400 if program is private or invalid private key for limited access
    """
    try:
        # 1. Get ListenerProgram by program_id
        program = await listener_program_service.get_by_id(program_id)
        if not program:
            raise HTTPException(status_code=404, detail="Program not found")

        # 2. Check publish_setting (same logic as RSS endpoint)
        if program.publish_setting == PublishSetting.PRIVATE:
            raise HTTPException(status_code=400, detail="Program is private")

        if program.publish_setting == PublishSetting.LIMITED:
            if not private_key or private_key != program.private_key:
                raise HTTPException(status_code=400, detail="Invalid private key")

        # 3. Get the broadcast history
        broadcast_history = await broadcast_history_service.get_broadcast_history_by_id(program_id, broadcast_history_id)
        if broadcast_history is None:
            raise HTTPException(
                status_code=404,
                detail=f"Broadcast history with ID {broadcast_history_id} not found",
            )

        # 4. Check if K_SERVICE is in environment (Cloud Run environment)
        if "K_SERVICE" in os.environ and GCS_AVAILABLE:
            # Use GCS signed URL approach
            try:
                credentials, _ = google.auth.default()
                credentials.refresh(google.auth.transport.requests.Request())

                # Get GCS URI from broadcast history
                gcs_uri = broadcast_history.gcs_uri()

                # Parse GCS URI (gs://bucket/path)
                if not gcs_uri.startswith("gs://"):
                    raise HTTPException(status_code=500, detail="Invalid GCS URI format")

                # Extract bucket and blob path
                gcs_path = gcs_uri[5:]  # Remove 'gs://' prefix
                bucket_name, blob_path = gcs_path.split("/", 1)

                # Create GCS client and get signed URL
                client = storage.Client()
                bucket = client.bucket(bucket_name)
                blob = bucket.blob(blob_path)

                # Generate signed URL with 10 minutes expiration
                signed_url = blob.generate_signed_url(
                    version="v4",
                    expiration=datetime.now() + timedelta(minutes=10),
                    method="GET",
                    service_account_email=credentials.service_account_email,
                    access_token=credentials.token
                )

                # Redirect to signed URL
                return RedirectResponse(url=signed_url, status_code=302)

            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Failed to generate signed URL: {str(e)}")
        else:
            # Use direct artifact serving (same as existing get_program_broadcast_history_audio)
            artifact = await chat_api.load_artifact(program.listener_id, broadcast_history.session_id, broadcast_history.artifact_id)

            if artifact is None:
                raise HTTPException(
                    status_code=404,
                    detail="Artifact not found",
                )

            return Response(status_code=200, content=artifact.inline_data.data, media_type=artifact.inline_data.mime_type)

    except HTTPException:
        # Re-raise HTTPExceptions
        raise
    except Exception as e:
        # Handle any other unexpected errors
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
