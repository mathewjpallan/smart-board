import cv2 as cv
import numpy as np
from collections import deque
from pynput.mouse import Button, Controller

cap = cv.VideoCapture(2) #This is for accessing the video stream from webcams that are attached to the workstation

#Read a frame from the camera
ret, frame = cap.read()
counter = 99999
#Start capturing the frames from the cam till the user chooses to exit by pressing q
while True:
    ret, frame = cap.read()

    #Conver the cropped area to HSV as it is easier to apply colour filters in HSV images
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #Applying a filter for RED color as our pointer is red
    rlower = np.array([0, 120, 70])
    rupper = np.array([10, 255, 255])
    rmask1 = cv.inRange(hsv, rlower, rupper)

    rlower = np.array([170, 120, 70])
    rupper = np.array([180, 255, 255])
    rmask2 = cv.inRange(hsv, rlower, rupper)

    mask = rmask1 + rmask2
    contours, hierarchy = cv.findContours(mask, 
                                    cv.RETR_TREE, 
                                    cv.CHAIN_APPROX_SIMPLE)
    #sorting and finding the biggest contour of red colour which should our pointer object.
    contours = sorted(contours, key = cv.contourArea, reverse = True)
    cv.imshow('mask', mask)
    if (len(contours) > 1):
        x,y,w,h = cv.boundingRect(contours[0])
        w += 1
        h += 1
        e1 = frame[y-30:y+h+30, x-30:x+w+30]
        cv.imshow('e1', e1)
        cv.imwrite('gen/pos' + str(counter) + '.png', e1)
        counter += 1
    
    if cv.waitKey(10) == ord('q'):
        break

#Releasing all resources before exit
cap.release()
cv.destroyAllWindows()