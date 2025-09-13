import cv2 as cv

img = cv.imread('images/cat_large.jpg')
#************ Reading and saving the image**********

# if img is None:
#  print('Could not open or find the image.')
#  exit(0)
# else:
#  cv.imshow('Cat', img)
#  cv.waitKey(0)
#  cv.destroyAllWindows()
#  print('Image loaded successfully.')
 
# cv.imwrite('images/cat_large_copy.png',img)

# ************ finding the shape of video - shape has 3 attributes h,w,c**********

# print('Shape of the image:', img.shape)

# h, w, c = img.shape
# print(f"height : {h}, width : {w}, channels : {c}")


# *** convert BGR to Grayscale ****

grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', grayscale)
cv.waitKey(0)

cv.imwrite('images/cat_large_grayscale.jpg',grayscale)
cv.destroyAllWindows()