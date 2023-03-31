import cv2
import numpy as np


img =cv2.imread("C:\OpenCv_Uygulamalar_1\src\cicek.jpg"   )

#Resmin en boy ve kanal sayısı öğrenildi.
dimesion=img.shape
print(dimesion)

color=img[650,400] #resim aralığıdaki b g r değerleri bulundu.
print("BGR",color)

#640 a 400 aralığındaki mavi değerlerini elde edildi.
blue=img[650,400,0]
print(blue)

#640 a 400 aralığındaki yeşil değerlerini elde edildi.
green=img[650,400,1]
print("Green",green)

#640 a 400 aralığındaki kırmızı değerlerini elde edildi.
red=img[650,400,2]
print("Red",red)

img[650,400,0]=245#img.itemset()
print("new blue",img[650,400,0])

#150
blue1=img.item(150,200,0)
print("blue1",blue1)
img.itemset((150,200,0),172)#atsama işlemi
print("new blue1",img[150,200,0])

cv2.imshow("Cicek",img)
cv2.waitKey(0)
cv2.destroyAllWindows()