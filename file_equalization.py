import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca citra
img = cv2.imread('image_maudy.jpg',0)

# membuat histogram equalization
equ = cv2.equalizeHist(img)

# menampilkan citra asli dan setelah histogram equalization
plt.subplot(1, 2, 1),plt.imshow(img,cmap = 'gray')
plt.title('Citra (Asli)'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2),plt.imshow(equ,cmap = 'gray')
plt.title('Citra (Histogram Equalization)'), plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(2, 2, 1)
# membuat histogram dari citra asli
hist,bins = np.histogram(img.flatten(),256,[0,256])
plt.hist(img.flatten(),256,[0,256], color = 'blue')
plt.xlim([0,256])
plt.title('Histogram (Citra Asli)')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

plt.subplot(2, 2, 4)
# membuat histogram dari citra histogram equalization
hist,bins = np.histogram(equ.flatten(),256,[0,256])
plt.hist(img.flatten(),256,[0,256], color = 'gray')
plt.xlim([0,256])
plt.title('Histogram (Citra Histogram Equalization)')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

#Menampilkan kedua histogram
plt.show()

# menunggu input keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()
