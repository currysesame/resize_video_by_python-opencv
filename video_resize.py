# resize the video by python-opencv based on windows

# ref:
# https://medium.com/@yanweiliu/python%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E7%AD%86%E8%A8%98-%E4%B8%89-open-cv%E6%93%8D%E4%BD%9C%E7%AD%86%E8%A8%98-1eab0b95339c
import cv2
video_name = 'your_file_name'
source = video_name + '.mp4'
cap = cv2.VideoCapture(source)# 設定擷取影像的尺寸大小
width = 400
height = 760
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)# 使用 XVID 編碼
fourcc = cv2.VideoWriter_fourcc(*'XVID')#影片常見編碼格式：DIVX、XVID、MJPG、X264、WMV1、WMV2# 建立 VideoWriter 物件，輸出影片至 output.avi
# FPS 值為 20.0，解析度為 640x360
output_name = video_name + 'resized.avi'
out = cv2.VideoWriter(output_name, fourcc, 24.0, (width, height))
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    # 寫入影格
    frame = cv2.resize(frame, (width, height))
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break# 釋放所有資源
cap.release()
out.release()
cv2.destroyAllWindows()