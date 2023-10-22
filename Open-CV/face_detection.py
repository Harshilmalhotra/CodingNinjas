#Harshil Malhotra
"""
As haar cassades are very vulnurable to noise so to avoid unwanted rectangles change scalefactor & neighbour parameters ....
"""



import cv2 as cv
# #original Image....
img = cv.imread('Resources\Photos\group 2.jpg')
# cv.imshow('Group of 5 people', img)
#
#
#
# #gray image...
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray_photo', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

print(f'Number of faces found = {len(faces_rect)}')

#rectangles on the faces...
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)


cv.imshow('Detected_Faces', img)
cv.waitKey(0)