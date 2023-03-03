import cv2 as cv
from  matplotlib import pyplot as plt
#读取目标图像
img = cv.imread('image-3-1.png',0)
#读取模板图像
template = cv.imread('image-3-2-2.png',0)
#获取模板图像行列
rows,cols = template.shape
#模板匹配
res = cv.matchTemplate(img,template,1)
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)
#获取匹配区域左上顶点
top_left = min_loc
#获取匹配区域右下顶点
bottom_right = (top_left[0] + rows, top_left[1] + cols)
#获取匹配区域方框
cv.rectangle(img,top_left,bottom_right,0,3)
#用matplotlib里的画图函数框出匹配的区域
plt.subplot(121),plt.imshow(template,cmap='gray')
plt.title('template image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap='gray')
plt.title('matching region'),plt.xticks([]),plt.yticks([])
plt.show()
