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
from typing import Any

import requests
from google.adk.tools import FunctionTool

logger = logging.getLogger(__name__)

# Google Places APIキーを環境変数から読み込みます。
# このキーはご自身のGoogle Cloudプロジェクトで有効化し、取得してください。
# .envファイルに GOOGLE_PLACES_API_KEY="YOUR_API_KEY" のように設定することを推奨します。
GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")

if not GOOGLE_MAPS_API_KEY:
    logger.warning("警告: 環境変数 'GOOGLE_MAPS_API_KEY' が設定されていません。 geolocation_tool は正しく動作しません。")


def get_geolocation_for_place(place_name: str) -> dict[str, Any]:
    """
    指定された地名（場所の名前や住所）から緯度と経度を取得します。
    Google Geocoding API を使用します。

    地名（場所の名前、住所、都市名、観光地名など）を指定すると、
    その場所の緯度、経度、およびGoogleによって整形された住所を返します。
    例えば「東京スカイツリーの緯度経度を教えて」や「パリの場所は？」のような質問に答えるために使用できます。


    Args:
        place_name: 緯度と経度を取得したい地名。
                    例: "東京タワー", "大阪駅", "フランス パリ"

    Returns:
        成功した場合は、緯度(latitude), 経度(longitude), 整形済み住所(formatted_address),
        およびステータス(status: "success") を含む辞書。
        失敗した場合は、エラーメッセージ(error)とステータス(status: "error") を含む辞書。
        例 (成功):
        {
            "latitude": 35.6585805,
            "longitude": 139.7454329,
            "formatted_address": "日本、〒105-0011 東京都港区芝公園４丁目２−８",
            "status": "success"
        }
        例 (失敗):
        {
            "error": "指定された地名が見つかりませんでした。",
            "status": "error"
        }
    """
    if not GOOGLE_MAPS_API_KEY:
        return {
            "error": "Google Places APIキーが設定されていません。",
            "status": "error",
        }

    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": place_name,
        "key": GOOGLE_MAPS_API_KEY,
        "language": "ja",  # 結果を日本語で取得する場合
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # HTTPエラーコードが4xxまたは5xxの場合に例外を発生
        data = response.json()

        if data["status"] == "OK":
            if data["results"]:
                location = data["results"][0]["geometry"]["location"]
                formatted_address = data["results"][0].get("formatted_address", "N/A")
                return {
                    "latitude": location["lat"],
                    "longitude": location["lng"],
                    "formatted_address": formatted_address,
                    "status": "success",
                }
            else:
                # "OK"ステータスでも結果がない場合 (通常はZERO_RESULTSになるはず)
                return {
                    "error": f"地名 '{place_name}' に対する結果が見つかりませんでした。",
                    "status": "error",
                }
        elif data["status"] == "ZERO_RESULTS":
            return {
                "error": f"地名 '{place_name}' が見つかりませんでした。",
                "status": "error",
            }
        else:
            # その他のAPIエラー (REQUEST_DENIED, INVALID_REQUEST, UNKNOWN_ERRORなど)
            error_message = data.get("error_message", f"Google Geocoding APIエラー: {data['status']}")
            return {"error": error_message, "status": "error"}

    except requests.exceptions.RequestException as e:
        # ネットワークエラーやタイムアウトなど
        return {
            "error": f"APIリクエスト中にネットワーク関連のエラーが発生しました: {e}",
            "status": "error",
        }
    except Exception as e:
        # JSONパースエラーや予期せぬエラー
        return {"error": f"処理中に予期せぬエラーが発生しました: {e}", "status": "error"}


# ADKのFunctionToolとしてラップ
geolocation_tool = FunctionTool(
    func=get_geolocation_for_place,
)
