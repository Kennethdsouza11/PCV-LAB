import cv2

img = cv2.imread('PCV-LAB\Basic_Operations\image.jpg')

cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()