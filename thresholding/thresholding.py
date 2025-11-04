import cv2

img = cv2.imread('/Users/hq/Data/Projects/Computer-vision-projects/Computer-vision-short-projects/LLT1_ComputerVision/Project3_Thresholding/input.jpg', 0)
_, simple = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Simple Threshold', simple)
cv2.imshow('Adaptive Threshold', adaptive)
cv2.imwrite('output.jpg', adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()