#Kütühane içeri aktarıldı.
import cv2
 
#Resim okuma
img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\cicek.jpg")

#print(img)#resimler renk yoğunluklarından oluşan birer matrislerdir.

cv2.namedWindow("Image",cv2.WINDOW_NORMAL)#pencerenin ismi,pencerenin yeniden boyutlandırılanilmesi.

#Resim Gösterme
cv2.imshow("Image",img)#resmin gösterelieceği pencere ekranı oluşturuldu.

#Resim kaydetme
cv2.imwrite("C:\OpenCv_Uygulamalar_1\output\cicek.jpg",img)

cv2.waitKey(0)#girilen değer kadar ekranda tutulur.m/s
cv2.destroyAllWindows()#pencerelerin kapanması adına önemli bir fonksiyondur.

