#-*-coding:utf-8-*-
# server.py
# 从wsgiref模块导入:  
from wsgiref.simple_server import make_server
from helloworld import application
#创建服务器
httpd = make_server('',8000, application)
print('Serving HTTP on port')
# 开始监听HTTP请求:
httpd.serve_forever()