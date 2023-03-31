#Blurry İmage Detec

import cv2

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\starwars.jpg")
blurry_img=cv2.medianBlur(img,7)

#Resim blur lu mu yoksa değilmi tespit ediliyor.
laplacian=cv2.Laplacian(blurry_img,cv2.CV_64F).var()
#print("laplacian blurr",laplacian)

if laplacian<500:
    print("Bllurry image")
    
    
cv2.imshow("img",img)
cv2.imshow("blurry_img",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()