import cv2
import numpy as np

image = cv2.imread('../data/tiger.jpg', 0)

edges = cv2.Canny(image, 100, 150)

cv2.imwrite('../data/edges.png', edges)
