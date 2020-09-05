from __future__ import print_function
import cv2
import numpy as np

# Load image
image_path = "images/zebrasmall.png"
image = cv2.imread(image_path)

cv2.imshow("original image", image)

# Crop the image to get only the face of the zebra
croppedImage = image[0:150, 0:250]
cv2.imshow("Cropped Image", croppedImage)
cv2.waitKey(0)