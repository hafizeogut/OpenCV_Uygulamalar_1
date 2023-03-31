import cv2
import numpy as np

video=cv2.VideoCapture("C://OpenCv_Uygulamalar_1//src//line.mp4")


while True:
    ret,frame= video.read()
    frame=cv2.resize(frame,(640,480))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_yellow=np.array([18,94,140],np.uint8)
    upper_yellow=np.array ([48,255,255],np.uint8)
    
    mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
    
    edges=cv2.Canny(mask,75,250)
    
    cv2.imshow("edges",edges)
    
    lines=cv2.HoughLinesP(edges,1,np.pi/180,40,maxLineGap=50)
    
    for line in lines :
        x1,y1,x2,y2=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
    
    
    cv2.imshow("Img",frame)
    if cv2.waitKey(20) & 0xFF== ord("q"):
        break
    
video.release()
cv2.destroyAllWindows()