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
#输入图像以获取识别结果
img = cv.imread('image-7-1.png')
cv.imshow('target image',img)
ret = youtu.imagetag('image-7-1.png', data_type = 0, seq = '')
text = ''
for i in range(len(ret['tags'])):
    ret_type = ret['tags'][i]['tag_name'].encode('raw_unicode_escape').decode()
    text = 'tag_name = '+ ret_type + '  tag_confidence = ' + str(ret['tags'][i]['tag_confidence'])
    print(text)
