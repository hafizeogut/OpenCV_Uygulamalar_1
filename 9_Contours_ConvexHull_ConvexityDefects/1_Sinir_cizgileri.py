#Kontur?
#Şeklin sınırları boyunca ard arda devam eden ve benzer renk özelliğine sahşp noktalar bütünüdür.
#ConvexHull: İçbükey şekillere dışbükey örtüler çizmektir.
#Convexity Defects:Dışbükey Kusurlar

import cv2

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\contour1.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#1-> kontur için Threshold işlemi yapılır.

#thresh iki adet değişken döndürüyor
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

#2->Kontur kordinatlarının tespiti
#(thresh işlemi,contur bulmak adına default yapılan iki argğman)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)

#3->bulunan kordinatların tespiti
cv2.drawContours(img,contours,-1,(0,0,255),1)
cv2.imshow("Contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
