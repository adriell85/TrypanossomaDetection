import cv2
import os

def draw_bounding_boxes(img_path, label_path, output_path=None):
    """
    Lê a imagem e o arquivo de label, desenha as bounding boxes e salva a imagem resultante.

    Parâmetros:
      img_path: Caminho para a imagem (frame).
      label_path: Caminho para o arquivo de label (formato YOLO).
      output_path: (Opcional) Caminho para salvar a imagem com as caixas. Se não informado,
                   salva no diretório atual com o prefixo 'output_'.
    """
    # Carrega a imagem
    image = cv2.imread(img_path)
    if image is None:
        print(f"Erro ao ler a imagem: {img_path}")
        return
    height, width = image.shape[:2]

    # Lê o arquivo de label
    try:
        with open(label_path, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Erro ao ler o arquivo de label: {label_path}\n{e}")
        return

    # Processa cada linha do label
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 5:
            continue  # Pula linhas com formato incorreto
        cls, x_center_norm, y_center_norm, w_norm, h_norm = parts
        # Converte os valores normalizados para absolutos
        x_center = float(x_center_norm) * width
        y_center = float(y_center_norm) * height
        box_width = float(w_norm) * width
        box_height = float(h_norm) * height

        # Calcula as coordenadas da caixa: top-left e bottom-right
        x_min = int(x_center - box_width/2)
        y_min = int(y_center - box_height/2)
        x_max = int(x_center + box_width/2)
        y_max = int(y_center + box_height/2)

        # Desenha a caixa na imagem (cor verde, espessura 2)
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    # Define o caminho de saída: se output_path não for fornecido, salva no diretório atual
    if output_path is None:
        base_name = os.path.basename(img_path)
        output_path = os.path.join(os.getcwd(), "output_" + base_name)

    # Salva a imagem com as caixas desenhadas
    cv2.imwrite(output_path, image)
    print(f"Imagem salva com caixas: {output_path}")

# Exemplo de uso:
img_file = 'Frames/frame_00000.jpg'
label_file = 'Frames/frame_00000.txt'
draw_bounding_boxes(img_file, label_file)
