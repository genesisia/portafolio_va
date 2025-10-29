import cv2

#cargar la imagen con imread
imagen=cv2.imread("SNOPPY.jpg")
imagen=cv2.resize(imagen,(500,500))
blanconegro=cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
aleatorio=cv2.cvtColor(imagen,cv2.COLOR_RGB2HSV)


#guardando las imagenes con cambio de campo de color
cv2.imwrite("aleatoria.jpg",aleatorio)
cv2.imwrite("blanconegro.jpg",blanconegro)

#mostrar el resultado con imshow()
cv2.imshow("SNOPPY",imagen)#muestra la imagen
cv2.imshow("SNOPPY B/N",blanconegro)#muestra la imagen
cv2.imshow("nuevo",aleatorio)#muestra la imagen

cv2.waitKey(0)#espera una tecla
cv2.destroyAllWindows()#cierra la ventana
