import cv2
import os

valid_lines = []
input_txt = 'haar_training_pack/positives.txt'
output_txt = 'haar_training_pack/positives_cleaned.txt'
min_width, min_height = 50, 50

with open(input_txt, 'r') as f:
    for line in f:
        tokens = line.strip().split()
        if len(tokens) >= 6:
            img_rel_path = tokens[0]
            img_path = os.path.join(*img_rel_path.split('/'))


            if not os.path.isfile(img_path):
                print(f'❌ 檔案不存在: {img_path}')
                continue

            img = cv2.imread(img_path)
            if img is None:
                print(f'⚠️ 無法讀入 (格式錯誤或損毀): {img_path}')
                continue

            h, w = img.shape[:2]
            if w < min_width or h < min_height:
                print(f'❌ 圖片太小 ({w}x{h})，跳過: {img_path}')
                continue

            valid_lines.append(line.strip())

# 寫入清理過的新檔案
with open(output_txt, 'w') as f:
    for line in valid_lines:
        f.write(line + '\n')

print(f'✅ 完成 ✔️ 留下 {len(valid_lines)} 筆有效樣本')
