import cv2

video=cv2.VideoCapture("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//4_Test_videoes//smile.mp4")

face_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//frontalface.xml")
smile_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//smile.xml")

while True:
    ret,frame=video.read()
    frame=cv2.resize(frame,(480,360))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        
    roi_img=frame[y:y+h,x:x+h]
    roi_gray=gray[y:y+h,x:x+h]
    smiles=smile_cascade.detectMultiScale(roi_gray,1.2,3)

    for (sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_img,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
        
    cv2.imshow("video",frame)
    
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break
    
video.release()
cv2.destroyAllWindows()