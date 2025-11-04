import cv2
import numpy as np

img = cv2.imread('/Users/hq/Data/Projects/Computer-vision-projects/Computer-vision-short-projects/LLT1_ComputerVision/Project2_ColorFiltering/input.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define color range (example: blue)
lower = np.array([90, 50, 50])
upper = np.array([130, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Original', img)
cv2.imshow('Masked Output', res)
cv2.imwrite('masked_output.jpg', res)
cv2.waitKey(0)
cv2.destroyAllWindows()