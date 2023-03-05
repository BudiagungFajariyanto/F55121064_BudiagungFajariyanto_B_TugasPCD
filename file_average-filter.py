import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('image_dami.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define kernel size for average filter
kernel_size = (5, 5)

# Apply average filter to image
blur = cv2.blur(gray, kernel_size)

# Plot original and filtered image
plt.subplot(121), plt.imshow(gray, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur, cmap='gray')
plt.title('Average Filter'), plt.xticks([]), plt.yticks([])
plt.show()

# membuat histogram
hist,bins = np.histogram(img.flatten(),256,[0,256])

# menampilkan histogram
plt.hist(img.flatten(),256,[0,256], color = 'orange')
plt.xlim([0,256])
plt.title('Histogram')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')
plt.show()

# menunggu input keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()