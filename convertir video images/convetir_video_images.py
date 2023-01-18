# importar los paquetes necesarios
import argparse
import imutils
import cv2
import os

# construir el analizador de argumentos y analizar los argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, type=str,
	help="ruta al archivo de video de entrada")
ap.add_argument("-o", "--output", required=True, type=str,
	help="ruta al directorio de salida para almacenar marcos")
args = vars(ap.parse_args())

# contador de para nombrar la imagen de salida
total = 0

# abrir el video para poder analizar la señal
vs = cv2.VideoCapture(args["video"])

# recorrer los cuadros del video
while True:
    # tomar un cuadro del video
    (grabbed, frame) = vs.read()
    # si el cuadro es Ninguno, entonces hemos llegado al final 
    # del archivo de video
    if frame is None:
        break

    # redimensionar imagen a 640 por un rango    
    frame = imutils.resize(frame, width=640)

    #construya la ruta al cuadro de salida e incremente el
    #contador total de cuadros
    filename = "{}.png".format(total)
    path = os.path.sep.join([args["output"], filename])

    # guarde el marco *original, de alta resolución* en el disco
    print("[INFO] saving {}".format(path))
    cv2.imwrite(path, frame)
    total += 1

    # se muestra el gramento del video.    
    cv2.imshow("Frame", frame)

    # detectar si hay una pulsación de tecla    
    key = cv2.waitKey(1) & 0xFF

    # si se presionó la tecla `q`, sal del bucle
    if key == ord("q"):
        break

# Terminar el proceso cuando el buble acabe.
vs.release()


    
