import os
import cv2


augmented_root = "augmented"
positive_folders = ["7-1", "7-2", "7-3", "7-4", "7-5"]  
output_folder = "haar_training_pack"
positive_txt = os.path.join(output_folder, "positives.txt")
negative_txt = os.path.join(output_folder, "bg.txt")
target_w, target_h = 50, 50  

os.makedirs(output_folder, exist_ok=True)


pos_lines = []
for folder in positive_folders:
    folder_path = os.path.join(augmented_root, folder)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".png", ".jpeg", ".bmp")):
            relative_path = f"{folder}/{filename}"
            line = f"{relative_path} 1 0 0 {target_w} {target_h}"
            pos_lines.append(line)

with open(positive_txt, "w") as f:
    for line in pos_lines:
        f.write(line + "\n")

print(f" 已產出正樣本 {len(pos_lines)} 筆 → {positive_txt}")


neg_lines = []
for folder in os.listdir(augmented_root):
    if folder not in positive_folders:
        folder_path = os.path.join(augmented_root, folder)
        for filename in os.listdir(folder_path):
            if filename.lower().endswith((".jpg", ".png", ".jpeg", ".bmp")):
                relative_path = f"{folder}/{filename}"
                neg_lines.append(relative_path)

with open(negative_txt, "w") as f:
    for line in neg_lines:
        f.write(line + "\n")

print(f" 已產出負樣本 {len(neg_lines)} 筆 → {negative_txt}")
