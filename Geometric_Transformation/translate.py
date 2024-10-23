import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"PCV-LAB\Geometric_Transformation\image.jpg")

rows, cols = image.shape[:2]

M = np.float32([[1,0,100], [0,1,50]])

translate = cv2.warpAffine(image, M, (cols, rows))

cv2.imshow('img', translate)
cv2.waitKey(0)
cv2.destroyAllWindows()