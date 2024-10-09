import numpy as np
import cv2

img = cv2.imread(r'C:\Users\kenneth\OneDrive\Desktop\PCV\PCV-LAB\Hisrogram_Equalization\image.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
angle = 45

h, w = img.shape[:2]
M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
rotated_img = cv2.warpAffine(img, M, (w,h))
cv2.imshow('Original image', img)
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()