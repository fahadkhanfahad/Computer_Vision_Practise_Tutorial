
import cv2
import numpy as np

image=cv2.imread('fahad1.jpg',-1) 
#converting image to other formats like grayscale ,RGB 
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


croped_gray=gray[100:300,200:400]
cv2.imshow("Cropped Gray Scale Mode Image",croped_gray)

cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 