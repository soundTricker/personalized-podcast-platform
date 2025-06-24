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


def setup():
    if "K_SERVICE" not in os.environ:
        return

    import google.cloud.logging

    client = google.cloud.logging.Client()
    client.setup_logging(
        excluded_loggers=(
            "google_adk",
            "httpx",
            "google.api_core.bidi",
            "werkzeug",
        )
    )
