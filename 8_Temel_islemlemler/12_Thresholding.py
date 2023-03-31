#Thresholding:Basit Eşikleme
#siyah beyaz resimlerde işlem yapılır

import cv2

import numpy as np

from matplotlib import pyplot as plt

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\manzara.png",0)

#belirli bir eşik değerinin altındaki piksel değerleri siyah, üstündeki değerler ise beyaz olarak işaretlenir.
ret,thrs1=cv2.threshold(img,200,255,cv2.THRESH_BINARY)

th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)

th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)
cv2.imshow("img",img)

cv2.imshow("img thrs1",thrs1)

cv2.imshow("img thrs2",th2)

cv2.imshow("img thrs3",th3)


cv2.waitKey(0)