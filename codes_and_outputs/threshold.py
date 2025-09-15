import cv2 as cv

image = cv.imread('../images/cats.jpg',cv.IMREAD_GRAYSCALE)

ret, thres_img = cv.threshold(image,120,255,cv.THRESH_BINARY)

cv.imshow('Original Image',image)
cv.imshow('Threshold Image',thres_img)
cv.waitKey(0)
cv.destroyAllWindows()