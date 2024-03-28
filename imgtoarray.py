import cv2
import numpy as np

img = cv2.imread("00001.jpg")
img1 = list(img)
img2 = np.array(img)
print(isinstance(img, np.ndarray))
print(isinstance(img2, np.ndarray))
