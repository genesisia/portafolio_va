import cv2
#importa la libreria opencv para trabajar con imagen y vision artificial
import numpy as np
#importa numpy para crear y manipular matrices (las imagenes son
#matrices de pixeles

#creo una matriz
#img=np.zeros((300,300),np.uint8)
img=np.full((300,300),200,dtype=np.uint8)
#np.zeros((300))crea una matriz de 300 filas y 300 columnas
#llena de ceros
#input.vint8 define que cada valor se entero de 8 bits(0-255)
#adecuado para escala de grises

#creamos la ventana
cv2.imshow("imangen fondo negro",img)
#muestra la imagen de la ventana
#imagen de fondo negro es el nombre de la ventana
cv2.waitKey(0)
#espera que el usuario presione cualquier tecla para cerrar la ventana
cv2.destroyAllWindows()
#cierra la ventana