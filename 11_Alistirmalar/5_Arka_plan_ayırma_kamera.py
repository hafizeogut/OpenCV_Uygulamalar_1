import cv2

import numpy as np

capture=cv2.VideoCapture(0)
subtractor_cikarici=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=75,detectShadows=True)

while True:
    _,frame=capture.read()
    frame=cv2.flip(frame,1)
    mask=subtractor_cikarici.apply(frame)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    
    
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

capture.release()
cv2.destroyAllWindows()