#f(x,y)=x*a + y*b + c

import cv2
import numpy as np

#Bir tuval oluşturuluyor.
circle=np.zeros((512,512,3),np.uint8)+255

#Tuvale bir daire çiziliyor.
cv2.circle(circle,(256,256),60,(255,0,0),-1)

#Tuvale dikdörtgen oluituruluyor
regtangle=np.zeros((512,512,3),np.uint8)+255
cv2.rectangle(regtangle,(150,150),(350,350),(125,25,55),-1)

#x*a + y*b + c
dst=cv2.addWeighted(circle,0.7,regtangle,0.3,0)

cv2.imshow("Cirle",circle)
cv2.imshow("Regtangle",regtangle) 
cv2.imshow("Dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()