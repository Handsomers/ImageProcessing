import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#目标图像的读取
img1 = cv.imread('image-3-1.png',0)
img2 = cv.imread('image-3-2-2.png',0)
#初始化ORB特征点检测器
orb = cv.ORB_create()
#使用ORB检测器获取特征点
kp = orb.detect(img1,None)
#描述并表示特征点
kp, des = orb.compute(img1, kp)
#画出特征点在目标图像中的位置
img3 = cv.drawKeypoints(img1, kp, None, color=(255, 0, 0), flags = 0)
plt.subplot(211), plt.imshow(img3)
#
orb = cv.ORB_create()
kp = orb.detect(img2, None)
kp, des = orb.compute(img2, kp)
img3 = cv.drawKeypoints(img2, kp, None, color=(255, 0, 0), flags = 0)
plt.subplot(212), plt.imshow(img3),plt.show()
