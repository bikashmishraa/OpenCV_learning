import cv2 as cv

image = cv.imread('../images/cat.jpg',cv.IMREAD_GRAYSCALE)
edges = cv.Canny(image,50,200)
cv.imshow('Original Image',image)
cv.imshow('Canny Edges',edges)
cv.waitKey(0) 
cv.destroyAllWindows()