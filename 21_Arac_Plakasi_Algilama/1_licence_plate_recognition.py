import cv2
import numpy as np
import pytesseract #metin okuma
import imutils  #Goruntu üzerindeki temel işlemler

img=cv2.imread("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//3_Test_images//licence_plate.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#edged1=cv2.Canny(gray,30,200)
#Resimleri yumuşatarak keskin çizgileri yumuşatma işlemi yapılıyor.
filtered=cv2.bilateralFilter(gray,6,250,250)

#Köşeleri Algılama
edged=cv2.Canny(filtered,30,200)

#Kontur sınırlarının kordinatları bulunuyor.
contours=cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) [:10]
##print("contours",contours)

#Uygun konturlar yakalanıyor.
cnts=imutils.grab_contours(contours)
##print("cnts",cnts)

#Kordinatlar alanlarına göre sıralanıyor.True=girilen değerleri tersten sıralanıyor.
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)
##print("cnts",cnts)

screen=None#Kapalı şekil bulundu mu?

for c in cnts:
    #Bulunan konturlar düzeltiliyor
    epsilon=0.018*cv2.arcLength(c,True)
    #kat sayı,epsilon=0.018*cv2.arcLength(c-->,True-->Boşluk var mı yok mu?)-->Konturların yay uzunluğu bulunuyor.
    
    #approx=yaklaşım Daha yaklaşılmış fonksiyon tutuluyor
    approx=cv2.approxPolyDP(c,epsilon,True)
    
    if len (approx)==4:
        screen=approx
        break
##print("screen",screen) 

#Siyah bir ekran oluituruldu.     
mask=np.zeros(gray.shape,np.uint8)

#Plaka alanı beyaza boyanıyor
new_image=cv2.drawContours(mask,[screen],0,(255,255,255),-1)

#arabayı beyaz alanla and işlemi uygulandı.
new_image= cv2.bitwise_and(img,img,mask=mask)

#new_image resmi kırpılıyor
(x,y)=np.where(mask==(255))

##print(np.where(mask==(255)))

#Bilgisayarada SOL ÜST (0,0)
#En büyük x ve y kordinatları bulundu.
(topx,topy)=(np.min(x),np.min(y))
(bottomx,bottomy)=(np.max(x),np.max(y))

#Kırpma işlemi yapılıyor.
cropped=gray[topx:bottomx+1,topy:bottomy+1]

text=pytesseract.image_to_string(cropped,lang="eng")
print("detevted text",text)



# cv2.imshow("gray",gray)
# cv2.imshow("mask",mask)
# cv2.imshow("new_image",new_image)
cv2.imshow("cropped",cropped)

# cv2.imshow("1_img",img)
# cv2.imshow("2_gray",gray)
# cv2.imshow("3_filtered",filtered)
# cv2.imshow("4_edged",edged)
#cv2.imshow("4_edged1",edged1)


cv2.waitKey(0)
cv2.destroyAllWindows()

