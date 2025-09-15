import cv2 as cv
import numpy as np

img1 = np.zeros((250,250),dtype='uint8')
img2 = np.zeros((250,250),dtype='uint8')

cv.circle(img1,(125,125),100,255,-1)
cv.rectangle(img2,(50,50),(200,200),255,-1)

bitAnd = cv.bitwise_and(img1,img2)
bitOr  cv.bitwise_or(img1,img2)
bitXor = cv.bitwise_xor(img1,img2)
bitNot = cv.bitwise_not(img1)

cv.imshow('Image 1',img1)
cv.imshow('Image 2',img2)

cv.imshow('Bitwise AND',bitAnd)
cv.imshow('Bitwise OR',bitOr)
cv.imshow('Bitwise XOR',bitXor)
cv.imshow('Bitwise NOT',bitNot)

cv.waitKey(0)
cv.destroyAllWindows()