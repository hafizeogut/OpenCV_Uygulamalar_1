#Kontur:şeklin sınırları boyunca ard arda devam eden benzer renk özelliğine  sahip olan renk bütünüdür
#       Temel Kontur Tespit Algoritması
#Yüksek doğruluklu kontur çizimleri için binary resimler kulllanmalıyız cv2.cvtColor() cv2. trreshold()
#kontur kordinatları tespiti cv2.findContours
#bulunan noktaların tespiti cv2.drawContours
# Contous Features:Kontur Ozellikleri
#   Alan
#   Çevre
#   geometri merkezi
#   Çevreleyici Geometriler

#convex hull Duşbükey Örtü
#Convex Hull:Dışbükey örtü
#Convexity Defects:Dışbükey 

import cv2

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\contour.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(contours)
cnt=contours[0]

Moments=cv2.moments(cnt)
print(Moments)
print(Moments["m00"])

#Alan Bulunuyor.
area=cv2.contourArea(cnt)
print(area)

#Çevre bulunuyorç
primeter=cv2.arcLength(cnt,True)
print(primeter)
 

cv2.waitKey(0)
cv2.destroyAllWindows()