import cv2
import numpy as np
import imageio

# Cargar la imagen de pingüinos
pinguinos_img = cv2.imread('pinguinos.jpg')

if pinguinos_img is None:
    print("No se pudo cargar la imagen 'pinguinos.jpg'. Verifica la ruta y el archivo.")
    exit()

# Crear una serie de frames con un cambio de color
num_frames = 30
frames = []

for i in range(num_frames):
    # Crear un efecto de cambio de color
    color_shift = i * 8
    frame = cv2.addWeighted(pinguinos_img, 0.5, np.zeros(pinguinos_img.shape, pinguinos_img.dtype), 0.5, color_shift)
    frames.append(frame)

# Guardar los frames como un archivo GIF usando imageio
output_gif = 'pinguinos_effect.gif'
imageio.mimsave(output_gif, frames, duration=0.1)

print(f"Se ha guardado la animación de los pingüinos con efecto como '{output_gif}'")
