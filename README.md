# パーソナライズドポッドキャストプラットフォーム（PPP）

個人向けAI Podcast生成プラットフォーム「Personalized Podcast Platform（通称: PPP）」は、AIエージェントを活用してパーソナライズされたポッドキャスト番組を自動生成し、ユーザーに配信するプラットフォームです。

## 🎯 プロジェクト概要

PPPは、ユーザーの興味や嗜好に基づいて、AIが自動的にコンテンツを収集・分析・編集し、個人専用のポッドキャスト番組を生成します。リアルタイムの情報収集から音声合成まで、完全に自動化されたワークフローを提供します。

## 📋 目次

- [アーキテクチャ](#アーキテクチャ)
- [アプリケーション構成](#アプリケーション構成)
- [技術スタック](#技術スタック)
- [開発環境セットアップ](#開発環境セットアップ)
- [プロジェクト構造](#プロジェクト構造)
- [開発ワークフロー](#開発ワークフロー)
- [コントリビューション](#コントリビューション)

## 🏗️ アーキテクチャ

PPPは以下の2つの主要アプリケーションで構成されています：

```
┌─────────────────────────────────────────────────────────────┐
│                    PPP Platform                             │
├─────────────────────────────────────────────────────────────┤
│  👥 Listener Web App          🎙️ Radio Station             │
│  ┌─────────────────────┐      ┌─────────────────────────┐    │
│  │   React Frontend    │      │    AI Agent System     │    │
│  │   ┌─────────────┐   │      │   ┌─────────────────┐   │    │
│  │   │   Web UI    │   │◄────►│   │  Content Agent  │   │    │
│  │   └─────────────┘   │      │   ├─────────────────┤   │    │
│  │   FastAPI Backend   │      │   │ Research Agent  │   │    │
│  │   ┌─────────────┐   │      │   ├─────────────────┤   │    │
│  │   │ REST API    │   │      │   │  Writer Agent   │   │    │
│  │   │ Firebase    │   │      │   ├─────────────────┤   │    │
│  │   │ Firestore   │   │      │   │ Composer Agent  │   │    │
│  │   └─────────────┘   │      │   └─────────────────┘   │    │
│  └─────────────────────┘      └─────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 アプリケーション構成

### 1. 👥 Listener Web App
**ユーザー向けWebアプリケーション**

- **目的**: リスナー（ユーザー）がポッドキャストを視聴・管理するためのWebインターフェース
- **場所**: `apps/listener-web-app/`
- **構成**: 
  - React.js v19 フロントエンド
  - FastAPI バックエンド
  - Firebase Authentication & Firestore

**主な機能**:
- ユーザー認証・プロフィール管理
- ポッドキャスト番組の視聴
- 番組履歴

### 2. 🎙️ Radio Station
**AI番組制作システム**

- **目的**: AIエージェントを使用してパーソナライズされたポッドキャスト番組を自動生成
- **場所**: `apps/radio-station/`
- **構成**: Python + Google ADK (Agent Development Kit)

**主な機能**:
- **Research Agent**: RSS・Web情報の収集・分析
- **Writer Agent**: コンテンツの執筆・編集
- **Composer Agent**: 音声合成・番組構成
- **Flow Agent**: ワークフロー管理・調整

## 🛠️ 技術スタック

### Listener Web App
| 分野 | 技術 |
|------|------|
| **フロントエンド** | React.js v19, Vite, TailwindCSS, React Router v7 |
| **バックエンド** | Python 3.12, FastAPI, Firedantic |
| **データベース** | Firebase Firestore |
| **認証** | Firebase Authentication |
| **開発環境** | Docker Compose, Firebase Emulator |
| **テスト** | pytest, ESLint |

### Radio Station
| 分野 | 技術 |
|------|------|
| **AI Framework** | Google ADK (Agent Development Kit) |
| **言語** | Python 3.12 |
| **パッケージ管理** | uv |
| **テスト** | pytest |
| **フォーマット** | ruff |

## 🚀 開発環境セットアップ

### 前提条件
- Docker & Docker Compose
- Node.js v22.16.0
- Python 3.12
- mise
- uv

### 1. Listener Web App

#### バックエンド
```bash
cd apps/listener-web-app/backend
docker-compose -f docker-compose.dev.yml up
```
- FastAPI: http://localhost:8000
- Firebase Emulator: http://localhost:4000

#### フロントエンド
```bash
cd apps/listener-web-app/frontend
npm install
npm run dev
```

### 2. Radio Station
```bash
cd apps/radio-station
uv pip install -e .
python main.py
```

## 📁 プロジェクト構造

```
personalized-podcast-platform/
├── README.md                          # このファイル
├── LICENSE                            # ライセンス
├── mise.toml                          # 環境管理設定
├── .gitignore                         # Git除外設定
└── apps/                              # アプリケーション群
    ├── listener-web-app/              # リスナー向けWebアプリ
    │   ├── README.md                  # Webアプリ詳細ドキュメント
    │   ├── frontend/                  # React.js フロントエンド
    │   │   ├── src/                   # ソースコード
    │   │   ├── generated/             # OpenAPI自動生成コード
    │   │   └── package.json           # Node.js依存関係
    │   ├── backend/                   # FastAPI バックエンド
    │   │   ├── ppp/                   # メインパッケージ
    │   │   │   ├── api/               # APIルーター
    │   │   │   ├── models/            # データモデル
    │   │   │   ├── services/          # ビジネスロジック
    │   │   │   └── utils/             # ユーティリティ
    │   │   └── tests/                 # テストコード
    │   ├── compose.yaml               # Docker Compose設定
    │   └── cloudbuild.yaml            # Cloud Build設定
    └── radio-station/                 # AI番組制作システム
        ├── README.md                  # Radio Station詳細ドキュメント
        ├── main.py                    # エントリーポイント
        ├── pyproject.toml             # Python依存関係
        ├── radio_station/             # メインパッケージ
        │   ├── agent.py               # メインエージェント
        │   ├── model/                 # データモデル
        │   ├── services/              # 外部サービス連携
        │   ├── sub_agents/            # サブエージェント群
        │   │   ├── researcher/        # 情報収集エージェント
        │   │   ├── writer.py          # 執筆エージェント
        │   │   └── composer.py        # 音声合成エージェント
        │   └── tools/                 # ユーティリティツール
        └── tests/                     # テストコード
            ├── unittests/             # 単体テスト
            └── integrations/          # 統合テスト
```

## 🔄 開発ワークフロー

### 1. 新機能開発
```bash
# 1. リポジトリクローン
git clone <repository-url>
cd personalized-podcast-platform

# 2. 対象アプリケーションで開発
cd apps/listener-web-app  # または apps/radio-station

# 3. 開発環境起動（各アプリのREADME参照）

# 4. 開発・テスト

# 5. コミット・プッシュ
```

### 2. API変更時（Listener Web App）
```bash
# バックエンドでAPI変更後
cd apps/listener-web-app/frontend
npm run codegen  # OpenAPIからクライアントコード生成
npm run lint     # リント実行
```

### 3. エージェント評価（Radio Station）
```bash
cd apps/radio-station
pytest tests/integrations/  # エージェント統合テスト
uv run ruff format          # コードフォーマット
```

## 🧪 テスト戦略

### Listener Web App
- **フロントエンド**: ESLint による静的解析
- **バックエンド**: pytest による単体・統合テスト
- **API**: OpenAPI仕様に基づく自動テスト

### Radio Station
- **単体テスト**: 各エージェントの個別機能テスト
- **統合テスト**: エージェント間連携テスト
- **評価テスト**: ADKを使用したエージェント性能評価

## 📚 詳細ドキュメント

各アプリケーションの詳細な開発ガイドは、それぞれのREADMEファイルを参照してください：

- **Listener Web App**: [`apps/listener-web-app/README.md`](apps/listener-web-app/README.md)
- **Radio Station**: [`apps/radio-station/README.md`](apps/radio-station/README.md)

## 🤝 コントリビューション

### 開発規約
- **言語**: ドキュメント・説明は日本語、コード内コメントは英語
- **コードスタイル**: 各アプリケーションの規約に従う
- **テスト**: 新機能には必ずテストを追加
- **コミット**: 意味のある単位でコミットし、適切なメッセージを記述

### プルリクエスト
1. 機能ブランチを作成
2. 開発・テスト実行
3. コードレビュー依頼
4. マージ

## 📄 ライセンス

このプロジェクトは [LICENSE](LICENSE) ファイルに記載されたライセンスの下で公開されています。

---

**Note**: このプラットフォームは継続的に開発中です。最新の情報については、各アプリケーションのドキュメントも併せて確認してください。