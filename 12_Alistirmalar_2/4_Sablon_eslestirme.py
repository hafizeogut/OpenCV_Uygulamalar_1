#TEMPLATE Matching

import cv2
import numpy as np

image_path="C:\OpenCv_Uygulamalar_1\src\starwars.jpg"
template_path="C:\OpenCv_Uygulamalar_1\src\starwars2.jpg"

img=cv2.imread(image_path)
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Şablom oluituruldu.
template=cv2.imread(template_path,cv2.IMREAD_GRAYSCALE)
w,h=template.shape[::-1]


#Şablonu resme  uygun yere yerleitirilecek. 
result=cv2.matchTemplate(gray_image,template,cv2.TM_CCOEFF_NORMED)
#Siyah beyaz ile arasında giden bir renk değeri
#Beyaza(1) en yakın olunan nokta hangisi ise iablon orada bulunur

location=np.where(result>=0.7)


#location[::-1] -1 genişlik yükseklik birde tam tersi dolaşılır
for point in zip(*location[::-1]):
    #print(point)
    #w=genişlik
    #h yükseklik
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(0,255,0),3)
    


cv2.imshow("Image",img)
cv2.waitKey(0)