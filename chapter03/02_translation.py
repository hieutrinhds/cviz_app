from __future__ import print_function
import cv2
import numpy as np

# Load image
image_path = "images/zebra.png"
image = cv2.imread(image_path)

cv2.imshow("original image", image)

# Define a translation matrix
translationMatrix = np.float32([[1, 0, 50],
                                [0, 1, 20]])

# Move the image
moveImage = cv2.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))

cv2.imshow("Move image", moveImage)
cv2.waitKey(0)