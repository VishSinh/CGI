import cv2, matplotlib.pyplot as plt

img = cv2.imread('irelia.jpg')
h, w = img.shape[:2]
quads = [
    img[:h//2, :w//2], 
    img[:h//2, w//2:], 
    img[h//2:, :w//2], 
    img[h//2:, w//2:]]
    
for i in range(2):
    plt.figure(figsize=(10, 5))
    for j in range(2):
        plt.subplot(1, 2, j+1)
        plt.imshow(quads[i*2+j])
        plt.title(str(i*2+j+1))
        plt.axis("off")

plt.show()