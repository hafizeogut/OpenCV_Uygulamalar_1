import cv2

import numpy as np

canvas=np.zeros((500,500,3),dtype=np.uint8)+25
#print(canvas)

#ÇİZGİ
#cv2.line(çizim yapılacak tuvsl,başlangıç kordinatları,bitiş kordinatları,rengi,kalınlık)
cv2.line(canvas,(1,1),(100,100),(255,155,0),thickness=5)
cv2.line(canvas,(250,305),(57,15),(255,155,0),thickness=7)

#DİKDÖRTGEN
cv2.rectangle(canvas,(20,20),(50,50),(255,255,0),thickness=4)
cv2.rectangle(canvas,(255,255),(325,325),(255,255,0),thickness=-1)

#Daire
cv2.circle(canvas,(250,250),100,(0,0,114),thickness=1)
cv2.circle(canvas,(360,250),36,(0,0,123),thickness=-1)

#ÇOKGEN 
#Çizgilerin birelşimi mantığı ile
p1=(100,200)
p2=(50,50)
p3=(300,100)

cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p1,p3,(0,0,0),4)

#YAMUK 
points=np.array([[100,200],[100,220],[250,250],[150,150] ],np.int32)
cv2.polylines(canvas,[points],True,(0,0,255),5)

#ELİPS
cv2.ellipse(canvas,(350,350),(80,20),10,90,360,(255,114,0),-1)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


