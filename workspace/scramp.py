# -*- coding: utf-8 -*-

from urllib import request
from urllib import error
from urllib import parse

from http import cookiejar

import re


if __name__ == '__main__':
    #登陆地址
    login_url = 'http://www.lesmao.cc/member.php?mod=logging&action=login&referer='    
    #User-Agent信息                   
    user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    #Headers信息
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    
    #登陆Form_Data信息
    Login_Data = {}
    Login_Data['formhash'] = '5ea0f6e4'
    Login_Data['referer'] = 'http://www.lesmao.cc/./'
    Login_Data['loginfield'] = 'username'         
    Login_Data['username'] = 'secondtonone1'      
    Login_Data['password'] = '18301152001'
    Login_Data['loginsubmit'] = 'true'
    Login_Data['questionid'] = '0'
    Login_Data['answer'] = ''
            
    #使用urlencode方法转换标准格式
    logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
    #声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(cookie_support)
    #创建Request对象
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head)

    #面向对象地址
    date_url = 'http://www.lesmao.cc/home.php?mod=space&do=notice&view=system'

    req2 = request.Request(url=date_url,  headers=head)
    try:
        #使用自己创建的opener的open方法
        response1 = opener.open(req1)
        #print(response1.read().decode('utf-8'))
        print('.................................')
        response2 = opener.open(req2)
        html = response2.read().decode('utf-8') 
        #打印查询结果
        print(html)

    except error.URLError as e:
        if hasattr(e, 'code'):
            print("URLError:%d" % e.code)
        if hasattr(e, 'reason'):
            print("URLError:%s" % e.reason)
    except error.HTTPError as e:
        if hasattr(e, 'code'):
            print("URLError:%d" % e.code)
        if hasattr(e, 'reason'):
            print("URLError:%s" % e.reason)
    except Exception as e:
        print('Exception is : ', e)
    	

