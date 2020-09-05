from __future__ import print_function
import cv2

# image path
image_path = "images/marsrover.png"
# Read or load image from its path
image = cv2.imread(image_path)

# Access pixel at (0, 0) location
(b, g, r) = image[0, 0]
print("Blue, Green, and Red values at (0,0): ", format((b, g, r)))

# Manipulate pixels and show modified image
image[0:100, 0:100] = (255, 255, 0) # from 0 to 100 along y-axis, 0 to 100 along x-axis, assign new values (255, 255, 0)
cv2.imshow("Modified Image", image)
cv2.waitKey(0) # wait for use press any key for program to exit.


