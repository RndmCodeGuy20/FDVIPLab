import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/lena.png', 0)

assert img is not None, 'file cannot be null'

edges = cv2.Canny(img, 100, 150)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, maxLineGap=50)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)

cv2.imshow('line edges', edges)
cv2.imshow('line detected', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
