import cv2
import os
import numpy as np
from datetime import datetime

def augment_image(image):
    h_flip = cv2.flip(image, 1)
    bright = cv2.convertScaleAbs(image, alpha=1.2, beta=30)
    dark = cv2.convertScaleAbs(image, alpha=0.8, beta=-30)
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    angle = np.random.uniform(-15, 15)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), borderMode=cv2.BORDER_REFLECT)
    return [h_flip, bright, dark, rotated]

def augment_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    count = 0

    for fname in os.listdir(input_folder):
        if fname.endswith(".jpg"):
            img_path = os.path.join(input_folder, fname)
            image = cv2.imread(img_path)
            if image is None:
                continue
            base = os.path.splitext(fname)[0]
            # 原圖
            cv2.imwrite(os.path.join(output_folder, f"{base}.jpg"), image)
            # 擴增
            for i, aug in enumerate(augment_image(image)):
                outname = os.path.join(output_folder, f"{base}_aug{i+1}.jpg")
                cv2.imwrite(outname, aug)
            count += 1

    print(f"📁 {input_folder} 擴增完成 → 共 {count * 5} 張圖")

def batch_augment_all(input_root="output", output_root="augmented"):
    if not os.path.exists(input_root):
        print(f"❌ 輸入資料夾不存在：{input_root}")
        return

    for subfolder in os.listdir(input_root):
        input_path = os.path.join(input_root, subfolder)
        if os.path.isdir(input_path):
            output_path = os.path.join(output_root, subfolder)
            augment_folder(input_path, output_path)

# ✅ 執行批次擴增
batch_augment_all("output", "augmented")
