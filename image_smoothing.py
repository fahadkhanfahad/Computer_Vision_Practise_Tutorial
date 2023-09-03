
import cv2
import numpy as np

image=cv2.imread('fahad1.jpg',-1) 

blur=cv2.GaussianBlur(image,(5,5),8)

cv2.imshow("blur  image",blur)

cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 