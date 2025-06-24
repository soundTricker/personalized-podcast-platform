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

FROM python:3.12-slim
WORKDIR /app

RUN apt-get -y update && apt-get install -y ffmpeg libavcodec-extra git curl

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Change ownership of /app to myuser
RUN chown -R myuser:myuser /app

ENV PATH="/home/myuser/.local/bin:$PATH"

ENV GOOGLE_GENAI_USE_VERTEXAI=1
ENV GOOGLE_CLOUD_PROJECT=ai-agent-sample-1
ENV GOOGLE_CLOUD_LOCATION=us-central1

RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
RUN uv pip install --system --no-cache-dir .

COPY "radio_station/" "/app/radio_station/"
COPY main.py "/app/"
COPY .env_for_deploy "/app/radio_station/.env"

# Switch to the non-root user
USER myuser

EXPOSE 8000

CMD python main.py api_server --port=8000 --host=0.0.0.0  "/app"