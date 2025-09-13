import cv2 as cv

img = cv.imread('images/cat.jpg')

# Rotated

# (h, w) = img.shape[:2]
# center = (w // 2, h // 2)

# M = cv.getRotationMatrix2D(center, 45, 2.0)
# rotated = cv.warpAffine(img, M , (w, h))

# cv.imshow('Original Image', img)
# cv.imshow('Rotated by 45 Degrees', rotated)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Flipped

flipped_horizontal = cv.flip(img, 1)
flipped_vertical = cv.flip(img, 0)
flipped_both = cv.flip(img, -1)

cv.imshow('Original Image', img)
cv.imshow('Flipped Horizontally', flipped_horizontal) 
cv.imshow('Flipped Vertically', flipped_vertical)
cv.imshow('Flipped Both', flipped_both)
cv.waitKey(0)
cv.destroyAllWindows()