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

import asyncio
from typing import List

from ppp.firestore.client import configure_firedantic
from ppp.models.radio_cast import RadioCast, RadioCastRole

# Provided voice names and their personalities (English)
# This will be used to select voice_name and as a base for Japanese personality
VOICE_CHARACTER_DATA_RAW = """
Zephyr -- Bright
Puck -- Upbeat
Charon -- Informative
Kore -- Firm
Fenrir -- Excitable
Leda -- Youthful
Orus -- Firm
Aoede -- Breezy
Callirrhoe -- Easy-going
Autonoe -- Bright
Enceladus -- Breathy
Iapetus -- Clear
Umbriel -- Easy-going
Algieba -- Smooth
Despina -- Smooth
Erinome -- Clear
Algenib -- Gravelly
Rasalgethi -- Informative
Laomedeia -- Upbeat
Achernar -- Soft
Alnilam -- Firm
Schedar -- Even
Gacrux -- Mature
Pulcherrima -- Forward
Achird -- Friendly
Zubenelgenubi -- Casual
Vindemiatrix -- Gentle
Sadachbia -- Lively
Sadaltager -- Knowledgeable
Sulafat -- Warm
"""


def parse_voice_data(data: str) -> List[tuple[str, str]]:
    """
    Parses the raw voice data string into a list of (voice_name, character_en) tuples.
    """
    parsed_data = []
    for line in data.strip().split("\n"):
        if " -- " in line:
            name, character = line.split(" -- ", 1)
            parsed_data.append((name.strip(), character.strip()))
    return parsed_data


def create_japanese_sample_radio_casts() -> List[RadioCast]:
    """
    Creates a list of 10 sample RadioCast objects with Japanese personas.
    These are intended to be pre-defined casts, so listener_id is None.
    """
    sample_casts: List[RadioCast] = []

    available_voices = parse_voice_data(VOICE_CHARACTER_DATA_RAW)

    # Helper to map English character to Japanese personality
    # This is a simple mapping, can be expanded for more nuance
    def translate_personality(character_en: str) -> str:
        mapping = {
            "Bright": "明るい",
            "Upbeat": "アップビートな",
            "Informative": "情報通な",
            "Firm": "しっかりした",
            "Excitable": "エキサイティングな",
            "Youthful": "若々しい",
            "Breezy": "軽快な",
            "Easy-going": "のんびりした",
            "Breathy": "息遣いの感じられる",
            "Clear": "クリアな",
            "Smooth": "スムーズな",
            "Gravelly": "しゃがれた",
            "Soft": "ソフトな",
            "Even": "落ち着いた",
            "Mature": "成熟した",
            "Forward": "積極的な",
            "Friendly": "フレンドリーな",
            "Casual": "カジュアルな",
            "Gentle": "優しい",
            "Lively": "生き生きとした",
            "Knowledgeable": "知識豊富な",
            "Warm": "温かい",
        }
        return mapping.get(character_en, character_en)  # Fallback to English if no mapping

    personas_data = [
        {
            "name_jp": "DJ ケンジ",
            "voice_idx": 0,  # Zephyr -- Bright
            "description_jp": "朝の通勤時間をフレッシュに！DJケンジが最新のヒットチャートと明るいトークをお届けします。",
        },
        {
            "name_jp": "MC ユミ",
            "voice_idx": 1,  # Puck -- Upbeat
            "description_jp": "週末の夜はMCユミにおまかせ！アップビートな選曲で気分を上げていきましょう。",
        },
        {
            "name_jp": "ナビゲーター リョウ",
            "voice_idx": 2,  # Charon -- Informative
            "description_jp": "知的好奇心を刺激する、ナビゲーター・リョウ。世界のニュースから身近な話題まで深く掘り下げます。",
        },
        {
            "name_jp": "パーソナリティ サキ",
            "voice_idx": 3,  # Kore -- Firm
            "description_jp": "リスナーの悩みに真摯に寄り添う、パーソナリティ・サキ。しっかりとした口調で的確なアドバイスを。",
        },
        {
            "name_jp": "DJ ハヤト",
            "voice_idx": 4,  # Fenrir -- Excitable
            "description_jp": "エキサイティングなスポーツ実況ならDJハヤト！熱い実況で試合の興奮をそのままお届け！",
        },
        {
            "name_jp": "アオイちゃん",
            "voice_idx": 5,  # Leda -- Youthful
            "description_jp": "ティーンのカリスマ、アオイちゃん！若々しい感性でトレンド情報を発信中！",
        },
        {
            "name_jp": "コメンテーター タカシ",
            "voice_idx": 8,  # Callirrhoe -- Easy-going
            "description_jp": "コメンテーターのタカシが、日々の出来事をのんびりとした語り口で解説。ほっと一息つける時間を提供します。",
        },
        {
            "name_jp": "DJ マナミ",
            "voice_idx": 9,  # Autonoe -- Bright
            "description_jp": "DJマナミのスマイルボイスで、午後のひとときを明るく彩ります。リクエストも募集中！",
        },
        {
            "name_jp": "ストーリーテラー カイト",
            "voice_idx": 11,  # Iapetus -- Clear
            "description_jp": "クリアな声で物語の世界へ誘う、ストーリーテラー・カイト。心に残る名作をお届け。",
        },
        {
            "name_jp": "ミッドナイト・ナビゲーター レイカ",
            "voice_idx": 29,  # Sulafat -- Warm
            "description_jp": "深夜の静寂に寄り添う、ミッドナイト・ナビゲーターのレイカ。温かい声で、一日の終わりに安らぎを。",
        },
    ]

    # Ensure we don't go out of bounds for available_voices
    num_personas_to_create = min(len(personas_data), len(available_voices))

    for i in range(num_personas_to_create):
        persona_def = personas_data[i]
        voice_name_en, character_en = available_voices[persona_def["voice_idx"]]

        cast = RadioCast(
            name=persona_def["name_jp"],
            listener_id=None,  # Pre-defined cast
            role=RadioCastRole.RadioPersonality,
            voice_name=voice_name_en,
            personality=persona_def["description_jp"],
            # 'id' will be auto-generated by Firestore upon saving if not provided
        )
        sample_casts.append(cast)

    # If personas_data has fewer items than 10, this will create fewer than 10.
    # If you strictly need 10, ensure personas_data has 10 items and voice_idx are valid.

    return sample_casts


async def main():
    configure_firedantic()

    predefined_radio_cast_map = {r.name: r for r in await RadioCast.find_predefined_radio_casts()}

    sample_radio_casts = create_japanese_sample_radio_casts()
    print(f"生成された日本人風ラジオキャストのサンプルデータ ({len(sample_radio_casts)}件):")

    print("saving...")

    for i, cast_data in enumerate(sample_radio_casts):
        origin = predefined_radio_cast_map.get(cast_data.name, cast_data)
        if origin.id is not None:
            cast_data.id = origin.id

        print(f"\n--- サンプルキャスト {i + 1} ---")
        print(f"名前: {cast_data.name}")
        print(f"リスナーID: {cast_data.listener_id}")
        print(f"役割: {cast_data.role.value}")
        print(f"ボイス名 (英語): {cast_data.voice_name}")
        print(f"性格 (日本語): {cast_data.personality}")
        await cast_data.save()
        print("saved", cast_data.id, cast_data.get_document_id(), cast_data._get_doc_ref().path, cast_data._get_col_ref())

    print("done")


if __name__ == "__main__":
    asyncio.run(main())
