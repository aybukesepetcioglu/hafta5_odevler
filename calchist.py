import cv2
from matplotlib import pyplot as plt

def kendi_calc_hist(kanal):
    histogram = [0] * 256
    
    for satir in kanal:
        for piksel in satir:
            histogram[piksel] += 1
            
    return histogram

img = cv2.imread('images3.jpg')
b, g, r = cv2.split(img)

b_hist = kendi_calc_hist(b)
g_hist = kendi_calc_hist(g)
r_hist = kendi_calc_hist(r)

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(b_hist, color='blue')
plt.title('Mavi Kanal Histogrami (Kendi Fonksiyonumuz)')

plt.subplot(3, 1, 2)
plt.plot(g_hist, color='green')
plt.title('Yesil Kanal Histogrami (Kendi Fonksiyonumuz)')

plt.subplot(3, 1, 3)
plt.plot(r_hist, color='red')
plt.title('Kirmizi Kanal Histogrami (Kendi Fonksiyonumuz)')

plt.tight_layout()
plt.show()