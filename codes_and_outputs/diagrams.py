import cv2 as cv

img = cv.imread('images/cat.jpg')
print(f"Image shape: {img.shape}") 

# Display the image
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Draw a line on the image
pt1=(200,200)
pt2=(400,400)
color=(0,255,0)
thickness=5

line = cv.line(img,pt1,pt2,color,thickness)
cv.imshow('Line', line)
cv.waitKey(0)
cv.destroyAllWindows()


#draw a rectangle on the image
rect = cv.rectangle(img,pt1,pt2,color,thickness)
cv.imshow('Rectangle', rect)
cv.waitKey(0)
cv.destroyAllWindows()

#draw a circle on the image
center=(200,200)
radius=100
circle = cv.circle(img,center,radius,color,thickness)
cv.imshow('Circle', circle)
cv.waitKey(0)
cv.destroyAllWindows() 

#write a text
text = "Hello OpenCV"
org = (400,50)
font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
fontscale = 1
color = (255,0,0)
thickn=2
img_text = cv.putText(img,text,org,font,fontscale,color,thickn)
cv.imshow('Text', img_text)
cv.waitKey(0) 
cv.destroyAllWindows()