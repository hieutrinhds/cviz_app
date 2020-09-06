import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read an image and convert it to grayscale
image = cv2.imread("images/nature.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)

# Calculate histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot histogram
plot.figure()
plot.title("Grayscale Histogram")
plot.xlabel("Bins")
plot.ylabel("Number of pixels")
plot.plot(hist)
plot.show()
cv2.waitKey(0)