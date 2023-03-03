import numpy as np
import cv2 as cv

img1 = cv.imread('image-2-2.jpg',1)
img2 = cv.imread('image-2-3.jpg',1)

#获取img2的图像大小，并获取img1感兴趣的区域
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]
cv.imshow('img1 interest region',roi)

#图像感兴趣区域叠加
dst = cv.addWeighted(roi, 0, img2, 1, 0)
img1[0:rows,0:cols] = dst

cv.imshow('Final image', img1)
cv.waitKey(0)
cv.destroyAllWindows()
