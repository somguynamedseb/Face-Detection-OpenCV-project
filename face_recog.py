#pylint:disable=no-member

import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Aiden S', 'Bryce', 'Caleb', 'Charlie','Ethan','Henry','Issa','Jeff','Jim','John','Matthew','Nate','Nathanel','Scott','Sean','Spencer','Tyler','Vijay','Wyatt']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'Resources\KAP_Gentlemen\Ethan\20231016221305-b3f94bfc-la.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 8)
dist = 30
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (20,dist), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    dist = 30+dist
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)
