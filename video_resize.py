# resize the video by python-opencv based on windows

# ref:
# https://medium.com/@yanweiliu/python%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E7%AD%86%E8%A8%98-%E4%B8%89-open-cv%E6%93%8D%E4%BD%9C%E7%AD%86%E8%A8%98-1eab0b95339c
import cv2
video_name = 'your_file_name'
source = video_name + '.mp4'
cap = cv2.VideoCapture(source)# set the frame shape
width = 400
height = 760
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)# use XVID codec
fourcc = cv2.VideoWriter_fourcc(*'XVID') # some codecs: DIVX、XVID、MJPG、X264、WMV1、WMV2
# fps is 24, resize the video to the size 400x760
output_name = video_name + 'resized.avi'
out = cv2.VideoWriter(output_name, fourcc, 24.0, (width, height))
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    # write the frame with the specific size
    frame = cv2.resize(frame, (width, height))
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break# release the resource
cap.release()
out.release()
cv2.destroyAllWindows()