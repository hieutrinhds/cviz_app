import cv2
import numpy as np

# Load an image
image = cv2.imread("images/sudoku.jpg")
cv2.imshow("Original Image", image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.bilateralFilter(image, 5, 50, 50)
cv2.imshow("Blurred image", image)

# Canny function for edge detection
canny = cv2.Canny(image, 50, 170) # passing minimum and maximum threshold values
cv2.imshow("Canny Edges", canny)

cv2.waitKey()
