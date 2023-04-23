import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

image = cv2.imread("../data/cameraman.jpg", 0)

kernel_3x3 = np.array([
    [0.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 0.0],
])
kernel_3x3 = kernel_3x3 / (np.sum(kernel_3x3) if np.sum(kernel_3x3) != 0 else 1)

kernel_5x5 = np.array([
    [0.0, 0.0, -1.0, 0.0, 0.0],
    [0.0, -1.0, -2.0, -1.0, 0.0],
    [-1.0, -2.0, 16.0, -2.0, -1.0],
    [0.0, -1.0, -2.0, -1.0, 0.0],
    [0.0, 0.0, -1.0, 0.0, 0.0],
])

kernel_5x5 = kernel_5x5 / (np.sum(kernel_5x5) if np.sum(kernel_5x5) != 0 else 1)

kernel_5x5_2 = np.array([
    [-1.0, -1.0, -1.0, -1.0, -1.0],
    [-1.0, 1.0, 2.0, 1.0, -1.0],
    [-1.0, 2.0, 4.0, 2.0, -1.0],
    [-1.0, 1.0, 2.0, 1.0, -1.0],
    [-1.0, -1.0, -1.0, -1.0, -1.0],
])

kernel_5x5_2 = kernel_5x5_2 / (np.sum(kernel_5x5_2) if np.sum(kernel_5x5_2) != 0 else 1)

filtered_image_3x3 = cv2.filter2D(image, -1, kernel_3x3)
filtered_image_5x5 = cv2.filter2D(image, -1, kernel_5x5)
filtered_image_5x5_2 = cv2.filter2D(image, -1, kernel_5x5_2)

# cv2.imshow("Original", image)
# cv2.imshow("Filtered 3x3", filtered_image_3x3)
# cv2.imshow("Filtered 5x5", filtered_image_5x5)
# cv2.imshow("Filtered 5x5_2", filtered_image_5x5_2)

# saving the images

cv2.imwrite("../data/filtered_image_3x3.jpg", filtered_image_3x3)
cv2.imwrite("../data/filtered_image_5x5.jpg", filtered_image_5x5)
cv2.imwrite("../data/filtered_image_5x5_2.jpg", filtered_image_5x5_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
