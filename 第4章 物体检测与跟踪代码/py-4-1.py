import cv2 as cv
#读取视频
capture = cv.VideoCapture('video-4-1.mp4')
if not capture.isOpened:
  print('视频无法读取')
  exit(0)
#获取视频背景的灰度图像
ret, background_color = capture.read()
background_gray = cv.cvtColor(background_color, cv.COLOR_BGR2GRAY)
#加权平均法求背景图像与运动物体
while True:
  #获取视频的图像帧
  ret, frame = capture.read()
  if frame is None:
    break
  #获取图像帧的灰度图像
  frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  #加权平均法求背景图像
  background_gray = cv.addWeighted(background_gray, 0.98, frame_gray, 0.02, 0)
  rows, cols, _channels = map(int, frame.shape)
  background_realtime = cv.pyrDown(background_gray, dstsize = (cols//2, rows//2))
  cv.imshow('background', background_realtime)
  #获取当前运动物体
  fgMask = frame_gray - background_gray
  fgMask_realtime = cv.pyrDown(fgMask, dstsize = (cols//2, rows//2))
  cv.imshow('Frame', fgMask_realtime)
  #按键退出
  keyboard = cv.waitKey(30)
  if keyboard == ord('q') or keyboard == 27:
    break
