import cv2
import os
import glob

def video_to_frames(video_path, output_folder, ext='png'):
    """
    Extrai todos os frames de um único vídeo, salvando em output_folder
    com nome <VideoID>_frame_<000000>.<ext>.
    """
    os.makedirs(output_folder, exist_ok=True)
    video_id = os.path.splitext(os.path.basename(video_path))[0]
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[ERRO] Não conseguiu abrir: {video_path}")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        filename = f"{video_id}_frame_{frame_count:06d}.{ext}"
        filepath = os.path.join(output_folder, filename)
        cv2.imwrite(filepath, frame)
        frame_count += 1

    cap.release()
    print(f"✅ Extraídos {frame_count} frames de {video_id}")

def extract_all(videos_folder, output_folder, ext='png'):
    """
    Percorre todos os arquivos .avi em videos_folder e extrai seus frames.
    """
    pattern = os.path.join(videos_folder, '*.avi')
    video_paths = sorted(glob.glob(pattern))
    if not video_paths:
        print(f"[AVISO] Nenhum vídeo encontrado em: {videos_folder}")
        return

    for video_path in video_paths:
        video_to_frames(video_path, output_folder, ext=ext)

if __name__ == "__main__":
    # Ajuste estes caminhos conforme sua estrutura local:
    VIDEOS_FOLDER = r'C:/Users/gomes/Documents/Artigos/videos/test'
    OUTPUT_FOLDER = r'C:/Users/gomes/Documents/Artigos/Frames'
    IMAGE_FORMAT  = 'png'  # ou 'jpg'

    extract_all(VIDEOS_FOLDER, OUTPUT_FOLDER, ext=IMAGE_FORMAT)
    print("✔️ Extração de frames completa para todos os vídeos.")
