import cv2
import numpy as np

def nothing(x):
    pass

capture=cv2.VideoCapture(0)
cv2.namedWindow("Settings")

cv2.createTrackbar("Lower-Hue","Settings",0,180,nothing)
cv2.createTrackbar("Lower-Saturation","Settings",0,255,nothing)
cv2.createTrackbar("Lower-Value","Settings",0,255,nothing)

cv2.createTrackbar("Upper-Hue","Settings",0,180,nothing)
cv2.createTrackbar("Upper-Saturation","Settings",0,255,nothing)
cv2.createTrackbar("Upper-Value","Settings",0,255,nothing)

font=cv2.FONT_HERSHEY_SIMPLEX

while 1:
    ret,frame=capture.read()
    frame=cv2.flip(frame,1)
    #Kızakların konumu alınıyor.
    lh=cv2.getTrackbarPos("Lower-Hue","Settings")
    ls=cv2.getTrackbarPos("Lower-Saturation","Settings")
    lv=cv2.getTrackbarPos("Lower-Value","Settings")
    
    uh=cv2.getTrackbarPos("Upper-Hue","Settings")
    us=cv2.getTrackbarPos("Upper-Saturation","Settings")
    uv=cv2.getTrackbarPos("Upper-Value","Settings")
    
    lower_color=np.array([lh,ls,ls])
    upper_color=np.array([uh,us,uv])
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_color,upper_color)
    
    #1 lerden oluian bir kernel
    #Beyaz nesneler üzereindeki siyah noktaları yok etmek için yapılması gerekiyor.
    kernel=np.ones((5,5),np.uint8)
    
    #erezyona uğratılılarak karıncalanmalar azaltıldı.
    mask=cv2.erode(mask,kernel)
    
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #merkez noktaları kullanılarak cizim yapılıyor
    for cnt in contours:
        are=cv2.contourArea(cnt)
        
        #cnt ile bulunan konturlara bir iyileştirme yapılıyor.
        epsilon=0.02* cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
        #kONTURLARA DAHA ÇOK YAKALAŞILDI
        
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        
        if are >400:
            cv2.drawContours(frame,[approx],0,(0,0,0),5)
            
            if len (approx)==3:
                cv2.putText(frame,"Triangle",(x,y),font,1,(0,0,0))
            elif len (approx)==4:
                cv2.putText(frame,"Rectangle",(x,y),font,1,(0,0,0))
                
            elif len (approx)>3:
                cv2.putText(frame,"Circle",(x,y),font,1,(0,0,0)) 
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    
    if cv2.waitKey(3) & 0xFF==ord("q"):
        break
    