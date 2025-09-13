import cv2 as cv

# image = cv.imread('../images/cat.jpg')

#Gaussian Blur Image

# blurred = cv.GaussianBlur(image,(15,15),10)

# cv.imshow('Original Image', image)
# cv.imshow('Blurred Image', blurred)
# cv.waitKey(0)
# cv.destroyAllWindows()

#Median Blur Image

img = cv.imread('../images/flower_dust.png')
median = cv.medianBlur(img,15)

cv.imshow('Original Image', img)
cv.imshow('Median Blurred Image', median) 
cv.waitKey(0)
cv.destroyAllWindows()