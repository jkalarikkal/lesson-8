import cv2
import os

haarfile = "/Users/jaanvikalarikkal/Desktop/open CV/lesson 8/haarcascade_frontalface_default.xml"
dataset = "/Users/jaanvikalarikkal/Desktop/open CV/lesson 8/dataset"

subdata =  "jaanvi"

path = os.path.join(dataset, subdata)

if not os.path.isdir(path):
    os.mkdir(path)

(width, height) = (130,100)

face_cascade = cv2.CascadeClassifier(haarfile)

webcam = cv2.VideoCapture(0)
count = 1

while count <= 30:
    (ret, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w, y+h) , (255,0,0),2)
        face = gray[y:y + h, x:x + w]
        rezize  = cv2.resize(face, (width,height))
        cv2.imwrite('% s/% s.png' % (path, count), rezize)

    count = count + 1
    cv2.imshow("face", im)
    key = cv2.waitKey(0)
    if key == 27:
        break
    

