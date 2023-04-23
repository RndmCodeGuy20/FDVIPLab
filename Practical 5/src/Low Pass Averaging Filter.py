import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

kernel_5x5 = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
])

kernel_3x3 = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
])

kernel_5x5 = kernel_5x5 / sum(kernel_5x5)
kernel_3x3 = kernel_3x3 / sum(kernel_3x3)

image = cv2.imread("../data/mri_2.png", 0)
filtered_image_5x5 = cv2.filter2D(image, -1, kernel_5x5)
filtered_image_3x3 = cv2.filter2D(image, -1, kernel_3x3)

# cv2.imshow("Original", image)
# cv2.imshow("Filtered 5x5", filtered_image_5x5)
# cv2.imshow("Filtered 3x3", filtered_image_3x3)

# save images
cv2.imwrite("../data/mri_2_filtered_5x5.png", filtered_image_5x5)
cv2.imwrite("../data/mri_2_filtered_3x3.png", filtered_image_3x3)

cv2.waitKey(0)
cv2.destroyAllWindows()
