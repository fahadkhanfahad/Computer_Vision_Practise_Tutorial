import cv2
import numpy as np

# Create a white rectangle on a black background
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (50, 50), (250, 250), 255, -1)

# Create a white filled circle on a black background
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 120, 255, -1)

# Perform a bitwise AND operation between the rectangle and the circle
bitwiseAND = cv2.bitwise_and(rectangle, circle)
bitwsieOR=cv2.bitwise_or(rectangle, circle)
bitwiseNOT=cv2.bitwise_not(rectangle)

# Display the images
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Circle", circle)
cv2.imshow("Bitwise AND", bitwiseAND)
cv2.imshow("Bitwise OR", bitwsieOR)
cv2.imshow("Bitwise NOT", bitwiseNOT)




cv2.waitKey(0)
cv2.destroyAllWindows()
