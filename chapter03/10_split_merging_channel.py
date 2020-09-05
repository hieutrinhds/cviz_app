import cv2
import numpy as np

# Load the image
natureImage = cv2.imread("images/nature.jpg")

# Split the image into component colors
(b, g, r) = cv2.split(natureImage)

# Show the blue image
cv2.imshow("Blue Image", b)

# Show the red image
cv2.imshow("Red Image", r)

# Show the greem image
cv2.imshow("Green Image", g)

# Merged channels
merged = cv2.merge([b, g, r])
cv2.imshow("Merged image", merged)

cv2.waitKey(0)