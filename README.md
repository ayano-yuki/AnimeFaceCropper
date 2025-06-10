# AnimeFaceCropper
アニメ画像から顔を検出し、指定サイズに切り抜くプログラム

## 機能概要
- `input/` フォルダ内のアニメ画像から顔を検出
- 顔部分を切り出して `output/` フォルダに保存

## フォルダ構成
```sh
./
├── input/              # 顔検出対象となる画像
├── output/             # 出力される顔画像
├── main.py
└── README.md
```

## 実行方法（Windows + Docker）
1. OpenCVのインストール
    ```powershell   
    pip install opencv-python
    ```
1. プログラムの実行