import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images3.jpg')

b, g, r = cv2.split(img)

plt.figure(figsize=(10, 8))
# Mavi Kanal Histogramı
plt.subplot(3, 1, 1)
plt.hist(b.ravel(), 256, [0, 256], color='blue')
plt.title('Mavi Kanal Histogrami')

# Yeşil Kanal Histogramı
plt.subplot(3, 1, 2)
plt.hist(g.ravel(), 256, [0, 256], color='green')
plt.title('Yesil Kanal Histogrami')

# Kırmızı Kanal Histogramı
plt.subplot(3, 1, 3)
plt.hist(r.ravel(), 256, [0, 256], color='red')
plt.title('Kirmizi Kanal Histogrami')

plt.tight_layout()
plt.show()