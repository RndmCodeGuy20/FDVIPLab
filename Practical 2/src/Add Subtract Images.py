import cv2
import numpy as np

img_lena = cv2.imread('../data/lena.png', 0)
img_star = cv2.imread('../data/star.png', 0)
#
# cv2.imshow("star", img_star)
# cv2.imshow("black", img_lena)
#
# # img_star = cv2.resize(img_star, (512, 512))
# # pixel addition and pixel subtraction
# cv2.imshow("addition", img_star + img_lena)
# cv2.imshow("subtraction", img_star - img_lena)
#
# # image superimposition
img_add = cv2.add(img_star, img_lena)
img_sub = cv2.subtract(img_star, img_lena)
#
cv2.imwrite("../data/add.png", img_add)
cv2.imwrite("../data/sub.png", img_sub)
#
# image multiplication and division
img_mul = cv2.multiply(img_star, img_lena)
img_div = cv2.divide(img_star, img_lena)
#
cv2.imwrite("../data/mul.png", img_mul)
cv2.imwrite("../data/div.png", img_div)
#
# image scaling
img_cameraman = cv2.imread('../data/cameraman.jpg', 0)
#
img_mul = cv2.multiply(img_cameraman, 2)
img_div = cv2.multiply(img_cameraman, 0.5)

cv2.imwrite('../data/scale2.png', img_mul)
cv2.imwrite('../data/scale05.png', img_div)
#
# cv2.imshow("scaled image mul", img_mul)
# cv2.imshow("scaled image div", img_div)

# logical scaling
img1 = cv2.imread('../data/img1.png')
img2 = cv2.imread('../data/img2.png')
#
# cv2.imshow("original 1", img1)
# cv2.imshow("original 2", img2)
#
img_and = cv2.bitwise_and(img1, img2)
img_or = cv2.bitwise_or(img1, img2)
img_xor = cv2.bitwise_xor(img1, img2)
img_not = cv2.bitwise_not(img1)

cv2.imwrite("../data/and.png", img_and)
cv2.imwrite("../data/or.png", img_or)
cv2.imwrite("../data/xor.png", img_xor)
cv2.imwrite("../data/not.png", img_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
