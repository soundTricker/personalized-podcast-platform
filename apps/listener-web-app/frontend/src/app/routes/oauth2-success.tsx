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

import { useEffect } from "react";

export default function OAuth2Success() {
  useEffect(() => {
    // Send message to parent window
    if (window.opener) {
      window.opener.postMessage("oauth2-success", window.origin);
      // Close this window
      window.close();
    }
  }, []);

  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="text-center">
        <h1 className="text-2xl font-bold mb-4">認証成功</h1>
        <p>Google APIの認証に成功しました。このウィンドウは自動的に閉じられます。</p>
        <p className="mt-4">
          ウィンドウが閉じない場合は、
          <button
            onClick={() => window.close()}
            className="text-blue-600 hover:underline"
          >
            こちら
          </button>
          をクリックしてください。
        </p>
      </div>
    </div>
  );
}

export function meta() {
  return [
    { title: "Google API認証成功 - Personalized Podcast Platform" },
    { name: "description", content: "Google APIの認証に成功しました" },
  ];
}