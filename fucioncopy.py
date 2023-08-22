import os
import time
from datetime import datetime
from PIL import Image


# Carpeta de imágenes originales
carpeta_imagenes = "images"

# Carpeta donde se guardarán las imágenes con marcos
carpeta_salida = "imagen_fusionada"

# Ruta del archivo de marco
archivo_marco = "./framed_images/image_1_framed.png"

# Crear la carpeta de salida si no existe
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)
    
    
# Cargar el archivo de marco
marco = Image.open(archivo_marco)
    
    
# Recorrer todas las imágenes en la carpeta
for imagen in os.listdir(carpeta_imagenes):
    print(imagen)
    
    if imagen.endswith(".jpg") or imagen.endswith(".png") or imagen.endswith(".jpeg"):
        ruta_imagen = os.path.join(carpeta_imagenes, imagen)
        imagen_fondo = Image.open(ruta_imagen)

        # Ajustar la imagen al tamaño del marco
        imagen_superpuesta = imagen_fondo.resize((1080, 1080))

        # if imagen_fondo.mode != "RGBA":
        imagen_fondo = imagen_fondo.convert("RGBA")
        print(imagen_fondo)
        # if imagen_superpuesta.mode != "RGBA":
        print(imagen_superpuesta)
        imagen_superpuesta = marco.convert("RGBA")

        # Ajustar la imagen superpuesta al tamaño de la imagen de fondo
        imagen_superpuesta = imagen_superpuesta.resize((1080, 1080))


        x = imagen_fondo.resize((1080, 1080))
        y =imagen_superpuesta.resize((1080, 1080))


        # Fusionar las imágenes utilizando paste()
        imagen_final = Image.alpha_composite(x, y)
        imagen_final.resize((1080, 1080))

        # Guardar la imagen fusionada

        # Obtener la fecha y hora actual
        fecha_actual = datetime.now()

        # Obtener el tiempo actual en nanosegundos
        tiempo_actual_ns = time.time_ns()
        # f"imagen_{fecha_actual.strftime('%Y-%m-%d_%H-%M-%S')}_{tiempo_actual_ns}.jpg"
        imagen_final.save(f"./imagen_fusionada/imagen_fusionada{fecha_actual.strftime('%Y-%m-%d_%H-%M-%S')}_{tiempo_actual_ns}.png")

        print("Imagen fusionada guardada.")



#         # Fusionar la imagen con el marco
#         imagen_fusionada = Image.new("RGBA", (marco.width, marco.height), (255, 255, 255, 0))
#         imagen_fusionada.paste(imagen, (0, 0))
#         imagen_fusionada.paste(marco, (0, 0), marco)

#         # Guardar la imagen fusionada en la carpeta de salida
#         ruta_salida = os.path.join(carpeta_salida, f"con_marco_{nombre_archivo}")
#         imagen_fusionada.save(ruta_salida)

# print("Imágenes fusionadas y guardadas en la carpeta de salida.")

# # Cargar el archivo de marco
# marco = Image.open(archivo_marco)

# for nombre_archivo in os.listdir(carpeta_imagenes):
#     if nombre_archivo.endswith(".jpg") or nombre_archivo.endswith(".png"):
#         ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
#         imagen = Image.open(ruta_imagen)
    
#     imagen_fondo = Image.open("./images/image_1.jpg")
#     imagen_superpuesta = Image.open("./framed_images/image_1_framed.png")

#     if imagen_fondo.mode != "RGBA":
#         imagen_fondo = imagen_fondo.convert("RGBA")
#     if imagen_superpuesta.mode != "RGBA":
#         imagen_superpuesta = imagen_superpuesta.convert("RGBA")

#     # Ajustar la imagen superpuesta al tamaño de la imagen de fondo
#     imagen_superpuesta = imagen_superpuesta.resize(imagen_fondo.size)

#     # Fusionar las imágenes utilizando paste()
#     imagen_final = Image.alpha_composite(imagen_fondo, imagen_superpuesta)

#     # Guardar la imagen fusionada

#     # Obtener la fecha y hora actual
#     fecha_actual = datetime.now()

#     # Obtener el tiempo actual en nanosegundos
#     tiempo_actual_ns = time.time_ns()
#     # f"imagen_{fecha_actual.strftime('%Y-%m-%d_%H-%M-%S')}_{tiempo_actual_ns}.jpg"
#     imagen_final.save(f"./imagen_fusionada/imagen_fusionada{fecha_actual.strftime('%Y-%m-%d_%H-%M-%S')}_{tiempo_actual_ns}.png")

#     print("Imagen fusionada guardada.")