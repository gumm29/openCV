import numpy as np 
import cv2

imagem = cv2.imread('python.jpg')
bg = cv2.imread('teste.jpg')
cv2.imshow('q', imagem)

print(imagem.shape[0])
print(imagem.shape[1])
print(imagem.shape[2])

(b,g,r) = imagem[0, 0]
print(r,g,b)

(b,g,r) = imagem[25, 100]
print(r,b,g)

imagem[0:20,0:30] = (15,30,60)
cv2.imshow('cor', imagem)

# corte = imagem[50:150, 50:150]
# cv2.imshow('corte', corte)
# cv2.imwrite('corte.jpg', corte)
alt, larg = imagem.shape[:2]

des = np.float32([[1, 0, 50], [0,1,20]])
d = cv2.warpAffine(bg,des,(larg, alt))
cv2.imshow('j', d)

ponto = (larg/2, alt/2)
rotacao = cv2.getRotationMatrix2D(ponto, 45, 1.0)
rotac = cv2.warpAffine(imagem, rotacao, (larg, alt))
cv2.imshow('i', rotac)

cv2.waitKey(0)