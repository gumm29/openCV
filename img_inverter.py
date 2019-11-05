import cv2
import numpy as np 

img = cv2.imread('teste.jpg')
img1 = cv2.imread('python.jpg')

rows, cols, channels = img1.shape
print(rows)
print(cols)
roi = img[0:rows, 0:cols]

img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 239, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img1_fg=cv2.bitwise_and(img1, img1, mask=mask)

dst=cv2.add(img_bg, img1_fg)
img[0:rows, 0:cols] = dst

cv2.imshow('r', img)
cv2.waitKey(0)
cv2.destroyAllWindows