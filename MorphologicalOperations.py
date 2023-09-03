# The fundamental idea of erosion is just like how it sounds, it erodes (eats
# away or eliminates) the boundaries of foreground objects 

#dilation the opposite of erosion. It increases the white region in the image or
# size of the foreground object increases. So essentially dilation expands the
# boundary of Objects

import cv2
import numpy as np

eimage=cv2.imread('for_erosion.png',-1) 
dimage=cv2.imread('for_dilation.png',-1) 


kernel=np.ones((7,7),np.uint8)

eroded=cv2.erode(eimage, kernel,3)
dilated=cv2.dilate(dimage,kernel,3)


cv2.imshow("orignal image for eroded",eimage)
cv2.imshow("output image - eroded", eroded)


cv2.imshow("orignal image for Dilation",dimage)
cv2.imshow("output image - dilated", dilated)

cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 