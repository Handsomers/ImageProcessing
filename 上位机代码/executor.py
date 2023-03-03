from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import scrolledtext
import os
import numpy as np
import cv2 as cv
import time
import TencentYoutuyun
#提供接口必要信息
appid = '10216798'
secret_id = 'AKIDFZifnlK9btzGLDPZ1QTM3Y3RhlcJ78JI'
secret_key = 'yYwDKFyCtQQFsLbgZGm68zgBUbWGtKYe'
userid = 'xxxxxx'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
session_id = ''
#定义需要用到的函数
#定义点击函数
def clicked():
  file_roots = filedialog.askopenfilenames(initialdir = os.path.dirname(__file__))
  global img_fp
  img_fp = file_roots[0]
  print(img_fp)
  img = cv.imread(img_fp, 1)
  cv.imshow('image', img)
  logText = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '已选择' + img_fp + '图像\n'
  scr.insert(END, logText)
  #默认显示
  if com.current() == 0:
    logText = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '未选择接口\n'
    scr.insert(END, logText)
  #图像内容识别功能
  if com.current() == 1:
    ret = youtu.imagetag(img_fp, data_type = 0, seq = '')
    logText = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '调用接口返回' + str(ret) + '\n'
    scr.insert(END, logText)
    text = ''
    for i in range(len(ret['tags'])):
        ret_type = ret['tags'][i]['tag_name'].encode('raw_unicode_escape').decode()
        text += ' ' + 'tag_name = '+ ret_type + '  tag_confidence = ' + str(ret['tags'][i]['tag_confidence'])
    logText = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '图像识别结果是：' + text + '\n'
    scr.insert(END, logText)
  #手写字体识别功能
  if com.current() == 2:
    handwritingocr = youtu.handwritingocr(img_fp, data_type = 0)
    length = len(handwritingocr['items'])
    text = ''
    for i in range(0, length):
      text += ' ' + handwritingocr['items'][i]['itemstring'].encode('raw_unicode_escape').decode()
    logText = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '调用接口返回：' + str(handwritingocr) + '\n'
    scr.insert(END, logText)
    logText = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '手写字符识别结果是：' + text + '\n'
    scr.insert(END, logText)
#定义功能下拉卡函数
def func(event):
  logText = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '已选择第' + str(com.current()) + com.get() + '功能\n'
  scr.insert(INSERT, logText)
#定义清除函数
def clearlog():
  scr.delete(1.0, END)
#初始化用户UI窗口
#初始化窗口
window = Tk()
window.title('Youtu SDK桌面测试软件')
window.geometry('600x300')
#初始化下拉控件
select_api = StringVar()
com = ttk.Combobox(window, textvariable = select_api)
com.grid(column = 1, row = 1)
#设置下拉控件数据
com['value'] = ('请选择优图SDK AI功能', '图像内容识别', '通用手写文字识别')
com.current(0)
#下拉控件绑带函数
com.bind('<<ComboboxSelected>>', func)
#初始化清除按钮
btn_clear = Button(window, text = '清空日志', command = clearlog)
btn_clear.grid(column = 2, row = 1)
#初始化图像识别按钮
btn_select = Button(window, text = '选择需要识别的图像', command = clicked)
btn_select.grid(column = 3, row = 1)
#初始化可滚动的文本控件
scr = scrolledtext.ScrolledText(window, width = 60, height = 9, font = ('Times', 12))
scr.place(x = 50, y = 50)
logText = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '软件启动\n'
scr.insert(END, logText)
#显示用户UI窗口
window.mainloop()
