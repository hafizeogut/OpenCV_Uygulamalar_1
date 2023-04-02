import cv2

#Resim ilk haliye BGR durumdadır.
img=cv2. imread("C:\OpenCv_Uygulamalar_1\src\cicek.jpg")

img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Cicek BGR",img)
#cv2.imshow("Cicek RGB",img_rgb)
#cv2.imshow("Cicek HSV",img_hsv)
cv2.imshow("Cicek GRAY",img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()