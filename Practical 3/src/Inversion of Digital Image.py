import cv2

bw_image = cv2.imread("../data/cameraman.jpg")
cv2.imshow("Cameraman BW", bw_image)

inv_image = bw_image.max() - bw_image
cv2.imshow("Cameraman BW Inverted", inv_image)

cv2.imwrite('../data/neg.png', inv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
