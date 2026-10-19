import cv2
import numpy as np
img_bgr = cv2.imread('images3.jpg')

rgb_opencv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

def kendi_bgr2rgb_fonksiyonumuz(resim):

    b = resim[:, :, 0]
    g = resim[:, :, 1]
    r = resim[:, :, 2]
    
    rgb_resim = np.dstack((r, g, b))
    return rgb_resim

rgb_kendi = kendi_bgr2rgb_fonksiyonumuz(img_bgr)

fark = np.abs(rgb_opencv.astype(np.int32) - rgb_kendi.astype(np.int32))
toplam_hata = np.sum(fark)

print(f"Hazır OpenCV ile Kendi Fonksiyonumuz Arasındaki Hata Değeri: {toplam_hata}")