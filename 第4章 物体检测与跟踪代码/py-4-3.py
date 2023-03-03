import numpy as np
import cv2 as cv
#读取视频
cap = cv.VideoCapture('video-4-1.mp4')
ret, frame = cap.read()
#初始化跟踪窗口
x, y, w, h = 350, 150, 50, 50
track_window = (x, y, w, h)
#初始化感兴趣区域，并转化为统计直方图
roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
#设置跟踪窗口移动范围
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
#统计图像直方图信息
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
#直方图归一化
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
#设置迭代条件
term_crit = (cv.TERM_CRITERIA_EPS|cv.TERM_CRITERIA_COUNT, 10, 1)
#循环跟踪目标
while True:
  ret, frame = cap.read()
  if ret == True:
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #直方图反向投影
    dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    #使用meanshift方法跟踪目标新位置
    ret, track_window = cv.meanShift(dst, track_window, term_crit)
    #绘制出新目标位置
    x, y, w, h = track_window
    img2 = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 4)
    rows, cols, _channels = map(int, img2.shape)
    print(x, y, w, h, rows, cols)
    #跟踪目标离开视频区域，恢复窗口初始值
    if (y+h)>0.95*rows:
      x, y, w, h = 350, 150, 50, 50
      track_window = (x, y, w, h)
    #显示图像
    cv.imshow('object tracking', img)
    #按键退出
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
      break
