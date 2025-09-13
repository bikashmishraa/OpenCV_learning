import cv2 as cv

#capture video from file
video = cv.VideoCapture(0)

# while True:
#  ret , frame = video.read()
#  if ret == False:
#      print("No frame to read")
#      break
#  cv.imshow('Video', frame)
 
#  if cv.waitKey(1) & 0xFF == ord('q'):
#     print('Quiting...')
#     break
# video.release()
# cv.destroyAllWindows()

#Saving the video

frame_width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', codec, 20.0, (frame_width, frame_height))


while True:
  success, image = video.read()
  
  if success == False:
      print("No frame to read")
      break
     
  out.write(image)
  cv.imshow('Video', image)
  
  if cv.waitKey(1) & 0xFF == ord('q'):
     print('Quiting...')
     break

out.release()
video.release()
cv.destroyAllWindows()