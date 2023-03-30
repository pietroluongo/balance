import cv2
import numpy as np
from statistics import mean
import imutils

vid = cv2.VideoCapture(0)
lower_bound = np.array([0, 100, 100])
upper_bound = np.array([40, 255, 255])


while(True):
    ret, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    coord = cv2.findNonZero(mask)

    M = cv2.moments(mask)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        print('centroid X: ', cx, 'centroid Y: ', cy)
        cv2.circle(frame, (int(cx), int(
            cy)), 5, (255, 0, 0), -1)

    if coord is not None:
        amountOfOrange = np.shape(coord)[0]
        pixels = coord[0]
        t = np.transpose(pixels)
        print('mean X: ', mean(t[0]), 'Y mean: ', mean(t[1]))
        # cv2.circle(frame, (int(mean(t[0])), int(
        # mean(t[1]))), 5, (255, 0, 0), -1)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
