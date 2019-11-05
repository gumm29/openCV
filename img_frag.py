import numpy as np 
import cv2

img = cv2.imread('imagem.jpg', cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]

img[100:150, 100:150] = [234,255,213]

cv2.imshow('teste', img)
cv2.waitKey(0)
cv2.destroyAllWindows