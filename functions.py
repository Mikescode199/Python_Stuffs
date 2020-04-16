import cv2


def Repeat(word, number):
    for _ in range(number):
        print(word)

def Take_picture():
    cam = cv2.VideoCapture(0)
    mike = cam.imwrite('MIke')
    cam.realase()

Take_picture()
