import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#读取图像
img1 = cv.imread('image-3-1.png', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('image-3-2-1.png',cv.IMREAD_GRAYSCALE)
#初始化orb检测器
orb = cv.ORB_create()
#使用orb检测器寻找并计算特征点描述符
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
#创建BFMatcher对象
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck = True)
#角点特征符比较与匹配
matches = bf.match(des1, des2)
#按距离排序
matches = sorted(matches, key = lambda x:x.distance)
for i in range(1,10):
  print("第", i, "特征点之间的距离：", matches[i].distance, "\n")
#绘制前10个匹配
img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags = cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3), plt.show()
