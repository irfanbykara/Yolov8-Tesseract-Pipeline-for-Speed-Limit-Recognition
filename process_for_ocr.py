import cv2
import numpy as np
from matplotlib import pyplot as plt
from utils import *


def crop_circle_with_text(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    # Blur using 3 * 3 kernel.
    thresh1 = cv2.blur(thresh1, (3, 3))

    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(thresh1,
                                        cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                        param2=40, minRadius=10, maxRadius=500)
    center_y = thresh1.shape[0] / 2
    center_x = thresh1.shape[1] / 2

    i = 0
    max_dist = 50000 # Setting a really big number as the max.
    res_index = 0

    if detected_circles is not None:
        for circle in detected_circles[0]:

            dist = euclidian_distance(center_y,circle[0],center_x,circle[1])

            if dist < max_dist:
                max_dist = dist
                res_index = i
            i += 1

        detected_circles = detected_circles[0][res_index]

        # Draw circles that are detected.
        # Convert the circle parameters a, b and r to integers.

        detected_circles = np.uint16(np.around(detected_circles))

        a, b, r = detected_circles[0], detected_circles[1], detected_circles[2]

        # Draw the circumference of the circle.
        cv2.circle(thresh1, (a, b), r, (0, 255, 0), 2)
        mask = np.zeros(thresh1.shape[:2], dtype="uint8")
        cv2.circle(mask, (a, b), r, 255, -1)
        masked = cv2.bitwise_and(thresh1, thresh1, mask=mask)

        # Draw a small circle (of radius 1) to show the center.
        return masked

