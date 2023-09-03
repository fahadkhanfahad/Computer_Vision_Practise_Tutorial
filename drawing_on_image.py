
import cv2
import numpy as np

image=cv2.imread('fahad1.jpg',-1) 
#drawing cirle
cirle=cv2.circle(image,(350,100),100,4)   #
#drawing line
line=cv2.line(image,(100,200),(300,400),3)
#drawaing rectangle
rectangle=cv2.rectangle(image,(100,200),(300,400),3)
#writing text
text=cv2.putText(image,"Fahad khan",(100,200),cv2.FONT_HERSHEY_COMPLEX,3,(100,200),3)

cv2.imshow("circle on image", cirle)
cv2.imshow("line  on image", line)
cv2.imshow("rectangle on image", rectangle)
cv2.imshow("text on image", text)

cv2.waitKey(0)  #that means it will infinte time untill key pressed
cv2.destroyAllWindows() 