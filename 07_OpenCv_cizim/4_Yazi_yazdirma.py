import cv2
import numpy as np

canvas=np.zeros((250,2620,3),dtype=np.uint8)+25

font1=cv2.FONT_HERSHEY_SIMPLEX
font2=cv2.FONT_HERSHEY_DUPLEX
font3=cv2.FONT_HERSHEY_COMPLEX

cv2.putText(canvas,"Niyeti temiz olanın yolu açık olur.",(50,150),font2,5,(0,3,0),cv2.LINE_AA)


cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()