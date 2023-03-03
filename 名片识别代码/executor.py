#encoding: utf-8
import time
import TencentYoutuyun
import cv2 as cv
import os
import base64
import sys
#提供接口必要信息
appid = '10216798'
secret_id = 'AKIDFZifnlK9btzGLDPZ1QTM3Y3RhlcJ78JI'
secret_key = 'yYwDKFyCtQQFsLbgZGm68zgBUbWGtKYe'
userid = 'xxxxxx'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
session_id = ''
#名片识别
retbcocr = youtu.bcocr('image-7-5.png',data_type = 0)
length = len(retbcocr['items'])
print('识别结果如下：')
for i in range(0, length-1):
  print(retbcocr['items'][i]['item'], '', retbcocr['items'][i]['itemstring'])
#获取公司LOGO图像并解码
strs = retbcocr['image']
img = base64.b64decode(strs)
#保存公司LOGO图像
file = open('logo.jpg', 'wb')
file.write(img)
file.close()
#显示公司LOGO图像
img2 = cv.imread('logo.jpg', 1)
cv.namedWindow('logo',0)
cv.resizeWindow('logo',150,150)
cv.imshow('logo', img2)
