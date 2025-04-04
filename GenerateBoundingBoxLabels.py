import pandas as pd
import os
from PIL import Image

fixed_width = 30
fixed_height = 30

csv_path = 'trainVideo1.csv'
img_folder = 'Frames'

# Lê o CSV
df = pd.read_csv(csv_path)
print("Colunas do CSV:", df.columns)

# Converte a coluna 'Frame' para numérico e remove linhas inválidas
df['Frame'] = pd.to_numeric(df['Frame'], errors='coerce')
df = df.dropna(subset=['Frame'])
df['Frame'] = df['Frame'].astype(int)

# Se você quiser trabalhar apenas com um vídeo (por exemplo, P1), pode filtrar:
# df = df[df['Video'] == 'P1']

# Agrupa por frame
grouped = df.groupby('Frame')

for frame_num, group in grouped:
    # Gera o nome da imagem no padrão "frame_00000.jpg", "frame_00001.jpg", etc.
    img_name = f"frame_{frame_num:05d}.jpg"
    print(f"Processando frame: {img_name}")
    
    img_path = os.path.join(img_folder, img_name)
    try:
        with Image.open(img_path) as img:
            img_width, img_height = img.size
    except Exception as e:
        print(f"Erro ao abrir a imagem {img_path}: {e}")
        continue

    # Define o nome do arquivo de label para esse frame
    txt_filename = os.path.splitext(img_name)[0] + '.txt'
    txt_path = os.path.join(img_folder, txt_filename)
    
    with open(txt_path, 'w') as f:
        for _, row in group.iterrows():
            # Converte Px e Py para float
            px = float(row['Px'])
            py = float(row['Py'])
            
            x_center_norm = px / img_width
            y_center_norm = py / img_height
            width_norm = fixed_width / img_width
            height_norm = fixed_height / img_height
            
            # Escreve a linha de anotação no formato YOLO:
            # <classe> <x_center_norm> <y_center_norm> <width_norm> <height_norm>
            f.write(f"0 {x_center_norm} {y_center_norm} {width_norm} {height_norm}\n")
