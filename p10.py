import cv2

img = cv2.imread("irelia.jpg", 0)
blurred = cv2.GaussianBlur(img, (25, 25), 0)

cv2.imshow("Original", img)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()