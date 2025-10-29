import cv2
import numpy as np


#crear una imagen de 500x500 pixeles de 3 canales RGB
img=np.zeros((500,500,3),dtype=np.uint8)

#cambia el color
img[:]=[0,255,0] #

#mostrar imagen
cv2.imshow("imagen fondo",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
