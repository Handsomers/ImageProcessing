def bcocr(self, image_path, data_type = 0, seq = ''):

  req_type = 'bcocr'
  headers = self.get_headers(req_type)
  url = self.generate_res_url(req_type, 2)
  data = {
    "app_id": self._appid,
    "session_id": seq,
    #添加logo显示选项
    "options":
  	  {
   	   "logo_detect": True,
  	   "ret_image": "logo"
  	  }
  }

  if len(image_path) == 0:
    return {'httpcode':0, 'errorcode':self.IMAGE_PATH_EMPTY, 'errormsg':'IMAGE_PATH_EMPTY'}

  if data_type == 0:
    filepath = os.path.abspath(image_path)
    if not os.path.exists(filepath):
      return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS'}

    data["image"] = base64.b64encode(open(filepath, 'rb').read()).rstrip().decode('utf-8')
  else:
    data["url"] = image_path

  r = {}
  try:
    r = requests.post(url, headers=headers, data = json.dumps(data))
    if r.status_code != 200:
      return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':''}
    #添加编码格式，防止出现乱码
    r.encoding = 'unicode'
    ret = r.json()
  except Exception as e:
    return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e)}

  return ret
