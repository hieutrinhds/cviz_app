import cv2
import numpy as np

# Load an image
image = cv2.imread("images/scanned_doc.png")
# Convert the image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original GrayScale Receipt", image)

# Binarize the image using thresholding
(T, binarizedImage) = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)
cv2.imshow("Binarized  Receipt", binarizedImage)

# Binarize the image using inverse thresholding
(T, inversebinarizedImage) = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Inverse Binarized  Receipt", inversebinarizedImage)
cv2.waitKey(0)
