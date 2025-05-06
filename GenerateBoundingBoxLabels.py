import pandas as pd
import os
from PIL import Image

# =============================
# Configurações iniciais
# =============================
csv_path     = 'test.csv'       # caminho para o CSV de trajetórias
img_folder   = 'Frames'          # pasta onde estão os frames gerados
img_ext      = 'png'             # extensão dos frames (png ou jpg)
fixed_width  = 30                # largura fixa da bounding box em pixels
fixed_height = 30                # altura fixa da bounding box em pixels

# =============================
# 1. Carrega e limpa o CSV
# =============================
df = pd.read_csv(csv_path)
df['Frame'] = pd.to_numeric(df['Frame'], errors='coerce')
df = df.dropna(subset=['Video', 'Frame', 'Px', 'Py', 'Class'])
df['Frame'] = df['Frame'].astype(int)

# =============================
# 2. Agrupa por vídeo e frame
# =============================
grouped = df.groupby(['Video', 'Frame'])

# =============================
# 3. Processa cada grupo
# =============================
for (video, frame_num), group in grouped:
    # nome do arquivo de imagem: P1_frame_000000.png
    img_name = f"{video}_frame_{frame_num:06d}.{img_ext}"
    img_path = os.path.join(img_folder, img_name)

    # verifica existência da imagem
    if not os.path.isfile(img_path):
        print(f"[AVISO] Imagem não encontrada: {img_path}")
        continue

    # abre a imagem para obter largura e altura
    try:
        with Image.open(img_path) as img:
            img_w, img_h = img.size
    except Exception as e:
        print(f"[AVISO] Erro ao abrir {img_path}: {e}")
        continue

    # monta caminho do arquivo de label: P1_frame_000000.txt
    txt_name = f"{video}_frame_{frame_num:06d}.txt"
    txt_path = os.path.join(img_folder, txt_name)

    # escreve as anotações no formato YOLO
    with open(txt_path, 'w') as f:
        for _, row in group.iterrows():
            class_id = int(row['Class'])
            px = float(row['Px'])
            py = float(row['Py'])
            x_center = px / img_w
            y_center = py / img_h
            w_norm = fixed_width / img_w
            h_norm = fixed_height / img_h
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}\n")

print("✔️ Geração de arquivos de label concluída.")
