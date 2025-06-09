import os
import argparse
from PIL import Image
from face_detect import detect_faces
from super_resolve import upscale_image

INPUT_DIR = "../input/"
OUTPUT_DIR = "../output/"
TARGET_SIZE = 512
VALID_EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp", ".bmp"]

def is_image_file(filename):
    return any(filename.lower().endswith(ext) for ext in VALID_EXTENSIONS)

def main(upscale=False):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    input_files = [f for f in os.listdir(INPUT_DIR) if is_image_file(f)]

    if not input_files:
        print(f"No valid image files found in {INPUT_DIR}")
        return

    face_count = 0
    for file in input_files:
        image_path = os.path.join(INPUT_DIR, file)
        print(f"Processing: {file}")
        faces = detect_faces(image_path)

        for i, face in enumerate(faces):
            pil_img = Image.fromarray(face[..., ::-1])  # BGR → RGB

            if upscale:
                print(f"  Upscaling face {i} from {file}...")
                pil_img = upscale_image(pil_img, TARGET_SIZE)

            output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(file)[0]}_face_{i}.png")
            pil_img.save(output_path)
            face_count += 1

    print(f"\n✅ Saved {face_count} face(s) from {len(input_files)} image(s) at '{OUTPUT_DIR}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect and optionally upscale anime faces from all images in input/")
    parser.add_argument("--upscale", action="store_true", help="Apply super-resolution to faces")
    args = parser.parse_args()

    main(upscale=args.upscale)
