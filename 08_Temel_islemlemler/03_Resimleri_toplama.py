import cv2
import numpy as np

#Bir tuval oluşturuluyor.
circle=np.zeros((512,512,3),np.uint8)+255

#Tuvale bir daire çiziliyor.
cv2.circle(circle,(256,256),60,(255,0,0),-1)

#Tuvale dikdörtgen oluituruluyor
regtangle=np.zeros((512,512,3),np.uint8)+255
cv2.rectangle(regtangle,(150,150),(300,300),(125,25,55),-1)

add=cv2.add(circle,regtangle)
print(add[256,256])

cv2.imshow("Cirle",circle)
cv2.imshow("Regtangle",regtangle)
cv2.imshow("Add",add)

cv2.waitKey(0)
cv2.destroyAllWindows()