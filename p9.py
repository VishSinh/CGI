import cv2
import numpy as np

img = cv2.imread("irelia.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
texture = cv2.filter2D(gray, -1, np.ones((5,5), np.float32)/25)

for name, im in [("Original", img), ("Edges", edges), ("Texture", texture)]:
    cv2.imshow(name, im)

cv2.waitKey(0)
cv2.destroyAllWindows()