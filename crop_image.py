
import cv2
import numpy as np

image=cv2.imread('fahad1.jpg',-1) 

#just grabbing the ROI *region of interest)
croped_portion=image[100:300,200:400]

cv2.imshow("cropped image",croped_portion)

cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 