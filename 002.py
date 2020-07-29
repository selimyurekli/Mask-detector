import cv2
import numpy as np 


resim = np.zeros((600,600),'uint8')

resim = cv2.line(resim,(20,0),(20,20),(255,255,255),1)
resim = cv2.circle(resim, (20,20),20,(255,255,255),1)
resim = cv2.rectangle(resim,(10,40),(30,0),(255,255,255),1)


cv2.imshow("..",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
