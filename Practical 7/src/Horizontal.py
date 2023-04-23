import cv2
import numpy as np

img = cv2.imread('../data/lines.png', 0)

# binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

kernel = np.ones((2, 19), np.uint8)

horizontalLines = cv2.erode(img, kernel, iterations=1)
# cv2.imshow('vertical', horizontalLines)

cv2.imwrite('../data/horizontalLines.png', horizontalLines)

cv2.waitKey(0)
cv2.destroyAllWindows()
