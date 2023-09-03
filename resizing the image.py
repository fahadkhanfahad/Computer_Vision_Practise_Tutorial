
import cv2
import numpy as np

#   -1 means unchanged , 1 mean grayscale , 2 mean coloured 
image=cv2.imread('fahad.jpg',-1) 
print(image)
# You can use cv2.resize() function to resize an image. You have 2 ways of
# resizing the image, either by passing in the new width & height values or by
# passing in percentages of those values using fx and fy params


resized_image=cv2.resize(image,(500,500))

cv2.imshow("resized image", resized_image)

# to keep the ascpect ratio 
# we first get the width,heigh from image.shape
# then with new width/old width 
# and multiply that with height 

height,width,shape=image.shape
#suppose my new width is 600
ratio=600/width
new_height=int(height*ratio)
aspect_ratio=cv2.resize(image,(600,new_height))

cv2.imshow("with maininting aspect ratio",aspect_ratio)


cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 