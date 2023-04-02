import cv2

img=cv2.imread("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//3_Test_images//smile.jpg")

face_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//frontalface.xml")
smile_cascade=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//smile.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    
roi_img=img[y:y+h,x:x+h]
roi_gray=gray[y:y+h,x:x+h]

smiles=smile_cascade.detectMultiScale(roi_gray,1.3,5)

for (sx,sy,sw,sh) in smiles:
    cv2.rectangle(roi_img,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
    
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    