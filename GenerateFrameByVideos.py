import cv2
import os

def video_to_frames(video_path, output_folder, prefix='frame', ext='jpg'):

    os.makedirs(output_folder, exist_ok=True)
    

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break 
        

        frame_filename = os.path.join(output_folder, f"{prefix}_{frame_count:05d}.{ext}")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    
    cap.release()
    print(f"Extração completa: {frame_count} frames salvos em '{output_folder}'.")

video_to_frames('C:/Users/gomes/Documents/Artigos/videos/train/P1.avi', 'Frames/')
