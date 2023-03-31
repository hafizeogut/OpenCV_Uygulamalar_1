#Set the resolution: Çözünürlük Ayarlama
import cv2

window_name="Live Video"
cv2.namedWindow(window_name)

cap=cv2.VideoCapture(0)
print("Width: "+str(cap.get(3)))
print("Height: "+str(cap.get(4)))

#Cozunurluk değereleri değiştiriliyor.3 x ekseni
cap.set(3,1280)
cap.set(4,720)
print("Width: "+str(cap.get(3)))
print("Height: "+str(cap.get(4)))

while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    
    cv2.imshow("Live Video",frame)
    
    if cv2.waitKey(1)==27:
        break
    
