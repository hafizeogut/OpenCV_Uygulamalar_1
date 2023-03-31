import cv2
import numpy as np
#Resimlerin arkasındaki sayısal değerlerini kariılaitırma.
path="C:\\OpenCv_Uygulamalar_1\\src\\aircraft.jpg"

img1=cv2.imread(path)
img1=cv2.resize(img1,(640,550))

img2=cv2.imread("C://OpenCv_Uygulamalar_1//src//aircraft1.jpg")
img2=cv2.resize(img2,(640,550))

img3=cv2.medianBlur(img1,7)
if img1.shape==img2.shape:
    print("same size")
    
else:
    print("not same")

#diiference:iki resmi karşılaştırıp farklı olan yerler tespit ediliyor. 
diff=cv2.subtract(img1,img3)

#b,g,r değerleri ayrıldı ve değişkenlerine atandı.
b,g,r=cv2.split(diff)
print(b)

#0 olmayan değerleri sayar
if cv2.countNonZero(b) ==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
    print("completely equal tamamen eşit")
    
else:
    print("NON completely equal")

cv2.imshow("Aircraft1",img1)
cv2.imshow("Aircraft2",img2)
cv2.imshow("Diference",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()