import cv2
import numpy as np

bw_image = cv2.imread("../data/cameraman.jpg")
cv2.imshow("BW", bw_image)

c = 255 / (np.log(1 + bw_image.max()))
log_image = c * np.log(bw_image + 1)
cv2.imshow("Log BW", np.array(log_image, dtype=np.uint8))

cv2.imwrite('../data/log.png', np.array(log_image, dtype=np.uint8))

cv2.waitKey()
cv2.destroyAllWindows()
