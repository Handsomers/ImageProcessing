import numpy as np
import cv2 as cv

#摄像头的调取
cap = cv.VideoCapture('0')
#创建编码器对象
fourcc = cv.VideoWriter_fourcc(*'XVID')
#初始化输出流
out = cv.VideoWriter('video-output-1-1.avi',fourcc,20.0,(640,480))

#循环保存视频的图像帧
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("the video cannot be read")
        break
    frame = cv.flip(frame, 0)
    out.write(frame)
    cv.imshow('video_from_camera',frame)
    if cv.waitKey(1) == ord('q'):
        break

#释放资源
cap.release()
out.release()
cv.destroyAllWindows()
