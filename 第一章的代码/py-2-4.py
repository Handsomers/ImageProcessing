import numpy as np
import cv2 as cv

#获取视频文件的内容
cap = cv.VideoCapture('video-2-1.mp4')

#循环读取视频的图像帧，并显示
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("video has ended")
        break
    cv.imshow('video frame',frame)
    if cv.waitKey(1) == ord('q'):
        break

#释放资源
cap.release()
cv.destroyAllWindows()
