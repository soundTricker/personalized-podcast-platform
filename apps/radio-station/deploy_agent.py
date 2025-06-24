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

import json
import os

import dotenv
import requests
import vertexai
from google.adk.artifacts import GcsArtifactService
from vertexai import agent_engines

dotenv.load_dotenv()
envs = dotenv.dotenv_values(".env_for_deploy")
vertexai.init(project=os.environ.get("GOOGLE_CLOUD_PROJECT"), location=os.environ.get("GOOGLE_CLOUD_LOCATION"), staging_bucket=os.environ.get("STAGING_BUCKET"))

SETTING_FILENAME = ".agentengine.json"

bucket = os.environ.get("ARTIFACT_BUCKET")


def generate_artifact_service():
    # TODO
    return GcsArtifactService(bucket)


def deploy_agentengine():
    from radio_station.adk_app import CustomAdkApp
    from radio_station.agent import root_agent

    adk_app = CustomAdkApp(agent=root_agent, enable_tracing=True, artifact_service_builder=generate_artifact_service)

    if not os.path.exists("radio_station/ffmpeg-7.0.2-amd64-static"):
        res = requests.get("https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz")
        res.raise_for_status()
        with open("radio_station/ffmpeg-release-amd64-static.tar.xz", mode="wb") as fp:
            fp.write(res.content)

        import tarfile

        with tarfile.open("radio_station/ffmpeg-release-amd64-static.tar.xz", mode="r:xz") as tar:
            tar.extractall("radio_station")
        os.remove("radio_station/ffmpeg-release-amd64-static.tar.xz")

    packages = ["radio_station"]

    requirements = [
        "feedparser>=6.0.11",
        "google-adk>=1.2.1",
        "google-cloud-aiplatform[adk,agent-engines]>=1.97.0",
        "google-cloud-aiplatform[evaluation]>=1.97.0",
        "google-cloud-logging>=3.12.1",
        "google-cloud-firestore>=2.21.0",
        "google-cloud-storage>=2.18.0",
        "google-cloud-texttospeech>=2.27.0",
        "google-genai>=1.18.0",
        "pydantic[email]>=2.11.5",
        "pydub>=0.25.1",
        "aiohttp>=3.11.18",
        "cryptography>=45.0.4",
        "litellm>=1.72.1",
        "git+https://github.com/weatherapicom/python.git#egg=weatherapipython",
    ]
    display_name = "RadioStationAgent"

    if os.path.isfile(SETTING_FILENAME):
        print("setting file found")

        with open(SETTING_FILENAME, mode="r") as fp:
            settings = json.load(fp)
            agent_engine_id = settings["agent_engine_id"]
            agent_engine = agent_engines.get(agent_engine_id)
            print(f"start updating {agent_engine_id}")
            agent_engine.update(agent_engine=adk_app, display_name=display_name, requirements=requirements, extra_packages=packages, env_vars=envs)
        return

    print("setting file not found")
    print("create new agent engine instance")
    agent_engine = agent_engines.create(agent_engine=adk_app, display_name=display_name, requirements=requirements, extra_packages=packages, env_vars=envs)
    print(f"Done creating new agent engine instance. resource name: {agent_engine.resource_name}")
    with open(SETTING_FILENAME, mode="w") as fp:
        print(f"Create setting file to {fp.name}")
        json.dump(
            {
                "agent_engine_id": agent_engine.resource_name,
            },
            fp,
        )


if __name__ == "__main__":
    deploy_agentengine()
