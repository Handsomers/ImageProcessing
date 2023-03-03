import cv2 as cv
from matplotlib import pyplot as plt
#
img1 = cv.imread('image-5-1.png',1)
img2 = cv.imread('image-5-3.png',1)
cv.namedWindow('image1',0)
cv.namedWindow('image2',0)
cv.resizeWindow('image1',200,200)
cv.resizeWindow('image2',200,200)
cv.imshow('image1',img1)
cv.imshow('image2',img2)
#
color = ('b', 'g', 'r')
w1, h1, c1 = img1.shape
w2, h2, c2 = img2.shape
#
for i, col in enumerate(color):
	#
  histr1 = cv.calcHist([img1], [i], None, [256], [0, 256])
  cv.normalize(histr1, histr1, 0, 255, cv.NORM_MINMAX)
  histr2 = cv.calcHist([img2], [i], None, [256], [0, 256])
  cv.normalize(histr2, histr2, 0, 255, cv.NORM_MINMAX)
  #
  difference = cv.compareHist(histr1, histr2, cv.HISTCMP_CHISQR)
  difference = difference/(w1*h1+w2*h2)
  #
  if i == 0:
    plt.subplot(131)
    title = 'B, distance=' + str(round(difference, 2))
    plt.title(title)
    plt.plot(histr1, color = col)
    plt.plot(histr2, color = col)
    plt.xlim([0, 256])
  if i == 1:
    plt.subplot(132)
    title = 'G, distance=' + str(round(difference, 2))
    plt.title(title)
    plt.plot(histr1, color = col)
    plt.plot(histr2, color = col)
    plt.xlim([0, 256])
  if i == 2:
    plt.subplot(133)
    title = 'R, distance=' + str(round(difference, 2))
    plt.title(title)
    plt.plot(histr1, color = col)
    plt.plot(histr2, color = col)
    plt.xlim([0, 256])
plt.show()
