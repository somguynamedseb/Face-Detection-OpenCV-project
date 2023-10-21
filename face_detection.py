#pylint:disable=no-member

import cv2 as cv

img = cv.imread(r'Resources\Group_Photos\Retreat 23-24 Group\20231016210431-ba0e08a2-la.jpg')
# cv.imshow('Group of 5 people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow('Detected Faces', img)
# img2 = cv.resize(img, (500,500))
# img3 = cv.resize(img, (1000,1000))


cv.waitKey(0)