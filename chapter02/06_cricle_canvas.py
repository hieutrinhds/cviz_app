from __future__ import print_function
import cv2
import numpy as np

# create a new canvas
canvas = np.zeros((200, 200, 3), dtype="uint8")
center = (100, 100)
radius = 50
color = (0, 0, 255)
thickness = -1 # change thickness into -1 will make rectangle solid

cv2.circle(canvas, center, radius, color, thickness)
cv2.imwrite("mycircle.jpg", canvas)
cv2.imshow("mycircle.jpg", canvas)
cv2.waitKey(0)