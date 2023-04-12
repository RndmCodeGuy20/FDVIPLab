import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/tiger.jpg', 0)

assert img is not None, 'file cannot be null'

edges = cv2.Canny(img, 100, 200)

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('og img')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title('edge img')
plt.xticks([])
plt.yticks([])
plt.show()
