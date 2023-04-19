import cv2
import numpy as np

img = cv2.imread('../data/cameraman.jpg', 0)

img_bit = np.zeros(img.shape, dtype=np.uint8)
for i in range(8):
    img_bit = img_bit + ((img >> i) & 1) * (2 ** i)
    cv2.imwrite(f'../data/bitplane-{i}.png', img_bit)

cv2.waitKey(0)
cv2.destroyAllWindows()
