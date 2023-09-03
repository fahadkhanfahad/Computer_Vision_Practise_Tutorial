import cv2
import numpy as np

#   -1 means unchanged , 1 mean grayscale , 2 mean coloured 
image=cv2.imread('fahad.jpg',-1) 
print(image)
image.shape