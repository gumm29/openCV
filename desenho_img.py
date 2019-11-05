import numpy as np
import cv2

img = cv2.imread('imagem.jpg', cv2.IMREAD_COLOR)

cv2.line(img,(0,0), (10, 50), (255,0,0), 2)
cv2.rectangle(img, (15,25), (100, 50), (0,255,0), 2)
cv2.circle(img, (100, 63), 55, (0,0,255), 2)

pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,0,225), 1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'teste!', (0,150), font, 3, (0, 255, 234), 5, cv2.LINE_AA)

cv2.imshow('teste', img)
cv2.waitKey(0)
cv2.destroyAllWindows
