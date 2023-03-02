import cv2 as cv
from matplotlib import pyplot as plt

#读取两个图像
img1 = cv.imread('ameng1.jpg',1)
img2 = cv.imread('ameng2.jpg',1)
cv.imshow('image1',img1)
cv.imshow('image2',img2)
#彩色图像的三通道
color = ('b','g','r')
#计算画出图像1的直方图
for i, col in enumerate(color):
  histr = cv.calcHist([img1], [i], None, [256], [0, 256])
  if i == 0:
    plt.subplot(231)
    plt.title('B')
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
  if i == 1:
    plt.subplot(232)
    plt.title('G')
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
  if i == 2:
    plt.subplot(233)
    plt.title('R')
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
#计算画出图像2的直方图
for i, col in enumerate(color):
  histr = cv.calcHist([img2], [i], None, [256], [0, 256])
  if i == 0:
    plt.subplot(234)
    plt.title('B')
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
  if i == 1:
    plt.subplot(235)
    plt.title('G')
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
  if i == 2:
    plt.subplot(236)
    plt.title('R')
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
plt.show()