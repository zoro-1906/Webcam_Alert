# This code creates a 3D NumPy array "a", which represents an image with pixel values,
# and then writes this array to an image file (img.png) using OpenCV's cv2.imwrite() function.

import numpy
import cv2

a = numpy.array(
[[[255, 0, 0],
  [255, 255, 255],
  [255, 255, 255],
  [187, 41, 160]],

 [[255, 255, 255],
  [255, 255, 255],
  [255, 255, 255],
  [255, 255, 255]],

 [[255, 255, 255],
  [0, 0, 0],
  [47, 255, 173],
  [255, 255, 255]]]
)

cv2.imwrite('img.png', a)