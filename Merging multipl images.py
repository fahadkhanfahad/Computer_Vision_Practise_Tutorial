#note for merging the size should be same 
import cv2

image1=cv2.imread('download.jpg')
image2=cv2.imread('bleed.png')

resize1=cv2.resize(image1,(400,400))
resize2=cv2.resize(image1,(400,400))

merging=cv2.add(resize1,resize2)

cv2.imshow("Merging the pictures", merging)



cv2.waitKey(0)
cv2.destroyAllWindows()
