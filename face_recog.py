#pylint:disable=no-member

import numpy as np
import cv2 as cv
import os
directory = r'C:\Users\sebas\Documents\GitHub\OpenCV-Project-1'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Adam','Bryce', 'Caleb', 'Chase','Charlie','Ethan','Graham','Henry','Issa','Jeff','Jim','Matt Duncan','Matthew','Nate','Scott','Sean','Sebastian','Shen','Spencer','Teddy','Tyler','Vijay','Wyatt']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# img = cv.imread(r'Resources\Group_Photos\Retreat 23-24 Group\20231016221434-f28fc50e-xl.jpg') #good with filter at 80
# img = cv.imread(r'Resources\Group_Photos\20230929131522-a00fa559-xx.jpg') #pretty good needs new recog model
# img = cv.imread(r'Resources\Group_Photos\20230828003535-4c8dd4c5-la.jpg') #bad
# img = cv.imread(r'Resources\Group_Photos\20230828003617-110b7384-la.jpg') #entirely wrong
img = cv.imread(r'Students_in_Large_Classroom_with_Laptops.jpg') #scotts face not detected

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 8)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    if confidence < 200.0:
        cv.putText(img, str(people[label]), (x,y-10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=1)
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

# cv.imshow('Detected Face', img)
print(faces_rect)

  
# List files and directories   
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'   
print("Before saving image:")   
print(os.listdir(directory))   
  
# Filename 
filename = 'savedImage.jpg'
  
# Using cv2.imwrite() method 
# Saving the image 
cv.imwrite(filename, img) 
cv.waitKey(0)
