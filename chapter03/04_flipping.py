from __future__ import print_function
import cv2
import numpy as np

# Load image
image_path = "images/zebra.png"
image = cv2.imread(image_path)

cv2.imshow("original image", image)

# Flip horizontally
flippedHorizontally = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flippedHorizontally)

# Flip vertically
flippedVertically = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flippedVertically)

# Flip horizontally then vertically
flippedHV = cv2.flip(image, -1)
cv2.imshow("Fliped H then V", flippedHV)
cv2.waitKey(-1)