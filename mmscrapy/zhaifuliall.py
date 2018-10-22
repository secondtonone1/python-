#-*-coding:utf-8-*-
import re,os,random
from urllib import request, parse
from datetime import datetime
from urllib import error

from urllib.parse import quote
import string

import time, threading

import http.client
import configparser  
  
http.client.HTTPConnection._http_vsn = 10  
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
WEBHEAD = 'https://52zfl.vip/'
contents=""

class GetMMPic(object):
    def __init__(self,path):
        #去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip('\\')
        self.path = path
        self.url = 'https://52zfl.vip/index.html'
        self.user_agent = USER_AGENT
    def makedir(self,dirname):
        joinpath = os.path.join(self.path,dirname)
        print(joinpath)
        isExists = os.path.exists(joinpath)
        if isExists:
            print('目录已经存在\n')
            return joinpath
        else:
            os.makedirs(joinpath)
            print('创建成功\n')
            return joinpath

    def setpath(self,path):
        self.path = path
    def seturl(self,url):
        self.url = url
    def getAbstractInfo(self):
        try:
            contenta = requestData(self.url, self.user_agent)
            self.getDetailList(contenta)
        except error.HTTPError as e:
            
            if hasattr(e,'code'):
                print(e.code)
            if hasattr(e,'reason'):
                print(e.reason)
            print('HTTPError!!!')
        except error.URLError as e:
            if hasattr(e,'code'):
                print (e.code)
            if hasattr(e,'reason'):
                print (e.reason)
    
    
    
    

    def getDetailList(self,content):
        filterstr = r'<h3 class="title">.*?<strong>最新发布</strong></h3>(.*?)<aside class="sidebar">'
        filterpattern = re.compile(filterstr,re.S)
        listcontent=re.search(filterpattern,content)
        if(listcontent==None):
            print('filter not found')
            return
        listcontent = listcontent.group(1)     
        patternstr = r'<h2><a target="_blank" href="(.*?)" title="(.*?)">'
        itempattern =re.compile(patternstr , re.S )
        result = re.findall(itempattern, listcontent)
        if not result:
            print('匹配规则不适配..............')
        #print('匹配条目:%s' %(result))
        for item in result:
            workthread(item, self.user_agent,self.path);


def requestData(url, user_agent):
    global contents
    try:
        req = request.Request(url)
        req.add_header('User-Agent', user_agent)
        response = request.urlopen(req,timeout = 8)
		#bytes变为字符串
        contents = response.read().decode('GBK')
    except error.URLError as e:
        if hasattr(e,'code'):
            print (e.code)
        if hasattr(e,'reason'):
            print (e.reason)
    except error.HTTPError as e: 
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
        print('HTTPError!!!')
    except Exception:
        return None
    return contents

def workthread(item, user_agent,path):
    itempage=WEBHEAD+item[0]
    itemdir=item[1]
    itemdir=os.path.join(path,itemdir)
    picname = item[1]
    splitindex=itempage.rfind('/')
    if(splitindex==-1):
        return
    pagehead=itempage[:splitindex+1]
    print('正在爬取%s...........................\n' %(picname))
    if (os.path.exists(itemdir) == False):
        os.makedirs(itemdir)
    content = requestData(itempage,user_agent)
    imagepatternstr=r'<p>.*?<img(.*?)></p>'
    imgsrc=r'src="(.*?)"'
    imagepattern =re.compile(imagepatternstr , re.S )
    imgsrcpattern =re.compile(imgsrc , re.S )
    nextpagestr=r"<li class='next-page'><a href='(.*?)'"
    nextpattern = re.compile(nextpagestr,re.S)
    while content:
        imagelist=re.findall(imagepattern,content)
        if (len(imagelist)==0):
            print('未找到符合格式图片')
            break
        getPicData(imagelist,itemdir,imgsrcpattern)
        searchres=re.search(nextpattern,content)
        if(searchres==None):
            break
        nextpage = pagehead+searchres.group(1)
        content = requestData(nextpage,user_agent)

    print('%s爬取成功...........................\n' %(picname))

def getPicData(imagelist,itemdir,imgsrcpattern):
    for img in imagelist:
        srcdata=re.search(imgsrcpattern,img).group(1)
        if(srcdata==None):
            continue
        srcindex=srcdata.rfind('/')
        if(srcindex==-1):
            continue
        srcname=srcdata[srcindex+1:]
        srcpath=os.path.join(itemdir,srcname)
        if(os.path.exists(srcpath)):
            os.remove(srcpath)
        print('正在爬取%s...........................\n' %(srcname))
        req = request.Request(srcdata)
        req.add_header('User-Agent',USER_AGENT)
        try:
            response = request.urlopen(req,timeout = 10)
            picdata =response.read()
            with open(srcpath,'wb') as file:
                file.write(picdata)
            time.sleep(1)
        except Exception as e:
            print("error code ")
        print('爬取成功%s...........................\n' %(srcname))

        





if __name__ == "__main__":
    #getMMPic = GetMMPic('D:/python/args')
    filepath = os.path.abspath(__file__)
    filedir=os.path.dirname(filepath)
    getMMPic = GetMMPic(filedir)
    now = datetime.now()
    timestr=now.strftime('%Y%m%d')
    todaypath = getMMPic.makedir(timestr)
    if  todaypath:
        config = configparser.ConfigParser()
        configpath=os.path.join(filedir,'config.ini')
        config.read(configpath)
        pages=config.items('page')
        getMMPic.setpath(todaypath)
        for i in pages:
            getMMPic.seturl(i[1])
            getMMPic.getAbstractInfo()
	
