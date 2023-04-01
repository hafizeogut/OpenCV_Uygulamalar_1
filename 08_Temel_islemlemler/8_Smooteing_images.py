#Resimleri yumuşatma
import cv2
import numpy as np

img_filter=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\filter.png")
img_median=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\median.png")
img_bilateral=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\bilateral.png")

blur=cv2.blur(img_filter,(5,5))
# blur=cv2.blur(img_filter,(15,15))
# blur=cv2.blur(img_filter,(7,10))

blur_gaussian=cv2.GaussianBlur(img_filter,(15,15),cv2.BORDER_DEFAULT)
blur_median=cv2.medianBlur(img_median,9)#15 9 g,b, tek sayı olmalıdır

blur_bilateral=cv2.bilateralFilter(img_bilateral,9,50,50)

# cv2.imshow("original",img_filter)
#cv2.imshow("original",img_median)
cv2.imshow("original",img_bilateral)


# cv2.imshow("blur",blur)
# cv2.imshow("Gasussianblur",blur_gaussian)
#cv2.imshow("Median Blur",blur_median)
cv2.imshow("Bilateral Blur",blur_bilateral)



cv2.waitKey(0)
cv2.destroyAllWindows()