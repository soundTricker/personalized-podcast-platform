# PPP Listener Web App Backend

バックエンドAPIサービスは、FastAPIを使用して構築されたRESTful APIです。

## 開発環境のセットアップ

### Dockerを使用した開発環境

このプロジェクトはDockerを使用して開発環境を簡単にセットアップできます。

#### 前提条件

- Docker
- Docker Compose

#### 開発環境の起動

1. リポジトリのルートディレクトリから以下のコマンドを実行します：

```bash
cd backend
docker-compose -f docker-compose.dev.yml up --build
```

2. APIサービスは http://localhost:8000 で利用可能になります。
3. Firebase Emulator UI は http://localhost:4000 で利用可能になります。

#### 開発環境の停止

```bash
docker-compose -f docker-compose.dev.yml down
```

### ローカル環境での開発（Docker不使用）

#### 前提条件

- Python 3.12
- mise
- uv

#### セットアップ

1. 依存関係のインストール：

```bash
uv pip install -e .
```

2. アプリケーションの起動：

```bash
python main.py
```

## APIドキュメント

アプリケーション起動後、以下のURLでSwagger UIを使用したAPIドキュメントにアクセスできます：

- http://localhost:8000/docs

## Firebase Emulator

開発環境では、Firebase Emulatorを使用してFirestoreとFirebase Authenticationをローカルで利用できます。

### Emulator UI

- http://localhost:4000

### 環境変数の設定

アプリケーションがFirebase Emulatorを使用するように、以下の環境変数を設定してください：

```bash
export FIRESTORE_EMULATOR_HOST="localhost:9199"
export FIREBASE_AUTH_EMULATOR_HOST="localhost:9099"
```

Docker Compose環境では、これらの環境変数が自動的に設定されます。

## 技術スタック

- Python 3.12
- FastAPI
- Firedantic
- Firebase Admin SDK
- Uvicorn
- Pytest
- Ruff (フォーマッタ)
- Ty (タイプチェッカー)
