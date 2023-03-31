#cv2.Canny(input,minThreshold,max,threshold)


import cv2

cap=cv2.VideoCapture(0)

while 1:
    ret,frame=cap.read()
    
    #gçrüntüyü y eksenine göre değiştiriliyor.
    frame=cv2.flip(frame,1)
    
    #Görüntüdeki kenarları saptama işlmei yapılıyor
    edges=cv2.Canny(frame,10,200)

    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)
    
    if cv2.waitKey(6) & 0xFF==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()