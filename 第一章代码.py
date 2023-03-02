#引入numpy和opencv库
import numpy as np
import cv2 as cv

#读取并显示图像
img = cv.imread('image/cup1.jpg', 1)
cv.imshow('image',img)

#保存图像
key = cv.waitKey(0)
if key == 27:	#27在ASCI码中代表ESC
  cv.destroyAllWindows()
elif key == ord('s'):
  cv.imwrite('image/cup1.jpg',img)
cv.destroyAllWindows()