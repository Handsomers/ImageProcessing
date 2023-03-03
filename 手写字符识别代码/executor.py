#encoding: utf-8
import time
import TencentYoutuyun
import cv2 as cv
import numpy as np
#提供接口必要信息
appid = '10216798'
secret_id = 'AKIDFZifnlK9btzGLDPZ1QTM3Y3RhlcJ78JI'
secret_key = 'yYwDKFyCtQQFsLbgZGm68zgBUbWGtKYe'
userid = 'xxxxxx'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
session_id = ''
#手写字符识别
handwritingocr = youtu.handwritingocr('image-7-3.png', data_type = 0)
length = len(handwritingocr['items'])
print('识别结果如下：')
for i in range(0, length):
  print(handwritingocr['items'][i]['itemstring'].encode('raw_unicode_escape').decode())
image = cv.imread('image-7-3.png')
cv.imshow('hand written recognition', image)
