import cv2
cap = cv2.VideoCapture(0)
#If we have more webcams and we want to set some of them, we change 0 for 1,2,3...
#In this case I only have one, then it's the first one 

leido, frame = cap.read()

if leido == True:
	cv2.imwrite("foto.png", frame)
	print("Foto tomada correctamente")
else:
	print("Error al acceder a la cámara")

cap.release()

#Pyinstaller name.py 