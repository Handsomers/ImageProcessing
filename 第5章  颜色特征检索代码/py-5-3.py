import cv2 as cv
from matplotlib import pyplot as plt
import sys
#
def getHistDistance(file1, file2):
  img1 = cv.imread(file1, 1)
  img2 = cv.imread(file2, 1)
  color = ('b', 'g', 'r')
  w1, h1, c1 = img1.shape
  w2, h2, c2 = img2.shape
  totalDistance = 0
  for i, col in enumerate(color):
    histr1 = cv.calcHist([img1], [i], None, [256], [0, 256])
    histr2 = cv.calcHist([img2], [i], None, [256], [0, 256])
    cv.normalize(histr1, histr1, 0, 255, cv.NORM_MINMAX)
    cv.normalize(histr2, histr2, 0, 255, cv.NORM_MINMAX)
    difference = cv.compareHist(histr1, histr2, cv.HISTCMP_CHISQR)
    difference = abs(difference)/(w1*h1+w2*h2)
    totalDistance = totalDistance + difference
  totalDistance = totalDistance/3
  return totalDistance
#
fileList = ['image-5-1.png', 'image-5-2.png', 'image-5-3.png', 'image-5-4.png', 'image-5-5.png', 'image-5-6.png', 'image-5-7.png']
#
fileForCompare = 'image-5-1.png'
fileDistanceList = [0,0,0,0,0,0,0]
#
for i, file in enumerate(fileList):
  distance = getHistDistance(fileForCompare, file)
  fileDistanceList[i] = distance
  print(round(distance, 2))
print(fileDistanceList)
#
for i, distance in enumerate(fileDistanceList):
  min_idx = i
  for j in range(i+1, len(fileDistanceList)):
    if fileDistanceList[min_idx] > fileDistanceList[j]:
      min_idx = j
    fileDistanceList[i], fileDistanceList[min_idx] = fileDistanceList[min_idx], fileDistanceList[i]
    fileList[i], fileList[min_idx] = fileList[min_idx], fileList[i]
#
print('排序后的数组：')
total = len(fileList)
#
imgShow = cv.imread(fileForCompare, 1)
b, g, r = cv.split(imgShow)
imgShow2 = cv.merge([r, g, b])
plt.subplot(1, total+1, 1)
title = 'Input Image'
plt.title(title)
plt.imshow(imgShow2)
plt.axis('off')
plt.tight_layout()
#
for i, file in enumerate(fileList):
  print('%s' %fileList[i])
  print('%s' %fileDistanceList[i])
  imgShow1 = cv.imread(file, 1)
  b, g, r = cv.split(imgShow1)
  imgShow2 = cv.merge([r, g, b])
  plt.subplot(1, total+1, i+2)
  title = 'distance=' + str(round(fileDistanceList[i], 2))
  plt.title(title)
  plt.imshow(imgShow2)
  plt.axis('off')
  plt.tight_layout()
plt.show()
