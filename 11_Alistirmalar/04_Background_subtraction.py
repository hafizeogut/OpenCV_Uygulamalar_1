import cv2
import numpy as np

capture=cv2.VideoCapture("C:\OpenCv_Uygulamalar_1\src\car.mp4")
subtractor_cikarici=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=75,detectShadows=True)
while True:
    _,frame=capture.read()
    frame=cv2.resize(frame,(640,480))
    mask=subtractor_cikarici.apply(frame)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break
    

capture.release()
cv2.destroyAllWindows()