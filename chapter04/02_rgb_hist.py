import cv2
import numpy as np
from matplotlib import pyplot as plot

# Read an image and convert it to grayscale
image = cv2.imread("images/nature.jpg")

cv2.imshow("Original Image", image)

colors = ("blue", "green", "red")
# Calculate histogram
for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [32], [0, 256])
    # Plot histogram graph
    plot.plot(hist, color=color)

plot.title("RGB Color Histogram")
plot.xlabel("Bins")
plot.ylabel("Number of Pixels")
plot.show()
cv2.waitKey(0)