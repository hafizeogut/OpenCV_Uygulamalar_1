import cv2
 
video=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//frontalface.xml")

while True:
    
    ret,frame=video.read()
    frame=cv2.flip(frame,1)
    #Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #Cascade dosyamızı kullanarak her bir frame üzerindeki yüzlerin kordinatlarını bulalım
    faces=face_cascade.detectMultiScale(gray,1.4,1)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    cv2.imshow("video",frame)
    
    if cv2.waitKey(1) & 0xFF== ord("q"):
        break
    
video.release()
cv2.destroyAllWindows()