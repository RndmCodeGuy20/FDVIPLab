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

image = cv2.imread("../data/mri_2.png", 0)

# median filter
filtered_image_5x5 = cv2.medianBlur(image, 5)
filtered_image_3x3 = np.zeros(image.shape, dtype=np.uint8)

for i in range(image.shape[0] - 1):
    for j in range(image.shape[1] - 1):
        temp = [image[i - 1, j - 1], image[i - 1, j], image[i - 1, j + 1], image[i, j - 1], image[i, j],
                image[i, j + 1], image[i + 1, j - 1], image[i + 1, j], image[i + 1, j + 1]]

        temp.sort()
        filtered_image_3x3[i, j] = temp[4]

# cv2.imshow("Original", image)
# cv2.imshow("Filtered 5x5", filtered_image_5x5)
# cv2.imshow("Filtered 3x3", filtered_image_3x3)

cv2.imwrite("../data/mri_2_filtered_5x5_med.png", filtered_image_5x5)

cv2.waitKey(0)
cv2.destroyAllWindows()
