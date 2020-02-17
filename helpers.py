import cv2 as cv

def getProjectionAreaCoordinates(srcImage):
    showCrosshair = False
    fromCenter = False
    r = cv.selectROI(srcImage)
    cv.destroyAllWindows()
    return (int(r[1]),int(r[1]+r[3]), int(r[0]),int(r[0]+r[2]))

def mapCamCoordinatesToScreenCoordinates(point, camCoordinates):
    #Change your screen resolution here
    resScreen = [1920, 1080]
    #The camResolution is measured from the projection area coordinates
    resImage = [(camCoordinates[3] - camCoordinates[2]), (camCoordinates[1] - camCoordinates[0])]
    return ((resScreen[0] / resImage[0]) * point[0], (resScreen[1] / resImage[1]) * point[1] )

def isPointer(contour):
    #Helper function which checks that the area of the contour is above a threshold. The threshold values were 
    #figured out by printing the values when the pointer was detected in the image.
    if cv.contourArea(contour) > 10 or cv.arcLength(contour, True) > 10:
        return True
    else:
        return False