import cv2
import numpy as np

gamma = 1.5
C = 20

img = cv2.imread('PCV-LAB\Intensity_Transformation\image.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

log_transformed = C * np.log(1 + gray.astype(np.float64))
log_img = cv2.normalize(log_transformed, None, 0,255, cv2.NORM_MINMAX)
log_img = np.uint8(log_img)

result = cv2.hconcat([gray, log_img])

cv2.imshow('Log Transformation', result)

cv2.imwrite('log_transformed_image.jpg', log_img)

cv2.waitKey(0)
cv2.destroyAllWindows()