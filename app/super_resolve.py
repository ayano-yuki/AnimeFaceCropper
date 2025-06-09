from realesrgan import RealESRGAN
from PIL import Image
import torch

def upscale_image(image: Image.Image, target_size: int = 512):
    device = torch.device('cpu')  # 強制的にCPU使用
    model = RealESRGAN(device, scale=4)
    model.load_weights('weights/RealESRGAN_x4.pth')

    sr_image = model.predict(image)
    return sr_image.resize((target_size, target_size), Image.LANCZOS)
