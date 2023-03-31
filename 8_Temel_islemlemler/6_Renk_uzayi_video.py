import cv2

capture=cv2.VideoCapture("C:\OpenCv_Uygulamalar_1\src\gun_ve_gece.mp4")

 
while True:
    ret,frame=capture.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    if ret==False:
        break

    frame=cv2.resize(frame,(700,500))
    
    cv2.imshow("Video",frame)
    if cv2.waitKey(20) & 0XFF == ord("q"):
        break
    
capture.release() 
cv2.destroyAllWindows()