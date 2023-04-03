import cv2
import matplotlib.pyplot as plt

path="C://OpenCv_Uygulamalar_1//src//smile.jpg"


img=cv2.imread(path,1)#1 BGR 0->grayscale
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(img,cmap='gray',interpolation='BICUBIC')#RGB
plt.show()