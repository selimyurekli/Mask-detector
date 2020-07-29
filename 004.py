import cv2

aile = cv2.imread("fotos/aile.jpg")
cascPath = cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
eyePath = cv2.data.haarcascades+"haarcascade_eye.xml"
smilePath = cv2.data.haarcascades+"haarcascade_smile.xml"

faceCascade = cv2.CascadeClassifier(cascPath)
eyeCascade = cv2.CascadeClassifier(eyePath)
smileCascade = cv2.CascadeClassifier(smilePath)


grayColors = cv2.cvtColor(aile,cv2.COLOR_BGR2GRAY)
faces = cascPath.detectMultiScale(grayColors,1.03,3)

for(x,y,w,h) in faces:
    cv2.rectangle(aile,(x,y),(x+w,y+h),(0,255,0),1)
    faceFamilyGray = grayColors[y:y+h,x:x+w]
    faceFamily = aile[y:y+h,x:x+w]
    eye = eyeCascade.detectMultiScale(faceFamilyGray,1.1,3)
    smile = smileCascade.detectMultiScale(faceFamilyGray,1.1,3)
   
    for(a,b,e,f) in eye:
        cv2.rectangle(aile,(a,b),(a+e,b+f),(255,0,0),1)  
    for(k,l,t,u) in smile:
        cv2.rectangle(aile,(k,l),(k+t,l+u),(0,0,255),2)      

cv2.imshow("yüz",aile)

cv2.waitKey(0) 
cv2.destroyAllWindows()
