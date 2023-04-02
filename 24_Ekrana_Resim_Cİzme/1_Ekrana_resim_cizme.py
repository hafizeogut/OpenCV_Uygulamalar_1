import cv2
import numpy as np

#listeleme işlemi yapılacağımndan içe aktarıldı.
from collections import deque

kernel=((5,5),np.uint8)

lower_blue=np.array([160,60,60])
upper_blue=np.array([140,255,255])

#Mavi n oktalar blue_points e atandı.
blue_points=[deque(maxlen=512)]
green_points=[deque(maxlen=512)]
red_points=[deque(maxlen=512)]
yellow_points=[deque(maxlen=512)]

blue_index=0
green_points=0
red_points=0
yellow_points=0

colors=[(255,0,0),(0,0,255),(0,0,255),(0,255,255)]
color_index=0

paintWindow=np.zeros((471,636,3))+255 
paintWindow=cv2.rectangle(paintWindow,(40,1),(140,65),(0,0,0),2)
paintWindow=cv2.rectangle(paintWindow,(160,1),(255,65),colors[0],-1)
paintWindow=cv2.rectangle(paintWindow,(275,1),(370,65),colors[1],-1)
paintWindow=cv2.rectangle(paintWindow,(390,1),(485,65),colors[2],-1)
paintWindow=cv2.rectangle(paintWindow,(505,1),(600,65),colors[3],-1)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(paintWindow,"CLEAR ALL",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(paintWindow,"CLEAR BLUE",(185,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(paintWindow,"CLEAR GREEN",(298,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(paintWindow,"CLEAR RED",(420,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(paintWindow,"CLEAR YELLOW",(520,33),font,0.5,(0,0,0),2,cv2.LINE_AA)

cv2.namedWindow("Paint")

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    frame=cv2.rectangle(frame,(40,1),(140,65),(0,0,0),2)
    frame=cv2.rectangle(frame,(160,1),(255,65),colors[0],-1)
    frame=cv2.rectangle(frame,(275,1),(370,65),colors[1],-1)
    frame=cv2.rectangle(frame,(390,1),(485,65),colors[2],-1)
    frame=cv2.rectangle(frame,(505,1),(600,65),colors[3],-1)

    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"ALL",(49,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"BLUE",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"GREEN",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"RED",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"YELLOW",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    
    if ret is False:
        break
    
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    
    
    if cv2.waitKey(3) & 0xFF==ord("q"):
        break
    
    
cap.release()
cv2.destroyAllWindows()