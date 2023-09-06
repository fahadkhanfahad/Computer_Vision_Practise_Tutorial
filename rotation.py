import cv2

image=cv2.imread('download.jpg')


roatated=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Orignal window", image)
cv2.imshow("Roatated Image",roatated)


cv2.waitKey(0)
cv2.destroyAllWindows()
