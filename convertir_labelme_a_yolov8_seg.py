import os
import json
import shutil

# Carpetas donde están los JSON
carpetas_json = [
    r'C:/Users/imeld/Desktop/Gestos/data/Gesto_I',
    r'C:/Users/imeld/Desktop/Gestos/data/Gesto_Perfecto',
    r'C:/Users/imeld/Desktop/Gestos/data/Gesto_Pistola',
    r'C:/Users/imeld/Desktop/Gestos/data/Gesto_puno',
    r'C:/Users/imeld/Desktop/Gestos/data/Gesto_Rock'

]

# Clases y su índice
clases = {
    'Gesto_I': 0,
    'Gesto_Perfecto': 1,
    'Gesto_Pistola': 2,
    'Gesto_puno': 3,
    'Gesto_Rock': 4
}

# Rutas de salida
base = r'C:/Users/imeld/Desktop/Gestos/YOLODataset'
rutas = {
    'train_images': os.path.join(base, 'train/images'),
    'train_labels': os.path.join(base, 'train/labels'),
    'val_images': os.path.join(base, 'val/images'),
    'val_labels': os.path.join(base, 'val/labels')
}

# Crear carpetas
for ruta in rutas.values():
    os.makedirs(ruta, exist_ok=True)

# Procesar
for carpeta in carpetas_json:
    clase_nombre = os.path.basename(carpeta)
    clase_id = clases[clase_nombre]

    archivos_json = sorted([f for f in os.listdir(carpeta) if f.endswith('.json')])

    for i, archivo in enumerate(archivos_json):
        ruta_json = os.path.join(carpeta, archivo)
        with open(ruta_json, 'r') as f:
            datos = json.load(f)

        img_nombre = datos['imagePath']
        ancho = datos['imageWidth']
        alto = datos['imageHeight']
        nombre_base = os.path.splitext(img_nombre)[0]

        # Determinar si va en train o val
        if i <= 40:
            tipo = 'train'
        elif 41 <= i <= 50:
            tipo = 'val'
        else:
            continue  # ignora si pasa de 50

        img_origen = os.path.join(carpeta, img_nombre)
        img_destino = os.path.join(rutas[f'{tipo}_images'], img_nombre)
        txt_destino = os.path.join(rutas[f'{tipo}_labels'], nombre_base + '.txt')

        # Copiar imagen
        if os.path.exists(img_origen):
            shutil.copyfile(img_origen, img_destino)

        # Escribir .txt con segmentación
        with open(txt_destino, 'w') as ftxt:
            for forma in datos['shapes']:
                if forma['shape_type'] == 'polygon':
                    puntos = forma['points']
                    segmento = []
                    for x, y in puntos:
                        segmento.append(f"{x / ancho:.6f}")
                        segmento.append(f"{y / alto:.6f}")
                    linea = f"{clase_id} " + " ".join(segmento)
                    ftxt.write(linea + "\n")

print("✅ Segmentación YOLOv8 organizada correctamente en train/ y val/")
