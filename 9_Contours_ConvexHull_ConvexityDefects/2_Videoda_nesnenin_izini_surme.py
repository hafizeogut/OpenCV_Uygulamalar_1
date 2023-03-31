import cv2

import numpy as np

cap=cv2.VideoCapture("C:\OpenCv_Uygulamalar_1\src\dog.mp4")

while (1):
    _,frame=cap.read()
    frame=cv2.resize(frame,(400,400))
    
    #Nesnelerin izini sürmek adına BGR formattan HSV formatına çevriliyor.
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Videoda beyaz nesnenin takibi yapmak adına beyazın hsv kodları kullanılıyor.
    sensitivity=15
    lower_white=np.array([0,0,255-sensitivity])#hsv code for
    upper_white=np.array([0,sensitivity,255])
    
    #hsv ye çevrilmiş framelerin içinde  lower_white  upper_white karalığında maske uygulanıyor.
    mask=cv2.inRange(hsv,lower_white,upper_white)
    
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break