#引入numpy和opencv库
import numpy as np
import cv2 as cv

#读取并显示图像
img = cv.imread('image-2-1.jpg', 1)
cv.imshow('image',img)

#保存图像
key = cv.waitKey(0)
if key == 27:	#27在ASCI码中代表ESC
  cv.destroyAllWindows()
elif key == ord('s'):
  cv.imwrite('image-2-1_copy.jpg',img)
cv.destroyAllWindows()
