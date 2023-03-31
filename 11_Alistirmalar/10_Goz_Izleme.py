import cv2
#Göz bebeği olan yeri beyaz yapıp diğer yerler siyah yapılacak
video=cv2.VideoCapture("C://OpenCv_Uygulamalar_1//src//eye_motion.mp4")

while True:
    ret,frame=video.read()
    
    if ret is False:
        break
    
    
    roi=frame[80:210,230:450]
    rows,cols,_=roi.shape
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,threshold=cv2.threshold(gray,2,255,cv2.THRESH_BINARY_INV)
    
    
    
    #Göz bebeğinin konturları bulunuyor.
    contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #sorted içine girilen değerleri sıralar.
    #Kontuların alanlarına gçre sırala
    #True tersten sırala
    contours=sorted(contours,key=lambda x: cv2.contourArea(x),reverse=True)
    
    #Alanı en buyuk dikdorgeni cizilip bırakılıyor
    for cnt in contours:
        #sol üst ve sağ alt kordinatlarına ulaşıldı.
        (x,y,w,h)=cv2.boundingRect(cnt)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)
        
        #cv2.line(roi,(x1,y1),(x2,y2),(0,255,0))
        #satırların en sonu rows.Cols Sutun
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)
        cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
        break
    
    frame[80:210,230:450]=roi
    cv2.imshow("Frame",frame)
    cv2.imshow("Threshold",threshold)
    if cv2.waitKey(50) & 0xFF==ord("q"):
        break
    
video.release()
cv2.destroyAllWindows()