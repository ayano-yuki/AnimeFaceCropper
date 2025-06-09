# 現時点では未使用（将来的に画像補助関数を入れる用）

def ensure_rgb(image):
    if image.mode != 'RGB':
        return image.convert('RGB')
    return image
