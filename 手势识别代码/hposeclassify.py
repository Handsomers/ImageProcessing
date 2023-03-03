#定一个新的识别函数
def hposeclassify(self, image_path, data_type = 0, seq = ''):
  #获取接口相关信息
  req_type = 'classify'
  headers = self.get_headers(req_type)
  url = 'http://api.youtu.qq.com/youtu/handtracking/classify'
  print(url)
  data = {
    'app_id': self._appid,
    'seq': seq
  }
  #判断图片路径是否合法
  if len(image_path) == 0:
    return {'httpcode': 0, 'errorcode': self.IMAGE_PATH_EMPTY, 'errormsg': 'IMAGE_PATH_EMPTY'}
  else:
    data['url'] = image_path
    #初始化返回数据
    r = {}
    #调用优图手势识别API并获取返回结果
    try:
      r = requests.post(url, headers = headers, data = json.dumps(data))
      print(url)
      print(headers)
      print(data)
      if r.status_code != 200:
        return {'httpcode': r.status_code, 'errorcode': '', 'errormsg': ''}
      r.encoding = 'unicode'
      ret = r.json()
    except Exception as e:
      return {'httpcode': 0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e)}
  return ret
