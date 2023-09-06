# Take each frame of the video
# Convert from BGR to HSV color-space
# We threshold the HSV image for a range of blue color
# Now extract the blue object alone, we can do whatever on that image we want.

import cv2
import numpy as np

# Initialize video capture
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the red color in HSV
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([30, 255, 255])

    # Create a mask to isolate the red color
    mask = cv2.inRange(hsv_frame, lower_red1, upper_red1)

    # Apply bitwise AND operation to highlight red regions
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
