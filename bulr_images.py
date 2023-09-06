import cv2

image1 = cv2.imread('girl.png')

# Apply different blurring techniques
image_blur = cv2.blur(image1,(7, 7))
image_gaussian_blur = cv2.GaussianBlur(image1,(7, 7), 9)
image_median_blur = cv2.medianBlur(image1, 7)

# Resize the images for better visualization
resize1 = cv2.resize(image1, (300, 400))
resize2 = cv2.resize(image_blur, (300, 400))
resize3 = cv2.resize(image_gaussian_blur, (300, 400))
resize4 = cv2.resize(image_median_blur, (300, 400))

# Concatenate the images horizontally for comparison
horizontal_concat = cv2.hconcat([resize1, resize2, resize3, resize4])

# Show the concatenated image
cv2.imshow("Different Blurring Techniques", horizontal_concat)

cv2.waitKey(0)
cv2.destroyAllWindows()
