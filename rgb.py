import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images3.jpg')

gray_opencv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def kendi_gri_yapan_fonksiyon(resim):

    b = resim[:, :, 0].astype(np.float32)
    g = resim[:, :, 1].astype(np.float32)
    r = resim[:, :, 2].astype(np.float32)
    
    gri = 0.299 * r + 0.587 * g + 0.114 * b
    
    return gri.astype(np.uint8)

gray_kendi = kendi_gri_yapan_fonksiyon(img)

fark = np.abs(gray_opencv.astype(np.int32) - gray_kendi.astype(np.int32))
toplam_hata = np.sum(fark)

print(f"Eşleşen piksellerin mutlak farklarının toplamı (Hata Değeri): {toplam_hata}")

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(gray_opencv, cmap='gray')
plt.title('OpenCV cvtColor')

plt.subplot(1, 3, 2)
plt.imshow(gray_kendi, cmap='gray')
plt.title('Kendi Fonksiyonumuz')

plt.subplot(1, 3, 3)
plt.imshow(fark, cmap='hot')
plt.title('Piksel Farkları')

plt.tight_layout()
plt.show()