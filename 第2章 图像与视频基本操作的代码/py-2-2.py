import numpy as np
import cv2 as cv

#图像的读取
image1 = cv.imread('image-2-1.jpg',1)
image2 = cv.imread('image-2-2.jpg',1)

#图像的叠加
new_image = cv.addWeighted(image1,0.7,image2,0.3,0)

#图像的显示
cv.imshow('The first image',image1)
cv.imshow('The second image', image2)
cv.imshow('Final image', new_image)

cv.waitKey(0)
cv.destroyAllWindows()
