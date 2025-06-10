import cv2
import os

# パス設定
INPUT_DIR = "input"
OUTPUT_DIR = "output"
CASCADE_PATH = "lbpcascade_animeface.xml"
FACE_SIZE = (128, 128)  # 出力画像のサイズ（幅, 高さ）

# 出力フォルダ作成
os.makedirs(OUTPUT_DIR, exist_ok=True)

# カスケード分類器の読み込み
if not os.path.exists(CASCADE_PATH):
    raise FileNotFoundError(f"カスケードファイルが見つかりません: {CASCADE_PATH}")
cascade = cv2.CascadeClassifier(CASCADE_PATH)

# 入力画像の処理
image_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith((".jpg", ".png", ".jpeg"))]

for img_file in image_files:
    img_path = os.path.join(INPUT_DIR, img_file)
    img = cv2.imread(img_path)
    if img is None:
        print(f"画像が読み込めません: {img_file}")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(24, 24))

    for i, (x, y, w, h) in enumerate(faces):
        face_img = img[y:y+h, x:x+w]
        face_resized = cv2.resize(face_img, FACE_SIZE)
        out_name = f"{os.path.splitext(img_file)[0]}_face{i}.png"
        out_path = os.path.join(OUTPUT_DIR, out_name)
        cv2.imwrite(out_path, face_resized)

    print(f"{img_file}: {len(faces)} 個の顔を検出")

print("完了しました。")
