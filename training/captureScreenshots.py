import numpy as np
import pyautogui
import imutils
import cv2 as cv

#This program is used to capture screen shots for training a haar classifier
counter = 0
while True:
    image = pyautogui.screenshot()
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    cv.imwrite('gen/neg' + str(counter) + '.png', image)
    counter += 1
    cv.waitKey(100)
cv.destroyAllWindows()