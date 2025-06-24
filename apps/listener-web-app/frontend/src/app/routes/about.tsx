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
import { Button } from "flowbite-react";

export default function About() {
  return (
    <div className="mx-auto px-4 py-8">
      <header className="mb-12 text-center">
        <h1 className="text-4xl font-bold mb-4">PPPについて</h1>
        <p className="text-xl text-gray-600">パーソナライズドポッドキャストプラットフォームの詳細</p>
      </header>

      <div className="max-w-3xl mx-auto">
        <section className="mb-8">
          <h2 className="text-2xl font-bold mb-4">プラットフォームの概要</h2>
          <p className="mb-4">
            Personalized Podcast Platform (PPP) は、AIを活用して個人の興味や好みに合わせたポッドキャストを自動生成するプラットフォームです。
            最新の情報を取り入れながら、ユーザーごとにカスタマイズされたコンテンツを提供します。
          </p>
          <p>
            従来のポッドキャストとは異なり、PPPではAIがあなたの好みを学習し、常に最適なコンテンツを生成し続けます。
            これにより、情報収集の効率が大幅に向上し、新たな知識や視点を得ることができます。
          </p>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-bold mb-4">主な機能</h2>
          <ul className="list-disc pl-6 space-y-2">
            <li>AIによるパーソナライズされたコンテンツ生成</li>
            <li>最新情報の自動取り込み</li>
            <li>ユーザーの好みに合わせた学習と最適化</li>
            <li>複数のトピックやジャンルに対応</li>
            <li>オフライン再生と同期機能</li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-bold mb-4">利用を開始する</h2>
          <p className="mb-4">
            PPPの利用を開始するには、アカウントを作成し、興味のあるトピックを選択するだけです。
            あとはAIが自動的にあなたに最適なポッドキャストを生成します。
          </p>
        </section>
      </div>
    </div>
  );
}

export function meta() {
  return [
    { title: "PPPについて - Personalized Podcast Platform" },
    { name: "description", content: "パーソナライズドポッドキャストプラットフォーム（PPP）の詳細と機能について" },
  ];
}
