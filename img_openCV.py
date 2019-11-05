import cv2

img = cv2.imread('imagem.jpg')
cv2.imshow('imagem',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray = cv2.cvtColor(img, cv2.COLOR_LUV2LBGR)
cv2.imwrite('pb2.jpg', gray)