import cv2
import numpy as np 


kamera = cv2.VideoCapture(0)
faceCasc =cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml ')
eyeCasc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_nose.xml')
smileCasc = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_mouth.xml')

while(True):
    _,resim = kamera.read()
    #resim= cv2.imread("fotos/smile.jpg")
    grayColors = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    faces= faceCasc.detectMultiScale(grayColors,1.1,3)


    ctr = 0
    for(x,y,w,h) in faces:
        cv2.rectangle(resim,(x,y),(x+w,y+h),(0,255,0),1)
        faceFamilyGray = grayColors[y:y+h,x:x+w]
        faceFamily = resim[y:y+h,x:x+w]
        eye = eyeCasc.detectMultiScale(faceFamilyGray)
        smile = smileCasc.detectMultiScale(faceFamilyGray)
        for(k,l,t,u) in eye:
            cv2.rectangle(faceFamily,(k,l),(k+t,l+u),(0,0,255),2) 
        for(a,b,e,f) in smile:
            cv2.rectangle(faceFamily,(a,b),(a+e,b+f),(255,0,0),1)
            ctr = ctr+1
            break 
            
    if(ctr > 0):cv2.putText(resim,"Maske yok",(70,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
    else:cv2.putText(resim,"Maskeli",(70,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow("yüz",resim)
    if(cv2.waitKey(200)& 0xFF==ord('q')):
        break
    






cv2.waitKey(0) 
cv2.destroyAllWindows()




