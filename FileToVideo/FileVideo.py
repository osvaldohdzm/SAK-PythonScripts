import cv2
import qrcode
import numpy as np
from PIL import Image
from tqdm import tqdm

# Ruta del archivo de imagen que quieres convertir en códigos QR
archivo_a_convertir = r"D:\osvaldohm\Desktop\Repositories\SAK-PythonScripts\FileToVideo\File.png"

# Abrir la imagen que deseas convertir
imagen_a_convertir = Image.open(archivo_a_convertir)

# Obtener el contenido de la imagen como una cadena de texto
contenido = imagen_a_convertir.tobytes()

# Dividir el contenido en partes de 3 segundos (puedes ajustar este valor)
duracion_segmento = 3
segmentos = [contenido[i:i+duracion_segmento] for i in range(0, len(contenido), duracion_segmento)]

# Comprueba si el códec de vídeo mp4v está disponible
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Ruta donde se guardará el archivo .mp4
nombre_archivo_mp4 = 'archivo_qr.mp4'

# Crea el objeto de video .mp4
video = cv2.VideoWriter(nombre_archivo_mp4, fourcc, 10, (640, 480))

# Agregar una barra de progreso usando tqdm
for segmento in tqdm(segmentos, desc="Procesando segmentos"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(segmento)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Convertir la imagen QR a escala de grises usando PIL
    qr_img = qr_img.convert('L')
    qr_img_np = np.array(qr_img)

    for _ in range(30):  # Agregar el mismo cuadro durante 3 segundos
        video.write(qr_img_np)

# Liberar el objeto de video
video.release()
cv2.destroyAllWindows()
