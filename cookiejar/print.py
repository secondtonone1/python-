#-*-coding:utf-8-*-
from urllib import request
from urllib.parse import quote
import urllib
import string
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'


import http.cookiejar
'''
#声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()

#HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)

#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print ('Name = '+item.name)
    print ('Value = '+item.value)

'''

'''
filename = 'cookie.txt'
#定义MozillaCookieJar对象保存cookie，并且cookie关联上filename文件
cookie = http.cookiejar.MozillaCookieJar(filename)
#创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#通过handler构建opener
opener = request.build_opener(handler)
#利用opener请求网页
response = opener.open('http://www.baidu.com')
#保存cookie到文件
cookie.save(ignore_discard = True, ignore_expires = True)
'''

filename = 'cookie.txt'
#创建MozillaCookieJar对象
cookie = http.cookiejar.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load(filename,ignore_discard = True, ignore_expires = True)
#生成cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#创建opener
opener = request.build_opener(handler)
#用opner打开网页
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))








