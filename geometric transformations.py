#translation part

import cv2
import numpy as np

#   -1 means unchanged , 1 mean grayscale , 2 mean coloured 
image=cv2.imread('fahad.jpg',-1)
image=cv2.resize(image,(500,500)) 

# //-------------------TRanslation (moving in x and y direction )
# first acces rows coloumn from image.shape 
# then create constrcution matrix  [ab tx  
#                                 cd  ty]  tx and ty are x and y axix

rows,col,channels=image.shape
Matrix=np.float32([
    [1,0,120],
    [0,1,30]
])

translated=cv2.warpAffine(image,Matrix,(col,rows))
cv2.imshow("output image", translated)

#----------------------ROtation iMgae
angle=45
rotated_image=cv2.getRotationMatrix2D((col/2,rows/2),angle,1)
roataion=cv2.warpAffine(image,rotated_image,(col,rows))





cv2.imshow("Roated image",roataion)

cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 