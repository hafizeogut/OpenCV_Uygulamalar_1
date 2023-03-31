#Hough Line Transform: Cizgi dönüşümü.
#Hough Circle Transform: Çember dönüşümü

import cv2 
import numpy as np

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\h_line.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#1->KENAR TESPİTİ
#Canny(resim,min,max) Kenarlık tespiti.
edges=cv2.Canny(gray,75,150)

#2->ÇİZGİ TESPİTİ
#HoughLinesP(edges,RO,teta,threshold değeri)
lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200)
#print(lines)#[[[ 46  57 119  57]] cizgilerin bulıunduklerı yerler


for line in lines:
    #[[[ 46  57 119  57]]
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    
cv2.imshow("img",img)
cv2.imshow("Gray",gray)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
