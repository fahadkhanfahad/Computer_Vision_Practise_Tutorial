import cv2
import numpy as np

def nothing(x):
    pass

capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

cv2.namedWindow("Trackbars")

cv2.createTrackbar("lh", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("ls", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("lv", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("uh", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("us", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("uv", "Trackbars", 255, 255, nothing)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # ... Image processing goes here ...

    # Read the trackbar values
    lh = cv2.getTrackbarPos("lh", "Trackbars")
    ls = cv2.getTrackbarPos("ls", "Trackbars")
    lv = cv2.getTrackbarPos("lv", "Trackbars")
    uh = cv2.getTrackbarPos("uh", "Trackbars")
    us = cv2.getTrackbarPos("us", "Trackbars")
    uv = cv2.getTrackbarPos("uv", "Trackbars")

    # ... Use these values for processing ...

    cv2.imshow("trackbar", frame)

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
