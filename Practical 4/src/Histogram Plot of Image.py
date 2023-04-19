import cv2
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style('darkgrid')
colors = ["#ffbe0b", "#fb5607", "#ff006e", "#8338ec", "#3a86ff"]
rgb = ["#118ab2", "#06d6a0", "#ef476f"]

# reading image from data/ folder using opencv
lena_image = cv2.imread('../data/lena.png', 1)
img = cv2.imread('../data/lena.png', 0)
# cv2.imshow("Lena Image", lena_image)

# plt.figure(figsize=(20, 10))
# # for i, col in enumerate(['blue', 'green', 'red']):
# #     histogram = cv2.calcHist([lena_image], [i], None, [256], [0, 256])
# #     plt.subplot(1, 3, i + 1)
# #     plt.title(col)
# #     plt.plot(histogram, color=rgb[i])
#
# histogram = cv2.calcHist([lena_image], [0], None, [256], [0, 255])
# histogram_bw = cv2.calcHist([lena_image_bw], [0], None, [256], [0, 256])
#
# plt.figure(figsize=(20, 10))
# plt.subplot(221)
# plt.title('Image Histogram')
# plt.xlabel('bins')
# plt.ylabel('No. of Pixels')
# plt.hist(histogram, color=colors[0])
#
# plt.subplot(222)
# plt.title('Image Plot')
# plt.xlabel('bins')
# plt.ylabel('No. of Pixels')
# plt.plot(histogram, color=colors[1])
#
# plt.subplot(223)
# plt.title('Image Histogram B/W')
# plt.xlabel('bins')
# plt.ylabel('No. of Pixels')
# plt.hist(histogram_bw, color=colors[3])
#
# plt.subplot(224)
# plt.title('Image Plot B/W')
# plt.xlabel('bins')
# plt.ylabel('No. of Pixels')
# plt.plot(histogram_bw, color=colors[4])
# plt.savefig('../plots/hist_rgb.svg', dpi=350)
# plt.show()

img_eq = cv2.equalizeHist(img)
plt.hist(img_eq.ravel(), 256, [0, 256], color=colors[2])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
