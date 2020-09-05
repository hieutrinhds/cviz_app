import cv2
import numpy as np

# Load the park image
parkImage = cv2.imread("images/park.jpg")
cv2.imshow("Original Image", parkImage)

# Gaussian blurring with 3x3 kernel and 0 for std
GaussianFilterd = cv2.GaussianBlur(parkImage, (3, 3), 0)
cv2.imshow("Gaussian Blurred Image", GaussianFilterd)

cv2.waitKey(0)