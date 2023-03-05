import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca citra
img = cv2.imread('image_abstrak.jpg',0)

# menampilkan citra
cv2.imshow('Citra Asli', img)

# membuat histogram
hist,bins = np.histogram(img.flatten(),256,[0,256])

# menampilkan histogram
plt.hist(img.flatten(),256,[0,256], color = 'red')
plt.xlim([0,256])
plt.title('Histogram')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')
plt.show()

# menunggu input keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()
