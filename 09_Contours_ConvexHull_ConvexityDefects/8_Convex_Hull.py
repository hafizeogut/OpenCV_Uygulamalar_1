import cv2 
import numpy as np
#Kontur kavramı
#nesneyi çevreleyen ard arda devam eden benzer renk özelliğine sahip olan renkler bütünüdür
#1-başla
#2-cv2.cvtColor() ile gri formata çerilir
#3-cv2.threshold() ile binary formata çevrilir
#4-cv2.findContours() kontur kordinatlarının tespiti
#5-drawContours() Bulunan noktaların çizimi

#Kontur Özellikleri

#convexhull:dışbükey örtü


img=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\map.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur=cv2.blur(gray,(3,3))

ret,thresh=cv2.threshold(blur,40,255,cv2.THRESH_BINARY)

#conturlar değilkene atandı.
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(contours)
hull=[]

for i in range(len(contours)):
    #Doğrudan değeri döndürmek için True, İndisi döndüremek için Flase değeri girilir
    hull.append(cv2.convexHull(contours[i],False))
    
bg=np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)
#print(hull)

for i in range (len(contours)):
    cv2.drawContours(bg,contours,i,(255,0,0),3,8,hierarchy)
    cv2.drawContours(bg,hull,i,(0,255,0),1,8,hierarchy)
    
    
cv2.imshow("Image",bg)

cv2.waitKey(0)
cv2.destroyAllWindows()