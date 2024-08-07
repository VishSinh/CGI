import cv2
import numpy as np

img = cv2.imread('irelia.jpg')
h, w = img.shape[:2]
c = (w//2, h//2)

rot = cv2.getRotationMatrix2D(c, 95, 1)
scl = cv2.getRotationMatrix2D(c, 0, 2)
trans = np.float32([[1, 0, 30], [0, 1, 20]])

img = cv2.warpAffine(img, rot, (w, h))
img = cv2.warpAffine(img, scl, (w, h))
img = cv2.warpAffine(img, trans, (w, h))

cv2.imwrite('Final_image.png', img)