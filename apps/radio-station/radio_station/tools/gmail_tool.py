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

import base64
import datetime
import logging
import os
from typing import Any, Dict, List
from zoneinfo import ZoneInfo

from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ClientCreds, UserCreds
from aiogoogle.excs import AiogoogleError
from google.adk.tools import ToolContext

from radio_station.constants import GoogleApiScope
from radio_station.state_keys import GlobalState
from radio_station.utils.crypto import decrypt

logger = logging.getLogger(__name__)


async def list_gmail_messages(q: str, max_results: int, tool_context: ToolContext) -> List[Dict[str, Any]]:
    """Lists messages in the user's mailbox that match the given query.

    This tool allows you to search for and list email messages in the user's
    Gmail account. It uses the Gmail API to perform the search.

    Args:
        q: The search query to filter messages. It uses the same format as the
            Gmail search box. For example: 'from:someuser@example.com is:unread'
            If not provided, it will list all messages.
            For more details on query syntax, see:
            https://support.google.com/mail/answer/7190
        max_results: The maximum number of messages to return. The actual number
            of returned messages might be less. max: 500
        tool_context: The ADK ToolContext for execution.

    Returns:
        A list of message resources. Each resource contains a 'header' that is mail header dict by RFC2822 mail header format) and `body` that is mail body. Returns an empty list if no messages match the query or
        if an error occurs.
    """
    creds = None
    if (
        (listener := GlobalState.get_listener(tool_context.state))
        and GoogleApiScope.GmailReadOnly in listener.scopes
        and listener.encrypted_google_access_token
        and listener.encrypted_google_refresh_token
    ):
        creds = UserCreds(access_token=decrypt(listener.encrypted_google_access_token), refresh_token=decrypt(listener.encrypted_google_refresh_token))

    try:
        async with Aiogoogle(user_creds=creds, client_creds=ClientCreds(client_id=os.getenv("GOOGLE_CLIENT_ID"), client_secret=os.getenv("GOOGLE_CLIENT_SECRET"))) as aiogoogle_client:
            # Gmail APIのv1を非同期でdiscoveryします。
            # discoveryは一度実行されるとクライアント内部でキャッシュされます。
            gmail_v1 = await aiogoogle_client.discover("gmail", "v1")

            # メッセージを一覧表示するためのAPIリクエストを作成します。
            # 'userId="me"'は、認証済みユーザー自身を指す特別な識別子です。
            request = gmail_v1.users.messages.list(userId="me", q=q, maxResults=max_results)

            # ユーザーとしてリクエストを実行します。
            response = await aiogoogle_client.as_user(request)

            get_message_requests = []
            for message in response.get("messages", []):
                get_message_requests.append(gmail_v1.users.messages.get(userId="me", id=message["id"]))

            if not get_message_requests:
                return []

            results = []

            for i in range(0, len(get_message_requests), 5):
                reqs = get_message_requests[i : i + 5]
                logger.info(reqs)
                messages = await aiogoogle_client.as_user(*reqs)
                logger.info(messages)

                if isinstance(messages, dict):
                    messages = [messages]

                for message in messages:
                    logger.info(message)
                    header = {h["name"]: h["value"] for h in message["payload"]["headers"]}
                    results.append(
                        {
                            "header": header,
                            "snippet": message["snippet"],
                            "labelIds": message["labelIds"],
                            "body": base64.b64decode(message["payload"]["body"]["data"]) if "data" in message["payload"]["body"] else None,
                            "received_date": datetime.datetime.fromtimestamp(float(message["internalDate"]) / 1000, tz=ZoneInfo("Asia/Tokyo")),
                        }
                    )

            return results

    except AiogoogleError as e:
        # API関連のエラー（権限不足、無効なクエリなど）を捕捉します。
        logger.exception(f"An API error occurred while listing Gmail messages: {e}")
        return []
    except Exception as e:
        # その他の予期せぬエラーを捕捉します。
        logger.exception(f"An unexpected error occurred: {e}")
        return []
