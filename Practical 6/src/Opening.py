import cv2
import numpy as np

img = cv2.imread('../../Practical 5/data/H.png', 0)

kernel = np.ones((5, 5), np.uint8)

binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

invert = cv2.bitwise_not(binr)
for i in range(0, 26, 5):
    opening = cv2.morphologyEx(binr, cv2.MORPH_OPEN, kernel, iterations=i)
    cv2.imwrite(f"../data/opening_{i}.png", opening)
    # cv2.imshow(f"after opening image iter={i}", opening)
    # cv2.waitKey(100)

binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

invert = cv2.bitwise_not(binr)
for i in range(0, 26, 5):
    closing = cv2.morphologyEx(binr, cv2.MORPH_CLOSE, kernel, iterations=i)
    cv2.imwrite(f"../data/closing_{i}.png", closing)

cv2.destroyAllWindows()
