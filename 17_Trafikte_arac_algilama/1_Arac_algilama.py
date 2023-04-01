import cv2 
 
img=cv2.imread("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//3_Test_images//car.jpg")

car=cv2.CascadeClassifier("C://OpenCv_Uygulamalar_1//13_Haar_Cascade//1_Haarcascade//car.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bodies=car.detectMultiScale(gray,1.1,2)

for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()