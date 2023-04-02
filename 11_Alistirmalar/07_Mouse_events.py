import cv2

capture=cv2.VideoCapture("C:\OpenCv_Uygulamalar_1\src\line.mp4")

#Mouse dan alınan etkiyi saklamak için fonksiyon yazılıyor

circles=[]
def mouse(event,x,y,flags,params):
        
    #Sol tuia basıldıysa
    if event==cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))
        
    
 
cv2.namedWindow("Frame")

#Mause tıkladığında :
cv2.setMouseCallback("Frame",mouse)


while 1:
    _,frame=capture.read()
    frame=cv2.resize(frame,(640,480))
    #frameler üzerine çember ciziliyor:
    for center in circles:
        cv2.circle(frame,center,20,(255,0,0),-1)
    
    cv2.imshow("Frame",frame)
    
    #Esc tuşunda video durduruluyor.
    key=cv2.waitKey(1)
    if key==27:
        break
    #Ekran temizleniyor.
    elif key ==ord("h"):
        circles=[]

capture.release()
cv2.destroyAllWindows()