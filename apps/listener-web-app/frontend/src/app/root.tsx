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

import {Links, Meta, Outlet, Scripts, ScrollRestoration} from "react-router";
import Provider from '@/provider'

import "../index.css";
import {ThemeConfig} from "flowbite-react";
import Header from '@/components/Header';
import ChatUI from "@/components/ChatUI";

export default function App() {
    return (
        <html lang="ja">
        <head>
            <meta charSet="utf-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1"/>
            <link rel="icon" href="/favicon.ico" />
            <Meta/>
            <Links/>
        </head>
        <body>
        <ThemeConfig dark={false}/>
        <div className="min-h-screen bg-gray-50">
            <Provider>
                <Header/>
                <main className="mx-auto px-4 py-4">
                    <Outlet/>
                </main>
                <ChatUI agentName="P3-CO" appName="concierge" icon="/p3-co.png" />
            </Provider>
        </div>

        <ScrollRestoration/>
        <Scripts/>
        </body>
        </html>
    );
}

export function ErrorBoundary() {
    return (
        <html lang="ja">
        <head>
            <meta charSet="utf-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1"/>
            <Meta/>
            <Links/>
            <title>エラーが発生しました</title>
        </head>
        <body>
        <ThemeConfig dark={false}/>
        <div className="min-h-screen bg-gray-50">
            <Provider>
                <Header/>
                <div className="flex items-center justify-center py-20">
                    <div className="text-center">
                        <h1 className="text-2xl font-bold text-red-600">エラーが発生しました</h1>
                        <p className="mt-2">申し訳ありませんが、問題が発生しました。</p>
                    </div>
                </div>
            </Provider>
        </div>
        <ScrollRestoration/>
        <Scripts/>
        </body>
        </html>
    );
}
