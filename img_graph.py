import numpy as np 
import cv2

img = cv2.imread('teste.jpg')
img1 = cv2.imread('python2.jpg')

# add = img + img1 
# mesclar
# add = cv2.add(img1,img1)
w = cv2.addWeighted(img, 0.6, img1, 0.4, 0)

cv2.imshow('add', w)
cv2.waitKey(0)
cv2.destroyAllWindows