import cv2
import numpy as np
import math

video=cv2.VideoCapture(0)

while True:
    try:
        ret,frame=video.read()
        frame=cv2.flip(frame,1)
        
        kernel=np.ones((3,3),np.uint8)
        
        roi=frame[100:300,100:300]
        cv2.rectangle(frame,(100,100),(300,300),(0,0,255),0)
        
        #mask işlemlerinde hsv daha kullanıişlıdır
        hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
        
        #Nesne elimiz.
        lower_skin=np.array([0,20,70],np.uint8)
        upper_skin=np.array([20,255,255],np.uint8)
        
        mask= cv2.inRange(hsv,lower_skin,upper_skin)
        
        #oluşan karanlık noktaları beyazlara değiştirme.
        #maskın yeni şekli
        mask=cv2.dilate(mask,kernel,4)
        
        #Blur yöntemi ile gürültüler siliniyor
        mask=cv2.GaussianBlur(mask,(5,5),10)
        
        #Konturlar bulunuyor
        _,contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        #Konturların max alanı belirleniyor
        cnt=max(contours,key=lambda x:cv2.contourArea(x))
        
        #Konturlara daha iyi bir yaklaşım sağlanıyor.
        epsilon=0.0005*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
        
        #Dışbükey örtü kordinarları oluituruluyor.
        hull=cv2.convexHull(cnt)
        
        area_hull=cv2.contourArea(hull)
        area_cnt=cv2.contourArea(cnt)
        area_ratio=((area_hull-area_cnt)/area_cnt*100)
        
        #Dış Bükey kusurlar tespit ediliyor
        
        #ilk convexhull ile konturların indislerine ulaşılıyo.
        #True=konturlar,False=indisler
        hull=cv2.convexHull(approx,returnPoints=False)
        
        #Dışbükey kusurlar değişkene atanıyor
        defects=cv2.convexityDefects(approx)
        
        #Toplam kusur sayısı=0
        l=0
        for i in range(defects.shape[0]):
            s,e,f,d=defects[i,0]
            start=tuple(approx[s][0])
            end=tuple(approx[e][0])
            far=tuple(approx[f][0])
            
            #karekök(son nokta baişalnğıç noktasından çıkartılıp karesi alınıyor).
            a=math.sqrt((end[0]-start[0])**2+(end[0]-start[0])**2)
            b=math.sqrt((far[0]-start[0])**2+(far[0]-start[0])**2)
            c=math.sqrt((end[0]-far[0])**2+(end[0]-far[0])**2)
            
            #oluşan üçgenin alanı bulunuyor.
            s=(a+b+c)/2
            area=math.sqrt(s*(s-a)*(s-b)*(s-c))
            #Noktalar dışbükey noktalar arası mesafe tespit ediliyor.
            d=2*area/a
            
            #cos kuralu= iki kenar arası açı
            angle=math.acos((b**2+c**2-a**2)/(2*b*c))*57
            if angle <=90 and d>30:
                l+=1
                cv2.circle(roi,far,3,[255,0,0],-1)
                
            #star end noktalarını kullanarak bir çizgi çiziliyor
            cv2.line(roi,start,end,[255,0,0],2)
            l+=1
            
            font=cv2.FONT_HERSHEY_SIMPLEX
            if l==1:
                if area_cnt<2000:
                    cv2.putText(frame,"Put your in the box:",(0,50),50,(0,0,255,3,cv2.LINE_AA))
                    
                else:  
                    #elin olmadığı alanın yüzdesi
                    if area_ratio<12:
                        cv2.putText(frame,"0",(0,50),50,(0,0,255,3,cv2.LINE_AA))
                    elif area_ratio <17.5:
                        cv2.putText(frame,"Bol şans",(0,50),50,(0,0,255,3,cv2.LINE_AA))

                    else:
                        cv2.putText(frame,"1",font,2,(0,0,255),3,cv2.LINE_AA)
            
            elif l==2:
                cv2.putText(frame,"2",(0,50),50,(0,0,255,3,cv2.LINE_AA))
                
            elif l==3:
                #ratio area: orean alanı
                if area_ratio<27:
                    cv2.putText(frame,"2",(0,50),50,(0,0,255,3,cv2.LINE_AA))
                
                else:
                    cv2.putText(frame,"OK",(0,50),50,(0,0,255,3,cv2.LINE_AA))
                    
            elif l==4:
                cv2.putText(frame,"4",(0,50),50,(0,0,255,3,cv2.LINE_AA))
                
            elif l==5:
                cv2.putText(frame,"5",(0,50),50,(0,0,255,3,cv2.LINE_AA))
                
            elif l==6:
                cv2.putText(frame,"Reposition",(0,50),50,(0,0,255,3,cv2.LINE_AA))
        
            else: 
                cv2.putText(frame,"4",(0,50),50,(0,0,255,3,cv2.LINE_AA))
                
            cv2.imshow("mask",mask)
            cv2.imshow("frame",frame)

    except:
        pass
    k=cv2.waitKey(5) &0xFF
    if k==27:
        break
    
video.release()
cv2.destroyAllWindows()