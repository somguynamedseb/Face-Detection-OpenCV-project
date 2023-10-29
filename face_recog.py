#pylint:disable=no-member

import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Bryce', 'Caleb', 'Chase','Charlie','Ethan','Graham','Henry','Issa','Jeff','Jim','Matt Duncan','Matthew','Nate','Scott','Sean','Sebastian B','Shen','Spencer','Teddy','Tyler','Vijay','Wyatt']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# img = cv.imread(r'Resources\Group_Photos\Retreat 23-24 Group\20231016221434-f28fc50e-xl.jpg') #good except for random detections
# img = cv.imread(r'Resources\Group_Photos\20230929131522-a00fa559-xx.jpg') #currently good except for John
img = cv.imread(r'Resources\Group_Photos\20230828003535-4c8dd4c5-la.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 10)
dist = 30
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (x,y-10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=1)
    dist = 30+dist
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)
print(faces_rect)

cv.waitKey(0)
