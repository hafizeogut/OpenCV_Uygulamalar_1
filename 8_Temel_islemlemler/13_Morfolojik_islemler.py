import cv2
import numpy as np

img_erosion=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\erosion.PNG",0)
img_dilation=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\dilation.PNG",0) 
img_opening=cv2.imread("C:\OpenCv_Uygulamalar_1\src\opening.PNG")
img_closing=cv2.imread("C:\OpenCv_Uygulamalar_1\src\closing.PNG")

#iterations=tekrar
kernel=np.ones((7,7),np.uint8)
erosion=cv2.erode(img_erosion,kernel,iterations=1)


#dilation:kalınlaştırma işlemi yapar.
dilation=cv2.dilate(img_dilation,kernel,iterations=3)

#opening:resmin üzerindeki gürğltğyğ kaldırılyor.
opening=cv2.morphologyEx(img_opening,cv2.MORPH_OPEN,kernel)

#closing:
closing=cv2.morphologyEx(img_closing,cv2.MORPH_CLOSE,kernel)

#Morpholog Gradiend:
gradient=cv2.morphologyEx(img_erosion,cv2.MORPH_GRADIENT,kernel)

#Morpholog Tophat:
tophat=cv2.morphologyEx(img_erosion,cv2.MORPH_TOPHAT,kernel)



# cv2.imshow("img_erosion",img_erosion)
# cv2.imshow("eresion",erosion)

# cv2.imshow("img_dilation",img_dilation)
# cv2.imshow("dilation",dilation)

# cv2.imshow("img_opening",img_opening)
# cv2.imshow("opening",opening)

# cv2.imshow("img_closing",img_closing)
# cv2.imshow("closing",closing)

cv2.imshow("img_erosion",img_erosion)
#cv2.imshow("gradient",gradient)

cv2.imshow("tophat",tophat)

cv2.waitKey(0)