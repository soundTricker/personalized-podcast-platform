# パーソナライズドポッドキャストプラットフォーム（PPP）リスナーWebアプリについて

このプロジェクトは個人向けAI Podcast生成プラットフォーム「Personalized Podcast Platform（通称: PPP）」のサブアプリケーションで、ユーザー（リスナー）向けのWeb UI/APIプロジェクトです。

## プロジェクト構成

プロジェクトは以下の2つの主要部分から構成されています：

1. **フロントエンド（Web UI）**
   - `frontend` ディレクトリに配置
   - ユーザーインターフェースを提供

2. **バックエンド（API）**
   - `backend` ディレクトリに配置
   - データの保存・取得・処理を担当

## 技術スタック

### フロントエンド
- **環境管理**: mise
- **Node.js**: v22.16.0
- **フレームワーク**: React.js v19
- **ビルドツール**: Vite
- **スタイリング**: TailwindCSS v4.1.8, Flowbite React
- **状態管理**: TanStack Query
- **ルーティング**: React Router v7 (framework mode)
- **API連携**: OpenAPI自動生成 (@7nohe/openapi-react-query-codegen)
- **認証**: Firebase Authentication
- **リンター**: ESLint

### バックエンド
- **環境管理**: mise
- **パッケージ管理**: uv
- **言語**: Python 3.12
- **APIフレームワーク**: FastAPI
- **データベース**: Firestore (Firedantic使用)
- **認証**: Firebase Authentication
- **フォーマッター**: ruff (select: E,F,I)
- **タイプチェッカー**: ty
- **テスト**: pytest
- **ローカル開発**: Docker Compose + Firebase Emulator Suite

## 開発環境セットアップ

### バックエンド
1. Docker Composeを使用して開発環境を起動:
   ```bash
   cd backend
   docker-compose -f docker-compose.dev.yml up
   ```
   これにより、FastAPIサーバーとFirebase Emulatorが起動します。
   - FastAPIサーバー: http://localhost:8000
   - Firebase Emulator UI: http://localhost:4000

### フロントエンド
1. 依存関係をインストール:
   ```bash
   cd frontend
   npm install
   ```

2. 開発サーバーを起動:
   ```bash
   npm run dev
   ```

3. APIクライアントコードの生成（バックエンドが起動している必要があります）:
   ```bash
   npm run codegen
   ```

## テスト

### バックエンド
- pytestを使用してテストを実行:
  ```bash
  cd backend
  pytest
  ```

### フロントエンド
- ESLintを使用してコードをリント:
  ```bash
  cd frontend
  npm run lint
  ```

## コード規約

### 共通
- 回答や説明は常に日本語を使用
- ファイル内のコメントは英語を使用
- タスクを実行後は必ずコード上にエラーがないか、コンパイルエラーが発生していないかをチェックし修正すること

### フロントエンド
- ESLintの規約に従う
- React Router v7はframework modeを使用
- dark modeは無効化
- ボタンは右寄せ
- React Routerのactionは利用せず、バックエンドとのやり取りはすべて、`frontend/generated/api` 以下に保存されている serviceやhooksを利用する このファイルは openapi より作成されたファイル群です。 
- ルートを追加した場合は `fronend/src/app/routes.ts` にパスを追加すること
- ルートを追加後は `npm run typeegen` を実行すること
- コード生成後は必ず `npm run lint` を実行しリントエラーがあるかチェックしエラーがあれば修正すること

### バックエンド
- Google Style Guideに準拠
- PEP 8に可能な限り準拠
- 1行あたり最大200文字
- Pythonの文字列はダブルクォート使用
- 文字列フォーマットはf文字列を使用
- コードを修正した後は `uv run ty check` `uv run ruff format` `uv run ruff check --fix`を実行し、エラーがないかチェックすること エラーがあれば修正すること
- apiの追加・修正や、パラメータの修正をした後は　必ず frontendディレクトリにて、 `npm run codegen` を実行すること


## プロジェクト構造

### バックエンド
```
backend/
├── main.py                 # uvicornを使用してFastAPIを起動
├── ppp/                    # メインパッケージ
│   ├── __init__.py
│   ├── main.py             # FastAPIアプリケーションインスタンス
│   ├── models/             # Firedanticモデル
│   ├── firestore/          # Firestoreクライアント管理
│   ├── schemas/            # Pydanticスキーマ
│   ├── services/           # ビジネスロジック
│   ├── mcp/                # fastapi-mcp用のAPIルーター (基本的にfastapiと同じ)
│   │   ├── mcp.py          # mcpルーター集約
│   │   └── endpoints/      # エンドポイント定義
│   ├── api/                # APIルーター
│   │   └── v1/             # v1 API
│   │       ├── api.py      # v1ルーター集約
│   │       └── endpoints/  # エンドポイント定義
│   └── utils/              # ユーティリティ
└── tests/                  # テストコード
```
