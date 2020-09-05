from __future__ import print_function
import cv2
import numpy as np

# create a new canvas
canvas = np.zeros((200, 200, 3), dtype="uint8")
start = (10, 10)
end = (100, 100)
color = (0, 0, 255)
thickness = 5 # change thickness into -1 will make rectangle solid

cv2.rectangle(canvas, start, end, color, thickness)
cv2.imwrite("rectangle_canvas.jpg", canvas)
cv2.imshow("rectangle_canvas.jpg", canvas)
cv2.waitKey(0)