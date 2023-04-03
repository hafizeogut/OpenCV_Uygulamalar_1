import numpy as np

import matplotlib.pyplot as plt

path="C:\OpenCv_Uygulamalar_1\src\coins.jpg"
img=plt.imread(path)

print("img: ",img)
print("type(img): ",type(img))
print("img.shapeq",img.shape)
print("img.size: ",img.size)
print("img.dtype: ",img.dtype)


#Resmin chanel değerlerine erişiliyor.
#Matplotlib RGB
print("red chanel: ",img[50,50,0])#RGB 0 ->R 1->G 2->B
print("Green chanel: ",img[50,50,1])
print("Blue chanel: ",img[50,50,2])

print("rgb chanel value: ",img[50,50,2])
plt.imshow(img)
plt.show()