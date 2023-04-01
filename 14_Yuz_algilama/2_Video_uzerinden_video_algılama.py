import cv2

video=cv2.VideoCapture("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//4_Test_videoes//faces.mp4")
face_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//frontalface.xml")


while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray,1.1,2)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        
    cv2.imshow("image",frame)
    
    if cv2.waitKey(5)  & 0xFF==ord("q"):
        break
    
video.release()
cv2.destroyAllWindows()