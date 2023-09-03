
import cv2
import numpy as np

#   -1 means unchanged , 1 mean grayscale , 2 mean coloured 
image=cv2.imread('fahad.jpg',-1) 
print(image)


# Step 1: Use cv2.imshow() to show images.
# cv2.imshow(Window_Name, img)

cv2.imshow("output image", image)

# checking properties
print(format(image.dtype)) 
print(format(image.ndim))
cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 