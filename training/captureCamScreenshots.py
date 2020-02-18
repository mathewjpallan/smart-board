import cv2 as cv
import numpy as np

#This program is used to capture cam shots for training a haar classifier
cap = cv.VideoCapture(2)
counter = 999999
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    #Read a frame from the camera
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (cam enabled?). Exiting..")
        exit()
    cv.imshow ('cap', frame)
    cv.imwrite('gen/neg' + str(counter) + '.png', frame)
    counter += 1
    cv.waitKey(100)

cap.release()
cv.destroyAllWindows()