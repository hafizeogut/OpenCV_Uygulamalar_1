#Histogram ile aydınlık karanlık noktaları gibi özelliklerde çıkarım yapılabilir.

import cv2
import numpy as np
from matplotlib import pyplot as plt


#Tuval oluşturuluyor
#img=np.zeros ((500,500),np.uint8)+65

# cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
# cv2.rectangle(img,(250,170),(350,200),(200,20,155),-1)

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\Kizlarim.jpg")

cv2.imshow("Tuval",img)

b,g,r=cv2.split(img)
plt.hist(b.ravel(),200,[0,266])
plt.hist(g.ravel(),200,[0,266])
plt.hist(r.ravel(),255,[0,266])

plt.show()

#her piksel değeri, tek boyutlu bir diziye sıkıştırıldığında, NumPy kütüphanesi ile histogram hesaplaması yapmaktadır.
#histogram çizimi(,ka. değer olduğu,renk değeri)
plt.hist(img.ravel(),256,[0,256])
plt.show()


cv2.waitKey(0)