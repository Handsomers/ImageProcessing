#encoding: utf-8
import time
import TencentYoutuyun
import cv2 as cv
#提供接口必要信息
appid = '10216798'
secret_id = 'AKIDFZifnlK9btzGLDPZ1QTM3Y3RhlcJ78JI'
secret_key = 'yYwDKFyCtQQFsLbgZGm68zgBUbWGtKYe'
userid = 'xxxxxx'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
session_id = ''
#速算题目识别
arithmeticocr = youtu.arithmeticocr('image-7-4.png', data_type = 0)
print('返回数据：', arithmeticocr)
print('题目：', arithmeticocr['items'][0]['itemstring'])
print('答案：', arithmeticocr['items'][0]['answer'])
image = cv.imread('image-7-4.png', 1)
cv.namedWindow('arithmetic recognition',0)
cv.resizeWindow('arithmetic recognition',600,200)
cv.imshow('arithmetic recognition', image)
