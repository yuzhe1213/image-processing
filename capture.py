import cv2
import os
from datetime import datetime

def extract_frames(video_path, output_root="output", interval=1):
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_dir = os.path.join(output_root, base_name)
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f" 無法開啟影片：{video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        print(" FPS 無法取得，預設為 30")
        fps = 30

    frame_interval = int(fps * interval)
    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            filename = os.path.join(output_dir, f"frame_{saved_count:03d}_{timestamp}.jpg")
            if cv2.imwrite(filename, frame):
                saved_count += 1
            else:
                print(f" 儲存失敗：{filename}")

        frame_count += 1

    cap.release()
    print(f"擷取完成：{video_path} → 共 {saved_count} 張圖片，儲存在 {output_dir}")

def extract_all_videos_from_folder(video_folder, output_root="output", interval=1):
  
    for file in os.listdir(video_folder):
        if file.endswith(".mp4"):
            video_path = os.path.join(video_folder, file)
            extract_frames(video_path, output_root=output_root, interval=interval)


if __name__ == "__main__":
    video_folder = "Final_material"  
    output_root = "output"           
    interval = 1                     

    extract_all_videos_from_folder(video_folder, output_root, interval)
