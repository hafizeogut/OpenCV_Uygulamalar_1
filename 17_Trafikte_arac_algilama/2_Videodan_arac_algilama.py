import cv2

video=cv2.VideoCapture("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//4_Test_videoes//car.mp4")
car_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//car.xml")

while 1:
    ret,frame=video.read()
    frame=cv2.resize(frame,(640,360))
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.3,2)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+y+h),(255,0,0),3)
        
    cv2.imshow("video",frame)
    
    if cv2.waitKey(5) &0xFF==ord("Q"):
        break
    
video.release()
cv2.destroyAllWindows()