import cv2
import os
import glob

def draw_bounding_boxes_on_image(image, label_path):
    """
    Desenha todas as bounding boxes do label_path sobre a imagem,
    pintando cada caixa de acordo com a classe (0 ou 1).
    """
    height, width = image.shape[:2]

    with open(label_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        if len(parts) != 5:
            continue

        cls, x_cent_n, y_cent_n, w_n, h_n = parts
        x_center = float(x_cent_n) * width
        y_center = float(y_cent_n) * height
        box_w    = float(w_n) * width
        box_h    = float(h_n) * height

        x_min = int(x_center - box_w / 2)
        y_min = int(y_center - box_h / 2)
        x_max = int(x_center + box_w / 2)
        y_max = int(y_center + box_h / 2)

        # Escolhe cor de acordo com a classe
        if int(cls) == 0:
            color = (255, 0, 0)   # Azul para classe 0
        else:
            color = (0, 255, 0)   # Verde para classe 1

        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 2)

    return image

def create_video_from_frames(frames_folder, output_video_path, fps=30):
    """
    Lê todos os frames .png (ou .jpg) em frames_folder, desenha boxes usando
    os .txt correspondentes pintados por classe, e escreve um vídeo em output_video_path.
    """
    # Encontra todos os .png na pasta
    img_paths = sorted(glob.glob(os.path.join(frames_folder, "*.png")))

    if not img_paths:
        print("Nenhum frame encontrado em:", frames_folder)
        return

    # Prepara VideoWriter com as dimensões do primeiro frame
    first_frame = cv2.imread(img_paths[0])
    h, w = first_frame.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (w, h))
    
    for img_path in img_paths:
        base       = os.path.splitext(os.path.basename(img_path))[0]
        label_path = os.path.join(frames_folder, base + ".txt")

        img = cv2.imread(img_path)
        if img is None:
            print(f"[AVISO] não conseguiu ler {img_path}, pulando.")
            continue
        
        # annotated = draw_bounding_boxes_on_image(img, label_path)

        if os.path.isfile(label_path):
            annotated = draw_bounding_boxes_on_image(img, label_path)
        else:
            annotated = img

        video_writer.write(annotated)

    video_writer.release()
    print(f"✅ Vídeo gerado em: {output_video_path}")

if __name__ == "__main__":
    # Ajuste estes caminhos conforme sua estrutura
    FRAMES_DIR   = "Frames"
    OUTPUT_VIDEO = "output_with_boxes.avi"
    FPS          = 30

    create_video_from_frames(FRAMES_DIR, OUTPUT_VIDEO, FPS)
