# Contours can be deñned simply as a curve joining all the continuous points
# (along the boundary), having the same color or intensity
# The contours are a useful tool for shape analysis, object detection, and
# recognition

import cv2

image=cv2.imread('fahad1.jpg',-1) 
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,thresholded=cv2.threshold(image_gray,220,250,cv2.THRESH_BINARY_INV)

contour,_=cv2.findContours(thresholded,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
draw_contour=cv2.drawContours(image,contour,-1,(0,255,0),3)


cv2.imshow("output image", draw_contour)

cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 