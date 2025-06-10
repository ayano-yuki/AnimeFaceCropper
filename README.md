# AnimeFaceCropper
アニメ画像から顔を検出し、オプションで超解像（Super Resolution）を適用して指定サイズに変換するツールです。  
Docker 上で動作し、GPU 不要・CPU 環境で実行可能です。

## 機能概要
- `input/` フォルダ内のアニメ画像から顔を検出
- 顔部分を切り出して `output/` フォルダに保存
- オプションで Real-ESRGAN による超解像を適用（初期値は無効）

## フォルダ構成
```sh
./
├── app/
│ ├── main.py
│ ├── detect_faces.py
│ ├── super_resolve.py
│ └── utils.py
├── input/              # 顔検出対象となる画像 .jpg .jpeg .png .webp .bmp
├── output/             # 出力される顔画像(フォルダーは実行時から必須) .png
├── requirements.txt
├── Dockerfile
└── README.md
```

## 実行方法（Windows + Docker）
1. イメージをビルド
    ```powershell   
    docker build -t anime-face-up .
    ```
1.入力画像を配置
    input/ フォルダに .jpg, .png などの画像を入れます。
1. コンテナを実行
    ```powershell
    docker run --rm ^
    -v "${PWD}\input:/app/input" ^
    -v "${PWD}\output:/app/output" ^
    anime-face-up
    ```

    超解像オプションは通常時は無効化されています。
    超解像を有効にしたい場合、環境変数 UPSCALE=true を指定してください。
    ```powershell
    docker run --rm ^
    -v "${PWD}\input:/app/input" ^
    -v "${PWD}\output:/app/output" ^
    -e UPSCALE=true ^
    anime-face-up
   ```
