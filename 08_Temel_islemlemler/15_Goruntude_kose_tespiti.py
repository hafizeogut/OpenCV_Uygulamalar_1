#Koşelerin tespit edilmesi

import cv2
import numpy as np

img=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\text.png")
img1=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\contour.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Çember çizerken float sayı kullanılamıyor bu sebeple:
#gray değişkeni float32 formatına çevrildi.
gray=np.float32(gray)

#(Çalışılacak resim, max bulunabilecek köşe sayısı,kalite değeri,köşeler arası minimum uzaklık)
corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)

corners=np.int0(corners)

for corner in corners:
    #piksel değerleri tek boyutlu bir dizi yek boyutlu bir diziye sıkıştırıldı.
    x,y=corner.ravel()
    cv2.circle(img,(x,y),3,(0,255,255),-1)
    
cv2.imshow("Corner",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

