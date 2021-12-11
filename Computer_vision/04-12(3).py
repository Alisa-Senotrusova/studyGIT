import cv2
#import numpy as np
import time

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)

#lowerGreen = (65, 90, 75) 
#upperGreen = (105, 255, 255)

#lowerOrange = (5, 120, 150)
#upperOrange = (10, 255, 255)

#lowerYellow = (20, 70, 150)
#upperYellow = (40, 255, 255)

lower = [(65, 90, 75), (5, 120, 150), (20, 70, 150)]
upper = [(105, 255, 255), (10, 255, 255), (40, 255, 255)]

prev_time = time.time()
curr_time = time.time()
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0 
d = 5.6 * 10 ** -2 
radius = 1

while cam.isOpened():
    _, image = cam.read()
    curr_time = time.time()
    blurred = cv2.GaussianBlur(image, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    for i in range(len(lower)):
        mask = cv2.inRange(hsv, lower[i], upper[i])
        mask = cv2.erode(mask, None, iterations = 2)
        mask = cv2.dilate(mask, None, iterations = 2)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
    
        if len(cnts) > 0:
            c = max(cnts, key = cv2.contourArea)
            (curr_x, curr_y), radius = cv2.minEnclosingCircle(c)
            if radius > 10:
                cv2.circle(image, (int(curr_x), int(curr_y)), int(radius),\
                           (0, 255, 255), 2)
    
    cv2.imshow("Camera", image)
    #cv2.imshow("Mask", mask)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
