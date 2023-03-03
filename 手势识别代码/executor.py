#coding: utf-8
import time
import urllib.request as request
import numpy as np
import cv2 as cv
import TencentYoutuyun
#提供接口必要信息
appid = '10216798'
secret_id = 'AKIDFZifnlK9btzGLDPZ1QTM3Y3RhlcJ78JI'
secret_key = 'yYwDKFyCtQQFsLbgZGm68zgBUbWGtKYe'
userid = 'xxxxxx'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
session_id = ''
#调用优图手势识别API，以获取识别结果
image_address = 'https://img1.jiemian.com/101/original/20141119/141638675074705000_a700xH.jpg'
ret = youtu.hposeclassify(image_address, data_type = 0, seq = '')
print(ret)
print(ret['items'][0]['label'])
#读取手势并显示
response = request.urlopen(image_address)
img_array = np.array(bytearray(response.read()), dtype=np.uint8)
img = cv.imdecode(img_array, -1)
x = ret['items'][0]['x']
y = ret['items'][0]['y']
h = ret['items'][0]['height']
w = ret['items'][0]['width']
draw_0 = cv.rectangle(img, (x, y), (w, h), (255, 0, 0), 2)
cv.imshow('Gesture', draw_0)
