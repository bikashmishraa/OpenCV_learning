import cv2 as cv

img = cv.imread('images/cat_large.jpg')

resize_img = cv.resize(img,(400,400))

cv.imshow('Original Image', img)
cv.imshow('Resized Image', resize_img)
cv.waitKey(0)