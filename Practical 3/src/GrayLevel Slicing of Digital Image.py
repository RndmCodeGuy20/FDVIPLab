import cv2
import numpy as np

bw_image = cv2.imread("../data/cameraman.jpg", 0)
cv2.imshow("Cameraman BW", bw_image)

for i in range(bw_image.shape[0]):
    for j in range(bw_image.shape[1]):
        if 100 < bw_image[i][j] < 200:
            bw_image[i][j] = 0

cv2.imwrite("../data/gl.png", bw_image)

bw_image = cv2.imread("../data/cameraman.jpg", 0)
# cv2.imshow("Cameraman BW", bw_image)

for i in range(bw_image.shape[0]):
    for j in range(bw_image.shape[1]):
        if 100 < bw_image[i][j] < 200:
            bw_image[i][j] = 210

cv2.imshow("Grey Level Sliced BW WB", bw_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
