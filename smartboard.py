import cv2 as cv
import numpy as np
from pynput.mouse import Button, Controller
from helpers import *

mouse = Controller()

while True:
    userReady = raw_input('Point the cam towards the projector output and press the y key when ready - ')
    if userReady == 'y':
        break;

#Running the IP webcam apk on a mobile and reading the video stream from that device. The IP address below is that shown in the IP webcam app display.
#cap = cv.VideoCapture('http://10.42.0.66:8080/video')
cap = cv.VideoCapture(0) #This is for accessing the video stream from webcams that are attached to the workstation

if not cap.isOpened():
    print("Cannot open camera")
    exit()

#Read a frame from the camera
ret, frame = cap.read()

# if frame is read correctly ret is True
if not ret:
    print("Can't receive frame (cam enabled?). Exiting..")
    exit()

camCoordinates = getProjectionAreaCoordinates(frame)

#Start capturing the frames from the cam till the user chooses to exit by pressing q
while True:
    ret, frame = cap.read()
    crop = frame[camCoordinates[0]:camCoordinates[1], camCoordinates[2]:camCoordinates[3]]

    #Conver the cropped area to HSV as it is easier to apply colour filters in HSV images
    hsv = cv.cvtColor(crop, cv.COLOR_BGR2HSV)

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
        #pick the first contour which is the biggest as it is sorted
        contour = contours[0]
        if isPointer(contour):
            #find the extreme left point of the contour.
            extLeft = tuple(contour[contour[:, :, 0].argmin()][0])
            print('extLeft' + str(extLeft))

            screenCoordinates = mapCamCoordinatesToScreenCoordinates(extLeft, camCoordinates)
            print('screenCoordinates' + str(screenCoordinates))
            #Moving the mouse pointer to the detected screen coordinates
            mouse.position = (1920 + int(screenCoordinates[0]), int(screenCoordinates[1]))
    if cv.waitKey(50) == ord('q'):
        break

#Releasing all resources before exit
cap.release()
cv.destroyAllWindows()