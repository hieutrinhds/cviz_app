from __future__ import print_function
import cv2
import numpy as np

# Load image
image_path = "images/zebra.png"
image = cv2.imread(image_path)

cv2.imshow("original image", image)

# Get the shape which returns height, width, and channels asn a tuple. Calculate the aspect ratio
(h, w) = image.shape[:2]
aspect = w/h

# Resize by half the original image
# Pixel values must be integer
new_height = int(0.5*h)
new_width = int(new_height*aspect)

# New image dimension as a tuple
dimension = (new_height, new_width)
resizedImage = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Image", resizedImage)

# Resize using x and y factors
resizedWithFactor = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Resized with factors", resizedWithFactor)
cv2.waitKey(0)

