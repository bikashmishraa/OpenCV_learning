import cv2 as cv

image = cv.imread('images/cat.jpg')

grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

userinput = input(f"Enter 'v' to view and 's' to save the grayscale image: ")

if userinput.lower() =='v':
  cv.imshow('Grayscale Image', grayscale)
  cv.waitKey(0) 
  cv.destroyAllWindows()
elif userinput.lower() =='s':
  cv.imwrite('images/cat_grayscale.jpg', grayscale)
  print("Grayscale image saved as 'cat_grayscale.jpg'")
else:
  print("Invalid input. Please enter 'v' to view or 's' to save the image.")
  