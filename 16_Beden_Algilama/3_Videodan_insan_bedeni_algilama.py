import cv2 
 
video=cv2.VideoCapture("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//4_Test_videoes//body.mp4")

body_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//fullbody.xml")

while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies=body_cascade.detectMultiScale(gray,1.2,1)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv2.imshow("vşdeo",frame)
    
    if cv2.waitKey(5) & 0xFF==ord("q"):
        break
    
video.release()
cv2.destroyAllWindows()