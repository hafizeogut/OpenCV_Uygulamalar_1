import cv2

img=cv2.imread("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//3_Test_images//face.png")

#Cascade dosyası çalışmaya dahil edildi.
face_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//frontalface.xml")

#Resmin anlaşılır olması için gray tonlarına çevriliyor.
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#1.3 küçültme oranı iken 4 yüz arayacak olan pencere sayısıdır
faces=face_cascade.detectMultiScale(gray,1.3,7)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
    
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()