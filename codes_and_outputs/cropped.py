import cv2 as cv

img = cv.imread('images/cat.jpg')

crop_img = img[100:900,200:900]
cv.imshow('Original Image', img)
cv.imshow('Cropped Image', crop_img)
cv.waitKey(0)
cv.destroyAllWindows()