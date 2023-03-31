import cv2
import numpy as np

img=cv2.imread("C:\\OpenCv_Uygulamalar_1\\src\\star.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,127,255,0)

#İlk argüman, konturları bulmak istediğimiz ikili görüntüdür.
# İkinci argüman kontur alma modunu belirtir. Bu durumda, cv2.RETR_TREEtüm konturları alır ve iç içe geçmiş konturların tam bir hiyerarşisini yeniden oluşturur.
# Üçüncü bağımsız değişken, kontur yaklaşım yöntemini belirtir. Bu durumda, cv2.CHAIN_APPROX_SIMPLEyatay, dikey ve çapraz parçaları sıkıştırır ve yalnızca bitiş noktalarını bırakır.
contours,_=cv2.findContours(thresh,2,1)

cnt=contours[0]
#Dışbğkey örtü oluşturuluyor.
hull=cv2.convexHull(cnt,returnPoints=False)

#kusurlar tespit ediliyor.
defect_kusurlar=cv2.convexityDefects(cnt,hull)
print(hull)

#dış bükey cizgiler oluşturuluyor.
for i in range(defect_kusurlar.shape[0]):
    s,e,f,d=defect_kusurlar[i,0]
    #s:start point uç noktaların başlangıcı,e:end point
    #f:furthest point :en uzak nokta,d:distance: mesafe
    
    start_point=tuple(cnt[s][0])
    end_point=tuple(cnt[e][0])
    far_point=tuple(cnt[f][0]) 
    
    cv2.line(img,start_point,end_point,[0,255,0],2)
    cv2. circle(img,far_point,5,[0,255,0],-1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
