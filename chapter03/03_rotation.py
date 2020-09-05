from __future__ import print_function
import cv2
import numpy as np

# Load image
image_path = "images/zebrasmall.png"
image = cv2.imread(image_path)
(h, w) = image.shape[:2]

cv2.imshow("original image", image)

# Define translation matrix
center = (h//2, w/2)
angle = -45
scale = 1.0

rotationMatrix = cv2.getRotationMatrix2D(center, angle, scale)

# Rotate the image
rotatedImage = cv2.warpAffine(image, rotationMatrix, (image.shape[1], image.shape[0]))

cv2.imshow("Rotate image", rotatedImage)
cv2.waitKey(0)
