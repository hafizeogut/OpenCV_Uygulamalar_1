import cv2
cap=cv2.VideoCapture(0)

fileName="C:\OpenCv_Uygulamalar_1\output\Hafize.avi"

codec=cv2.VideoWriter_fourcc('W','M','V','2')#fourcc.org video codec uzantıları.
frameRate=30
resolution=(640,480)
video_file_output=cv2.VideoWriter(fileName,codec,frameRate,resolution)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    
    video_file_output.write(frame)
    cv2.imshow("Webcam Live",frame)
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    
video_file_output.release()
cap.release()
cv2.destroyAllWindows()