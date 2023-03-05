import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca citra pertama
img1 = cv2.imread('image_di1.jpeg')

# membaca citra kedua
img2 = cv2.imread('image_di2.jpeg')

# menghitung perbedaan antara kedua citra
diff = cv2.absdiff(img1, img2)

# menampilkan citra perbedaan
plt.subplot(1, 2, 1),plt.imshow(img1,cmap = 'gray')
plt.title('Citra Pertama'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2),plt.imshow(img2,cmap = 'gray')
plt.title('Citra Kedua'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.imshow('Citra Perbedaan',diff)

# membuat histogram dari citra perbedaan
hist,bins = np.histogram(diff.flatten(),256,[0,256])

# menampilkan histogram
plt.hist(diff.flatten(),256,[0,256], color = 'brown')
plt.xlim([0,256])
plt.show()

# menunggu input keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()
