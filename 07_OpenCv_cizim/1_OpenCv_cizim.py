import cv2
import numpy as np

canvas_tuval=np.zeros((512,512,3),dtype=np.uint8)+210#belirli bir alanı tuval uluiturmaktır.
                    #((tuvalin eni,tuvalin boyu,kanal sayısı 3 RGB),Tuvalin veri tipi)

#tuvali siyahtan beyaza çevirme bgr(0,0,0) +255
cv2.imshow("Canvas",canvas_tuval)   
cv2.waitKey(0)
cv2.destroyAllWindows()
print(canvas_tuval)