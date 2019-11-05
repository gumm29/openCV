import numpy as np
import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

im = cv2.imread('rosto.png')
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

faces1 = face.detectMultiScale(im_gray, 1.4, 2)

for (x,y,w,h) in faces1:
    cv2.rectangle(im, (x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('imagem', im)
cv2.waitKey(0)
cv2.destroyAllWindows