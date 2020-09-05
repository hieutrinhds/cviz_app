from __future__ import print_function
import cv2
import numpy as np

# Load image
image1_path = "images/cat1.png"
image2_path = "images/cat2.png"
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# Resize the two images to make them of the same dimensions.
resizedImage1 = cv2.resize(image1,(int(500*image1.shape[1]/image1.shape[0]), 500),interpolation=cv2.INTER_AREA)
resizedImage2 = cv2.resize(image2,(int(500*image2.shape[1]/image2.shape[0]), 500),interpolation=cv2.INTER_AREA)

cv2.imshow("Cat1", resizedImage1)
cv2.imshow("Cat2", resizedImage2)

# Subtract image 1 from 2
cv2.imshow("Diff Cat1 and Cat2", cv2.subtract(resizedImage2, resizedImage1))
cv2.waitKey(0)

# Subtract image 2 from 1
cv2.imshow("Diff Cat2 and Cat1", cv2.subtract(resizedImage1, resizedImage2))
cv2.waitKey(0)

# A constant subtraction
subtractedimage3 = resizedImage1 - 50
cv2.imshow("Constant Subtracted from the image", subtractedimage3)
cv2.waitKey(0)