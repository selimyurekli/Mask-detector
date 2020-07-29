import cv2
import numpy as np 



resim = cv2.imread("resmi.jpg")
cv2.imshow("Selim deneme", resim)
print(resim[(1,1)])
cv2.waitKey(0)
cv2.destroyAllWindows()










#cv2.imwrite("renksiz.png", resim)









