import cv2
import numpy as np
import pytesseract #metin okuma
import imutils  #Goruntu üzerindeki temel işlemler

img=cv2.imread("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//3_Test_images")
cv2.imshow("lincle plate",img)


cv2.waitKey(0)
cv2.destroyAllWindows()

