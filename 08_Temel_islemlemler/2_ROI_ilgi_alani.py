#roi--> region of interest-->ilgi alanı

import cv2

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\cicek.jpg")
#print(img.shape[:200])

#[dikey eksen,yatay eksen]
roi=img[1:300,125:325]

cv2.imshow("Cicek",img)
cv2.imshow("ROI",roi)


cv2.waitKey(0)
cv2.destroyAllWindows()