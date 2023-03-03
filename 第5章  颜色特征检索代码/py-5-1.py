import cv2 as cv
from matplotlib import pyplot as plt
#
img1 = cv.imread('image-5-1.png',1)
img2 = cv.imread('image-5-3.png',1)
cv.namedWindow('image1',0)
cv.namedWindow('image2',0)
cv.resizeWindow('image1',300,300)
cv.resizeWindow('image2',300,300)
cv.imshow('image1',img1)
cv.imshow('image2',img2)
#
color = ('b','g','r')
#
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
#
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
