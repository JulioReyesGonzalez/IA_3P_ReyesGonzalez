# IA_3P_ReyesGonzalez
Sistema de Detección de Gestos con YOLOv8 + MediaPipe
Este proyecto utiliza YOLOv8 con segmentación y MediaPipe para detectar gestos de la mano a través de la webcam. Según el gesto detectado, se ejecutan aplicaciones específicas automáticamente en el sistema.

🧠 Tecnologías utilizadas
Python 3.x

MediaPipe

YOLOv8 (Ultralytics)

OpenCV

subprocess (para control de la PC)

Estructura del proyecto
bash
Copiar
Editar
Gestos/
├── data/                    # Imágenes clasificadas por gestos
├── YOLODataset/            # Dataset en formato YOLOv8 (train/val)
├── best.pt                 # Modelo entrenado con YOLOv8-seg
├── inferencia.py           # Script principal de inferencia
├── SeguimientoManos.py     # Clase para detección y seguimiento de manos
├── convertir_labelme_a_yolov8_seg.py  # Script para convertir etiquetas
├── dataset.yaml            # Archivo de configuración para entrenamiento
├── README.md               # Este archivo
Gestos soportados
Gesto	Acción
Gesto_I	Abre Bloc de notas
Gesto_puno	Abre Microsoft Edge
Gesto_Paz	(acción personalizable)
Gesto_Perfecto	(acción personalizable)
Gesto_Rock	(actualmente desactivado por falsos positivos)

¿Cómo ejecutar?
Asegúrate de tener las dependencias:

bash
Copiar
Editar
pip install ultralytics opencv-python mediapipe
Ejecuta el script principal:

bash
Copiar
Editar
python inferencia.py
Coloca tu mano frente a la cámara y mantén el gesto por 2 segundos para activar la acción.

Entrenamiento personalizado
Puedes entrenar nuevos gestos usando tus datos con segmentación. El modelo se entrena fácilmente en Google Colab o localmente:

bash
Copiar
Editar
yolo task=segment mode=train epochs=30 data=dataset.yaml model=yolov8m-seg.pt imgsz=640 batch=4
 Notas
La ejecución de aplicaciones usa subprocess, asegúrate de que las rutas a los ejecutables sean válidas.

El sistema previene ejecuciones repetidas al mantener control temporal.

El gesto “Rock” fue desactivado temporalmente por falsos positivos frecuentes.

Autores
Julio González
Jayden Hammond
Proyecto académico – Centro de Enseñanza Técnica Industrial
2025
