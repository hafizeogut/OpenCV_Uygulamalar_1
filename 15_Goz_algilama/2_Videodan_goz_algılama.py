import cv2

video=cv2.VideoCapture("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//4_Test_videoes//eye.mp4")
 
face_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//frontalface.xml")
eye_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//eye.xml")


while True:
    ret,frame=video.read()
    frame=cv2.resize(frame,(480,360))
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    roi_frame=frame[y:y+h,x:x+w]
    roi_gray=gray[y:y+h,x:x+w]
    
    eyes=eye_cascade.detectMultiScale(roi_gray)
    
    for(ey,ex,ew,eh) in eyes:
        cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
        
    cv2.imshow("video",frame)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()
    