import cv2 
import numpy as np
#https://pyimagesearch-com.translate.goog/2021/10/06/opencv-contour-approximation/?_x_tr_sl=en&_x_tr_tl=tr&_x_tr_hl=tr&_x_tr_pto=sc 
#Kontur alanını çok iyi açıklamış



#Şekillerin üzerine yazılacak resim için yürütülecek resimler.

font=cv2.FONT_HERSHEY_SIMPLEX#open cv fonts
font1=cv2.FONT_HERSHEY_COMPLEX

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\polygons.png") 
#Griye Çevriliiyor.

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Eşik değeri belirleniyor.
_,threshold=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

#Kontur işlemi yapılıyor.
#CHAIN_APPROX_SIMPLE gereksiz köşeleri kaldırır.
contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print("contours",contours)

for cnt in contours:
    #kapalı mı değilmi şekil True
    epsilon=0.01*cv2.arcLength(cnt,True)
    approx_yaklasma=cv2.approxPolyDP(cnt,epsilon,True)
    
    cv2.drawContours(img,[approx_yaklasma],0,(0),5)
    #np.Ravel() dik sıraları satıra döker
    #
    print("approx_yaklasma",approx_yaklasma)
    print("len aprox",len(approx_yaklasma))
    x=approx_yaklasma.ravel()[0]
    y=approx_yaklasma.ravel()[1]
    
    if len(approx_yaklasma)==3:#approx un uzuluğu 3 ise
        cv2.putText(img,"Triangle",(x,y),font1,1,(0))
        
    elif len(approx_yaklasma)==4:#approx un uzuluğu 3 ise
        cv2.putText(img,"Rectangle",(x,y),font1,1,(0))
        
    elif len(approx_yaklasma)==5:#approx un uzuluğu 3 ise
        cv2.putText(img,"Pentogon",(x,y),font1,1,(0))
    
    elif len(approx_yaklasma)==6:#approx un uzuluğu 3 ise
        cv2.putText(img,"Hexagon",(x,y),font1,1,(0))
    
    else: 
        cv2.putText(img,"Ellipse",(x,y),font1,1,(0))
    
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()