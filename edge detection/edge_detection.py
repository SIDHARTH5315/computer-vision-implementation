import cv2

img = cv2.imread('/Users/hq/Data/Projects/Computer-vision-projects/Computer-vision-short-projects/LLT1_ComputerVision/Project1_EdgeDetection/input.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 2)

cv2.imshow('Edges', edges)
cv2.imshow('Contours', img)
cv2.imwrite('edges.jpg', edges)
cv2.imwrite('contours.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()