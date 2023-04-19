import cv2
import numpy as np

# reading image from data/ folder using opencv
lena_image = cv2.imread('../data/lena.png', 1)

[h, w, d] = lena_image.shape

cv2.putText(img=lena_image, text=f'Image Specs : {h}x{w}x{d}', org=(0, w - 25), fontFace=cv2.FONT_HERSHEY_DUPLEX,
            color=(0, 255, 0), fontScale=1)
cv2.imshow("Lena Image", lena_image)
# print(lena_image)

# reading image from data/ folder using opencv with flag : 0 -> read grayscale, 1 -> color image
lena_image_gray = cv2.imread('../data/lena.png', cv2.IMREAD_GRAYSCALE)  # 0 can also be used

[h, w] = lena_image_gray.shape

cv2.putText(img=lena_image_gray, text=f'Image Specs : {h}x{w}', org=(0, w - 25), fontFace=cv2.FONT_HERSHEY_DUPLEX,
            color=(0, 255, 0), fontScale=1)
cv2.imshow("Lena Image Gray", lena_image_gray)

# Get shape (h, w, d) of the image that is read
print(f'Height of image : {h}\nWidth of image : {w}\nDepth of image : {d}')

cv2.imwrite('../data/lena_og.png', lena_image)
cv2.imwrite('../data/lena_gray.png', lena_image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
