#-*-coding:utf-8-*-
import re,os,random
import http.cookiejar, urllib.request
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

if __name__ == "__main__":
    req = urllib.request.Request('https://www.aisinei.org/')
    req.add_header('User-Agent',USER_AGENT)
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open(req,timeout=10)
    for item in cookie:
        print(item.name+"="+item.value)


    
