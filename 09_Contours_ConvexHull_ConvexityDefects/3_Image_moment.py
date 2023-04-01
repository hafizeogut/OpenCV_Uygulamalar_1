import cv2

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\contour.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
Moments=cv2.moments(thresh)
print(Moments)
#Moments değeri bir sözlük formatındadır.
#'m00': 15946170.0, 'm10': 2512158510.0, 'm01': 2140943280.0, 'm20': 568586636580.0,

#Geometri merkezindeki x ve y kordinatları bulunuyor.
X=int(Moments["m10"]/Moments["m00"])
Y=int(Moments["m01"]/Moments["m00"])

cv2.circle(img,(X,Y),5,(156,0,156),-1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()