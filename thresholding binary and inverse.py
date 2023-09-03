
import cv2
import numpy as np

image=cv2.imread('fahad1.jpg',-1) 

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,bthresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)   #any pixel about 150 shoul be converted to white
_,bthreshinverse=cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)


cv2.imshow("Binary Threshold Mode",bthresh)
cv2.imshow("Inverse Binary Threshold Mode",bthreshinverse)


cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 