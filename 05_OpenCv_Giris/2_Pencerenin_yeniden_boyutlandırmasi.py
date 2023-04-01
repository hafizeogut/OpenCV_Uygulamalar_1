import cv2

#cv2.namedWindow("cicek",cv2.WINDOW_NORMAL)#resme yeniden boyutlandırma özelliği kazandırıldı.
img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\cicek.jpg")

img=cv2.resize(img,(640,480))


cv2.imshow("cicek",img)
cv2.waitKey(0)
cv2.destroyAllWindows()