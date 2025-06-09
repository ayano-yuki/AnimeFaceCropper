# ベースイメージ（Python 3.10 を使用）
FROM python:3.10-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# requirements.txt をコピー
COPY requirements.txt .

# NumPy は最初に旧バージョンを固定インストール
# PyTorch は CPU バージョンをインストール
RUN pip install --no-cache-dir "numpy<2.0" && \
    pip install --no-cache-dir \
        torch==2.0.1+cpu \
        torchvision==0.15.2+cpu \
        -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install --no-cache-dir -r requirements.txt


# アプリケーションのコードをコピー
COPY app/ ./app/

# エントリーポイント（必要なら）
CMD ["python", "app/main.py"]
