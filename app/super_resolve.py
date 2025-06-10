from PIL import Image
import torch
from realesrgan import RealESRGANer  # ← これを追加

def upscale_image(image: Image.Image, target_size: int = 512):
    device = torch.device('cpu')  # 強制的にCPU使用

    # モデルの初期化（weights は事前に取得 or 自動DLされる想定）
    model = RealESRGANer(
        scale=4,
        model_path='weights/RealESRGAN_x4.pth',  # ローカルにあるか、model=None で自動DL
        device=device
    )

    # 推論
    sr_image, _ = model.enhance(image)
    return sr_image.resize((target_size, target_size), Image.LANCZOS)
