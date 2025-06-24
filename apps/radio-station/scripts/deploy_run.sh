#!/bin/bash
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


# Script to deploy a service to Google Cloud Run.

# Exit immediately if a command exits with a non-zero status.
set -e
# Treat unset variables as an error when substituting.
set -u
# Cause a pipeline to return the exit status of the last command in the pipeline
# that returned a non-zero exit status, or zero if all commands in the pipeline
# exited successfully.
set -o pipefail

# 1. Navigate to the parent directory of the script's location.
# This assumes the script is in a subdirectory (e.g., 'scripts') and the
# source code and .env_for_deploy are in its parent directory.
SCRIPT_DIR_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
cd "$SCRIPT_DIR_PATH/.."
echo "Changed directory to $(pwd)"

# 2. Load environment variables from .env_for_deploy
ENV_FILE_PATH=".env"

if [ ! -f "$ENV_FILE_PATH" ]; then
    echo "Error: Environment file '$ENV_FILE_PATH' not found in $(pwd)."
    exit 1
fi

echo "Loading environment variables from $ENV_FILE_PATH..."
# Automatically export all variables subsequently defined or sourced.
set -a
# shellcheck disable=SC1090 # Disable warning for sourcing a variable file.
source "$ENV_FILE_PATH"
# Disable automatic export.
set +a

# Verify that necessary variables are set from the .env file or environment.
: "${GOOGLE_CLOUD_PROJECT:?Error: GOOGLE_CLOUD_PROJECT is not set. Please define it in $ENV_FILE_PATH or as an environment variable.}"
: "${AGENT_ENGINE_ID:?Error: AGENT_ENGINE_ID is not set. Please define it in $ENV_FILE_PATH or as an environment variable.}"
: "${ARTIFACT_BUCKET:?Error: ARTIFACT_BUCKET is not set. Please define it in $ENV_FILE_PATH or as an environment variable.}"
# It's highly recommended to define the region as well.
: "${GOOGLE_CLOUD_LOCATION:?Error: GCP_REGION is not set. Please define it in $ENV_FILE_PATH or as an environment variable (e.g., us-central1, asia-northeast1).}"

# 3. Construct the --command argument string for the container.
# The input command string is:
# adk,api-server,--port,8000,--host,0.0.0.0,--trace_to_cloud,--session_service_uri,"agentengine://$AGENT_ENGINE_ID,"/app/radio_station",--artifact_service_uri,"gs://ARTIFACT_BUCKET"
# This implies the following arguments are passed to the primary command `adk`:
#   - api-server
#   - --port
#   - 8000
#   - --host
#   - 0.0.0.0
#   - --trace_to_cloud
#   - --session_service_uri
#   - agentengine://${AGENT_ENGINE_ID}  (This is the argument for --session_service_uri)
#   - /app/radio_station                (This is a subsequent, separate argument for `adk`)
#   - --artifact_service_uri
#   - gs://${ARTIFACT_BUCKET}           (This is the argument for --artifact_service_uri)

# Using an array to build the command parts for clarity and safety,
# then joining with a comma for the gcloud --command flag.
declare -a container_command_parts
container_command_parts+=( "python" )
container_command_parts+=( "main.py" )
container_command_parts+=( "api_server" )
container_command_parts+=( "--port" "8000" )
container_command_parts+=( "--host" "0.0.0.0" )
container_command_parts+=( "--no-reload" )
container_command_parts+=( "--enable_cloud_logging" )
container_command_parts+=( "--trace_to_cloud" )
container_command_parts+=( "--session_service_uri" "agentengine://${AGENT_ENGINE_ID}" )
container_command_parts+=( "--artifact_service_uri" "gs://${ARTIFACT_BUCKET}" )
container_command_parts+=( "/app" )

# Join the array elements with a comma.
CONTAINER_COMMAND_STRING=$(IFS=,; echo "${container_command_parts[*]}")

echo "Deploying service 'radio-station' to Cloud Run..."
echo "  Project: $GOOGLE_CLOUD_PROJECT"
echo "  Region: $GOOGLE_CLOUD_LOCATION"
echo "  Source directory: $(pwd)"
echo "  Container command: $CONTAINER_COMMAND_STRING"

# Execute the gcloud run deploy command.
gcloud run deploy radio-station \
    --source . \
    --command "$CONTAINER_COMMAND_STRING" \
    --project "$GOOGLE_CLOUD_PROJECT" \
    --region "asia-northeast1" \
    --platform "managed" \
    --no-allow-unauthenticated \
    --env-vars-file=.env_for_deploy_run.yaml \
    --memory "8096Mi" \
    --cpu "4" \
    --timeout "3600s" \
    --port 8000
    # Add any other necessary flags for your service, for example:
    # --min-instances "0" # For cost saving, or "1" for faster cold starts
    # --max-instances "10"
    # --concurrency "80"
    # --service-account "your-service-account@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com"
    # --update-env-vars "KEY1=VALUE1,KEY2=VALUE2" # For env vars specific to the container, not from .env_for_deploy
    # --set-secrets "SECRET_NAME=your-secret-name:latest" # To mount secrets

echo "Cloud Run deployment command initiated for 'radio-station'."
echo "Monitor the deployment progress in the Google Cloud Console or via 'gcloud run services list'."