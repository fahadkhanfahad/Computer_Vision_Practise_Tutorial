
import cv2
import numpy as np

#   -1 means unchanged , 1 mean grayscale , 2 mean coloured 
image=cv2.imread('fahad.jpg',-1) 
print(image)

#accessin the pixel value have to right the location points
print(image[300,300]) #that means what's value of pixel will at this point we will get 3 channes B,G,R

image[300,300]=0 # modifyibg single pixel

#modifyibg ROI

image_copy=image.copy()
image_copy[400:800,200:600] = 0  #we are giving x and y axies rane values





# Step 1: Use cv2.imshow() to show images.
# cv2.imshow(Window_Name, img)
cv2.imshow("orignal Image", image)
cv2.imshow("chanaged ROI Image", image_copy)

cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 