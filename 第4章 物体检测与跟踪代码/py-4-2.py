import cv2 as cv
#初始化高斯背景建模变量
backSub = cv.createBackgroundSubtractorMOG2()
#读取视频
capture = cv.VideoCapture('video-4-1.mp4')
if not capture.isOpened:
  print('Video cannot be opened')
  exit(0)
#高斯建模法求背景与运动物体
while True:
  ret, frame = capture.read()
  if frame is None:
    break
  fgMask = backSub.apply(frame)
  rows, cols, _channels = map(int, frame.shape)
  framesrc = cv.pyrDown(frame, dstsize = (cols//2, rows//2))
  cv.imshow('Frame', framesrc)
  rows, cols, _channel = map(int, frame.shape)
  fgMasksrc = cv.pyrDown(fgMask, dstsize = (cols//2, rows//2))
  cv.imshow('FG Mask', fgMasksrc)
  #按键退出
  keyboard = cv.waitKey(30)
  if keyboard == 'q' or keyboard == 27:
    break
