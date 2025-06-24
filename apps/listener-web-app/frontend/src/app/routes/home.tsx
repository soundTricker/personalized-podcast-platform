/**
 * Copyright 2025 Keisuke Tominaga a.k.a soundTricker
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { Link } from "react-router";
import { Button, Card } from "flowbite-react";

function HomePage() {
  return (
    <div className="mx-auto px-4 py-8">
      <header className="mb-12 text-center">
        <h1 className="text-4xl font-bold mb-4">Personalized Podcast Platform</h1>
        <p className="text-xl text-gray-600">あなただけのAIポッドキャストを楽しもう</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto">
        <Card className="max-w-sm">
          <h5 className="text-2xl font-bold tracking-tight text-gray-900">
            パーソナライズされたコンテンツ
          </h5>
          <p className="font-normal text-gray-700">
            あなたの興味や好みに合わせたポッドキャストをAIが自動生成します。
          </p>
        </Card>

        <Card className="max-w-sm">
          <h5 className="text-2xl font-bold tracking-tight text-gray-900">
            リスナープログラム
          </h5>
          <p className="font-normal text-gray-700">
            あなた専用のポッドキャストプログラムを作成して管理できます。
          </p>
          <div className="flex flex-col gap-2">
            <Button as={Link} to="/listener-programs/create">
              新規プログラム作成
            </Button>
            <Button color="light" as={Link} to="/listener-programs">
              マイプログラム一覧
            </Button>
          </div>
        </Card>

        <Card className="max-w-sm">
          <h5 className="text-2xl font-bold tracking-tight text-gray-900">
            プラットフォームについて
          </h5>
          <p className="font-normal text-gray-700">
            PPPの詳細や使い方について詳しく知りたい方はこちら。
          </p>
          <Button as={Link} to="/about">
            詳細を見る
          </Button>
        </Card>
      </div>
    </div>
  );
}

export default function Home() {
  console.log("show home");
  return (
      <HomePage />
  );
}

export function meta() {
  return [
    { title: "Personalized Podcast Platform - ホーム" },
    { name: "description", content: "パーソナライズされたAIポッドキャストプラットフォーム" },
  ];
}
