import cv2

img = cv2.imread('/Users/hq/Data/Projects/Computer-vision-projects/Computer-vision-short-projects/LLT1_ComputerVision/Project4_Blurring/input.jpg')

avg = cv2.blur(img, (35,35))
gaussian = cv2.GaussianBlur(img, (35,35), 0)
median = cv2.medianBlur(img, 35)
bilateral = cv2.bilateralFilter(img, 35, 150, 150)

cv2.imshow('Average Blur', avg)
cv2.imshow('Gaussian Blur', gaussian)
cv2.imshow('Median Blur', median)
cv2.imshow('Bilateral Blur', bilateral)

cv2.imwrite('output_strong_blur.jpg', gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()