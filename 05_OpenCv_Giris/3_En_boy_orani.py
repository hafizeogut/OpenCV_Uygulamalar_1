import cv2

def resize_with_aspecth_ratio(img,width=None,height=None,inter=cv2.INTER_AREA):#inter=cv2.INTER_AREA Resim yendien boyutlandırılırken oluşan sorunların önüne geçmek
    
    dimension_boyut=None
    
    (h,w)=img.shape[:2]#en boy değerleri atandı.
    
    if width is None and height is None:
        return img
    
    if width is None:
        r=height/float(h)#
        dimension_boyut=(int(w*r),height)
        
    else:
        r=width/float(w)
        dimension_boyut=(width,int(h*r))
        
    return cv2.resize(img,dimension_boyut,interpolation=inter)

img=cv2.imread("C:\OpenCv_Uygulamalar_1\src\cicek.jpg")
img1=resize_with_aspecth_ratio(img,width=None,height=600,inter=cv2.INTER_AREA)

cv2.imshow("Original",img)
cv2.imshow("resized",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    