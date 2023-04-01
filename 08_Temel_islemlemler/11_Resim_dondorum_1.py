import cv2
import numpy as np

img=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\aysenaz.jpg",0)
img=cv2.resize(img,(500,650))
row,col=img.shape

#2 boyutta bir yön değiştirme işlemi yapıldı.

#((satur,sütunü),kaç derece,ölçek)
Matris=cv2.getRotationMatrix2D((col/2,row/2),90,2)

dst=cv2.warpAffine(img,Matris,(col,row))

cv2.imshow("dst",dst)
cv2.waitKey(0)