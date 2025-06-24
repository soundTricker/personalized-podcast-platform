# パーソナライズドポッドキャストプラットフォーム（PPP）リスナーWebアプリ

このプロジェクトは個人向けAI Podcast生成プラットフォーム「Personalized Podcast Platform（通称: PPP）」のサブアプリケーションで、ユーザー（リスナー）向けのWeb UI/APIプロジェクトです。

## 📋 目次

- [プロジェクト構成](#プロジェクト構成)
- [技術スタック](#技術スタック)
- [開発環境セットアップ](#開発環境セットアップ)
- [テスト](#テスト)
- [コード規約](#コード規約)
- [プロジェクト構造](#プロジェクト構造)
- [デプロイメント](#デプロイメント)

## 🏗️ プロジェクト構成

プロジェクトは以下の2つの主要部分から構成されています：

### 1. **フロントエンド（Web UI）**
- `frontend` ディレクトリに配置
- ユーザーインターフェースを提供
- React.js v19ベースのモダンなWebアプリケーション

### 2. **バックエンド（API）**
- `backend` ディレクトリに配置
- データの保存・取得・処理を担当
- FastAPIベースのRESTful API

## 🛠️ 技術スタック

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

## 🚀 開発環境セットアップ

### 前提条件
- Docker & Docker Compose
- Node.js v22.16.0
- Python 3.12
- mise
- uv

### バックエンド開発環境

1. **Docker Composeを使用した開発環境の起動**:
   ```bash
   cd backend
   docker-compose -f docker-compose.dev.yml up
   ```
   
   これにより以下のサービスが起動します：
   - **FastAPIサーバー**: http://localhost:8000
   - **Firebase Emulator UI**: http://localhost:4000

2. **APIドキュメント**:
   - Swagger UI: http://localhost:8000/docs

3. **開発環境の停止**:
   ```bash
   docker-compose -f docker-compose.dev.yml down
   ```

### フロントエンド開発環境

1. **依存関係のインストール**:
   ```bash
   cd frontend
   npm install
   ```

2. **開発サーバーの起動**:
   ```bash
   npm run dev
   ```

3. **APIクライアントコードの生成**（バックエンドが起動している必要があります）:
   ```bash
   npm run codegen
   ```

4. **型定義の生成**（ルート追加後）:
   ```bash
   npm run typegen
   ```

## 🧪 テスト

### バックエンドテスト
```bash
cd backend
pytest
```

### フロントエンドテスト
```bash
cd frontend
npm run lint
```

## 📝 コード規約

### 共通規約
- **言語**: 回答や説明は常に日本語を使用
- **コメント**: ファイル内のコメントは英語を使用
- **品質管理**: タスク実行後は必ずコンパイルエラーがないかチェックし修正すること

### フロントエンド規約
- ESLintの規約に従う
- React Router v7はframework modeを使用
- dark modeは無効化
- ボタンは右寄せ
- React Routerのactionは利用せず、バックエンドとのやり取りはすべて`frontend/generated/api`以下のserviceやhooksを利用
- ルート追加時は`frontend/src/app/routes.ts`にパスを追加
- ルート追加後は`npm run typegen`を実行
- コード生成後は必ず`npm run lint`を実行しエラーを修正

### バックエンド規約
- Google Style Guideに準拠
- PEP 8に可能な限り準拠
- 1行あたり最大200文字
- Pythonの文字列はダブルクォート使用
- 文字列フォーマットはf文字列を使用
- コード修正後は以下を実行：
  ```bash
  uv run ty check
  uv run ruff format
  uv run ruff check --fix
  ```
- API追加・修正後は必ずフロントエンドで`npm run codegen`を実行

## 📁 プロジェクト構造

```
listener-web-app/
├── README.md                   # このファイル
├── backend/                    # バックエンドAPI
│   ├── main.py                 # uvicornを使用してFastAPIを起動
│   ├── ppp/                    # メインパッケージ
│   │   ├── __init__.py
│   │   ├── main.py             # FastAPIアプリケーションインスタンス
│   │   ├── models/             # Firedanticモデル
│   │   ├── firestore/          # Firestoreクライアント管理
│   │   ├── schemas/            # Pydanticスキーマ
│   │   ├── services/           # ビジネスロジック
│   │   ├── mcp/                # fastapi-mcp用のAPIルーター
│   │   │   ├── mcp.py          # mcpルーター集約
│   │   │   └── endpoints/      # エンドポイント定義
│   │   ├── api/                # APIルーター
│   │   │   └── v1/             # v1 API
│   │   │       ├── api.py      # v1ルーター集約
│   │   │       └── endpoints/  # エンドポイント定義
│   │   └── utils/              # ユーティリティ
│   └── tests/                  # テストコード
├── frontend/                   # フロントエンドWebアプリ
│   ├── src/                    # ソースコード
│   ├── generated/              # OpenAPIから自動生成されたコード
│   ├── public/                 # 静的ファイル
│   ├── package.json            # Node.js依存関係
│   └── vite.config.ts          # Vite設定
├── compose.yaml                # Docker Compose設定（本番用）
├── cloudbuild.yaml             # Google Cloud Build設定
├── services.yaml               # Google Cloud Run設定
└── nginx.conf                  # Nginx設定
```

## 🚢 デプロイメント

### ローカル開発
- バックエンド: Docker Compose + Firebase Emulator
- フロントエンド: Vite開発サーバー

### 本番環境
- Google Cloud Run
- Firebase Authentication & Firestore
- Cloud Build による自動デプロイ

## 🔧 開発ワークフロー

1. **バックエンド開発**:
   ```bash
   cd backend
   docker-compose -f docker-compose.dev.yml up
   ```

2. **フロントエンド開発**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **API変更時**:
   ```bash
   # バックエンドでAPI変更後
   cd frontend
   npm run codegen
   npm run lint
   ```

4. **ルート追加時**:
   ```bash
   # frontend/src/app/routes.ts を更新後
   npm run typegen
   npm run lint
   ```

## 📚 参考資料

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React.js Documentation](https://react.dev/)
- [Firebase Documentation](https://firebase.google.com/docs)
- [TailwindCSS Documentation](https://tailwindcss.com/docs)
- [Vite Documentation](https://vitejs.dev/)

## 🤝 コントリビューション

1. 開発前に必ずコード規約を確認
2. テストを実行してエラーがないことを確認
3. リントエラーを修正
4. 適切なコミットメッセージを記述

---

**Note**: このプロジェクトは継続的に開発中です。最新の情報については、各ディレクトリ内のREADMEファイルも参照してください。