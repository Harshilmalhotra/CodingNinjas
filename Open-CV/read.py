#Harshil Malhotra
#Reading Images and videos in open CV

# ******************************************
#reading images
# import cv2 as cv

# img=cv.imread('Resources\Photos\cat_large.jpg')    #opened file stored in img variable

# cv.imshow('Cat',img)    

# cv.waitKey(0)           #Wait for infinite amount of time till key is pressed on keyboard



#**********************************************
#reading Videos
import cv2 as cv
capture= cv.VideoCapture('Resources\Videos\dog.mp4')     #() take int 0,1,2,3.... or path of img  eg 0 will be webcam
while True:
    isTure,frame=capture.read()                          #reads video frame by frame

    cv.imshow('Video',frame)

    if cv.waitKey(20) &0xFF==ord('d'):                   #if letter d is pressed break out of loop
        break

capture.release()
cv.destroyAllWindows()


#error: (-215:Assertion failed) means file not found or file out of frames.
