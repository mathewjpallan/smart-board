# smart-board
Using a mobile phone to track a physical object as a pointer. This can be used to convert a projector display and using the physical object to navigate around. This program uses open-cv to detect a red coloured pointer.

## Steps to run the program
1. Clone the repo
2. Open https://preprod.ntp.net.in/play/content/do_312473549722288128119665?contentType=Resource on a browser and project your display on to a wall with white background.
3. Update the screen resolution variable in smartboard.py
4. Install IP Webcam android app. Position the mobile cam towards the projected wall and start the app. The app will expose a URL that can be used to access the video stream from the app. Please note that you should set the capture FPS to 5/sec and resolution to 640*480 or the video stream becomes really slow.
5. Execute python smartboard.py. This program will help you to crop the projected screen area from the entire camera frame. Your cropped image should contain your entire screen display on the wall.

An image is worth a 1000 words - I will probably add an image demoing this later.

## How the program works
1. Capture the image and convert the image to HSV. 
2. Filter for HSV ranges of red as I am using a red pointer. My pointer is a stick with a red ribbon as the tip.
3. On the filtered image, find the biggest contour as this will be the pointer. (This will be a challenge if the screen has red objects and the pointer detection accuracy can be increased in such cases by using 2 coloured ribbons - red and green as the tip and using 2 masks and detecting the ribbons side by side)
4. Convert the coordinate of the contour to screen coordinates and move the mouse pointer to that location.
