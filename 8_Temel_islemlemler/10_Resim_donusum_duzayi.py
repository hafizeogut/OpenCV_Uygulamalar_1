import cv2

import numpy as np

img=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\aysenaz.jpg",0)
img=cv2.resize(img,(650,650))
row,col=img.shape
# print(row)
# print(col)

#Transformasyon:Dönüşüm uzzayı
Matris=np.float32([[1,0,150],[0,1,150]])

dst=cv2.warpAffine(img,Matris,(row,col))

cv2.imshow("Original",img)
cv2.imshow("Dst",dst)
cv2.waitKey(0)

