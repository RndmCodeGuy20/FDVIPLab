import cv2
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style('darkgrid')
colors = ["#ffbe0b", "#fb5607", "#ff006e", "#8338ec", "#3a86ff"]
rgb = ["#118ab2", "#06d6a0", "#ef476f"]

# reading image from data/ folder using opencv
img = cv2.imread('../data/cameraman.jpg', 1)
# lena_image = cv2.imread('../data/lena.png', 1)
lena_image_bw = cv2.imread('../data/cameraman.jpg', 0)
# cv2.imshow("Lena Image", lena_image)

lena_image_2 = cv2.convertScaleAbs(lena_image_bw, alpha=1.5, beta=50)
plt.title("Brightness & contrast")
# plt.imshow(lena_image_2)

# img_stretch = cv2.convertScaleAbs(img, alpha=1.5, beta=50)
# plt.hist(img_stretch.ravel(), 256, [0, 256])
# plt.show()
# plt.show()
plt.show()

# histogram stretching
