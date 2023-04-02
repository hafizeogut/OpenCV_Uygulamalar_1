import cv2
import numpy as np

video=cv2.VideoCapture("C://OpenCv_Uygulamalar_1//src//traffic.avi")

#arka plan 
backsub=cv2.createBackgroundSubtractorMOG2()
c=0

while True:
    ret,frame=video.read() 
    if ret:
        #arkaplanı çıkarma işlemi uygulandı.
        fgmask=backsub.apply(frame)
        
        #çizgiler çekiliyor
        cv2.line(frame,(50,0),(50,300),(0,255,0),2)
        cv2.line(frame,(70,0),(70,300),(0,255,0),2)
        
        #Araçların kordinatları bulunuyor
        contours,hierarchy=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        try:
            hierarchy=hierarchy[0]
        
        except:
            hierarchy=[]
        
        #zip tekrarlı bir işlem
        for contours,hier in zip(contours,hierarchy):
            # bounding:sınırlayıcı
            (x,y,w,h)=cv2.boundingRect(contours) 
            if w>40 and h>40:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)    
                if x>50 and x<70:
                    c+=1   
        
        cv2.putText(frame,"car:"+str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
        
        
        
        cv2.imshow("img",fgmask)
        cv2.imshow("cAR cOUNTER",frame)
         
        if cv2.waitKey(20) & 0xFFF==ord("q"):
            break
video.release()
cv2.destroyAllWindows()