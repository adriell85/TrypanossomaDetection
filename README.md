# Projeto Tcruzi-VMT: Processamento de Vídeos e Anotação YOLO

[LINK DO DATASET TRADUZIDO PARA O FORMATO YOLO!!!!!!!!!!](https://drive.google.com/drive/folders/1zs05BtIpfV7hh7pq5JdibfVmZZPsKDZF?usp=sharing)

Este repositório contém scripts para:
- **Extrair frames** de vídeos (`GenerateFrameByVideos.py`).
- **Gerar labels** em formato YOLO a partir de CSV de trajetórias (`GenerateBoundingBoxLabels.py`).
- **Visualizar** frames anotados individualmente (`VisualizeWithLabelFrames.py`).
- **Criar vídeo** a partir de frames anotados com boxes coloridos por classe (`MakeVídeoByDetectedFrames.py`).

---

## Estrutura de Arquivos

```
├── GenerateFrameByVideos.py        # Extrai frames de todos os vídeos .avi
├── GenerateBoundingBoxLabels.py    # Gera .txt com anotações YOLO para cada frame
├── VisualizeWithLabelFrames.py     # Exibe um frame anotado e salva imagem com boxes
├── MakeVídeoByDetectedFrames.py    # Constrói vídeo a partir de frames + labels, caixas coloridas
├── train.csv / test.csv            # CSVs de trajetórias (Video,Trajectory,Frame,Px,Py,Class)
└── Frames/                         # Pasta onde ficam os frames e labels gerados
```

---

## Pré-requisitos

- Python 3.7+  
- Bibliotecas Python:
  ```bash
  pip install opencv-python pandas pillow
  ```

---

## 1. Gerar Frames a partir dos Vídeos

Use `GenerateFrameByVideos.py` para extrair frames de todos os `.avi`:

```bash
python GenerateFrameByVideos.py
```

Ajuste nas variáveis:
- `VIDEOS_FOLDER`: pasta com arquivos `.avi` (ex.: `videos/train`).
- `OUTPUT_FOLDER`: pasta de saída (`Frames/`).
- `IMAGE_FORMAT`: `png` ou `jpg`.

---

## 2. Criar Labels YOLO a partir do CSV

Execute `GenerateBoundingBoxLabels.py`:

```bash
python GenerateBoundingBoxLabels.py
```

Ajuste:
- `csv_path`: caminho para `train.csv` ou `test.csv`.
- `img_folder`: pasta `Frames/`.
- `img_ext`: extensão dos frames (`png` ou `jpg`).

Isso gera, ao lado de cada frame:
```
P1_frame_000000.txt
P1_frame_000001.txt
...
```
com linhas no formato:
```
<class> <x_center> <y_center> <width> <height>
```

---

## 3. Visualização de Frames Anotados

Para debug, use `VisualizeWithLabelFrames.py`:

```bash
python VisualizeWithLabelFrames.py
```

Ele lê uma imagem e seu `.txt` e salva `output_<frame>.jpg` com as caixas desenhadas.

---

## 4. Montar Vídeo Anotado

Por fim, crie um vídeo com todas as caixas coloridas (azul=célula, verde=parasita) usando:

```bash
python MakeVídeoByDetectedFrames.py
```

Ajuste:
- `FRAMES_DIR`: pasta `Frames/`.
- `OUTPUT_VIDEO`: nome do arquivo AVI de saída.
- `FPS`: frames por segundo do vídeo.

---

## Exemplo de Fluxo Completo

```bash
# 1. Extrair frames
python GenerateFrameByVideos.py

# 2. Gerar labels
python GenerateBoundingBoxLabels.py

# (Opcional) Visualizar um frame
python VisualizeWithLabelFrames.py

# 3. Construir vídeo anotado
python MakeVídeoByDetectedFrames.py
```

Agora você terá:
- Uma pasta `Frames/` com as imagens e .txt.
- Um vídeo `output_with_boxes.avi` contendo todos os frames anotados.

---

## Contato

Qualquer dúvida, entre em contato com o desenvolvedor.


