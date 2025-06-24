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

from google.adk.agents.llm_agent import InstructionProvider
from google.adk.agents.readonly_context import ReadonlyContext
from google.api_core import exceptions
from google.cloud import secretmanager_v1 as secretmanager

logger = logging.getLogger(__name__)


def secret_instruction(secret_key: str, default: str) -> InstructionProvider:
    """
    Google Cloud Secret Managerから最新バージョンのシークレットを非同期で取得します。

    この関数は、指定されたキーのシークレットを取得します。シークレットの取得に失敗した場合
    （例: 存在しない、権限がない）や、必要な環境変数が設定されていない場合は、
    デフォルト値を返します。

    Args:
        secret_key (str): 取得するシークレットのID（名前）。
        default (str): シークレットの取得に失敗した場合に返すデフォルトの文字列。

    Returns:
        str: 取得したシークレットの文字列、またはデフォルト値。
    """

    async def _secret_instruction(ctx: ReadonlyContext):
        try:
            # 環境変数からGoogle CloudプロジェクトIDを取得します。
            # Cloud RunやCloud Functionsなどの環境では自動的に設定されています。
            project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
            if not project_id:
                logger.error(f"Error: The GOOGLE_CLOUD_PROJECT environment variable is not set. Returning default value for secret '{secret_key}'.")
                return default

            # Secret Managerの非同期クライアントを初期化します。
            # このクライアントはApplication Default Credentials (ADC) を使用して認証します。
            client = secretmanager.SecretManagerServiceAsyncClient()

            # アクセスするシークレットバージョンの完全なリソース名を構築します。
            # 'latest' は常に最新のバージョンを指します。
            name = f"projects/{project_id}/secrets/{secret_key}/versions/latest"

            # シークレットバージョンに非同期でアクセスします。
            response = await client.access_secret_version(request={"name": name})

            # レスポンスのペイロード（シークレットの値）をUTF-8でデコードして返します。
            payload = response.payload.data.decode("UTF-8")
            return payload

        except exceptions.NotFound:
            # シークレットが見つからない場合のエラーハンドリング
            logger.error(f"Error: Secret '{secret_key}' not found in project '{project_id}'. Returning default value.")
            return default
        except exceptions.PermissionDenied:
            # アクセス権がない場合のエラーハンドリング
            logger.error(f"Error: Permission denied to access secret '{secret_key}'. Check IAM permissions. Returning default value.")
            return default
        except Exception as e:
            # その他の予期せぬエラー
            logger.error(f"An unexpected error occurred while accessing secret '{secret_key}': {e}. Returning default value.")
            return default

    return _secret_instruction
