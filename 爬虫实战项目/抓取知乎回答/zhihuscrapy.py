#-*-coding:utf-8-*-
import requests
import re
import time
import json
from bs4 import BeautifulSoup
import os
import sys
from datetime import datetime
from urllib.parse import urlencode
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
COOKIES = '''_zap=860b3564-8750-4f74-884e-92bbb9889f37; 
d_c0="AJDmouQjGA6PTqTesVKUeMhrpmJrMi3h1tM=|1534918190"; 
__gads=ID=5caca3053cdd5eba:T=1539584288:S=ALNI_Mag94pZSq3q7hiGNXtlhiaxpY-Htw; 
z_c0="2|1:0|10:1542783145|4:z_c0|92:Mi4xSk5RdUFBQUFBQUFBa09haTVDTVlEaVlBQUFCZ0FsVk5xVTdpWEFCVmxDbENMYjlpSm0yVGNLQkRvUEFJT19qVmVR|67a272d0fd938302ee4e51e9229bf03303e6a46a97589be3404f86b68fb96ba4"; 
q_c1=de34732dc90a4c77b370861f34a7a2b1|1544002427000|1534918191000; _xsrf=05918ef9-2c9f-47a0-ac42-b2335305b044; 
__utma=51854390.1155392069.1535089086.1545361056.1545807386.16; __utmc=51854390; 
__utmz=51854390.1545807386.16.16.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/wang-wu-chen-32/activities; 
__utmv=51854390.100-1|2=registration_date=20140113=1^3=entry_date=20140113=1; tst=r; tgw_l7_route=e0a07617c1a38385364125951b19eef8'''

class ZhihuScrapy(object):
    def __init__(self,requrl,indexn):
        self.session_ = requests.Session()
        params = {
                'include':'content',
                'limit':str(indexn),
                'offset':'0',
                'sort_by':'default',
            }
        self.url_ = requrl+'?'+urlencode(params)
        self.cookiejar_ =requests.cookies.RequestsCookieJar()
        self.headers_ = {'User-Agent':USER_AGENT,}
        for item in COOKIES.split(';'):
            name ,value = item.split('=',1)
            name=name.replace(' ','').replace('\r','').replace('\n','')
            value = value.replace(' ','').replace('\r','').replace('\n','')
            self.cookiejar_.set(name,value)
        
        self.path=os.path.dirname(os.path.abspath(__file__))
        now = datetime.now()
        timestr=now.strftime('%Y%m%d')
        self.path=os.path.join( self.path,timestr)
        self.nindex_=0
        if os.path.exists(self.path)==False:
            os.mkdir(self.path)

    def getPicData(self,rspdata):
        try:
            for data in rspdata.get('data'):
                self.nindex_ = self.nindex_+1
                print('正在爬取第%d项'%(self.nindex_))
                indexpath=os.path.join(self.path,str(self.nindex_))
                if os.path.exists(indexpath) == False:
                    os.mkdir(indexpath)
                #print(data.get('content'))
                filepath = os.path.join(indexpath,'userdata.txt')
                with open(filepath,'w') as userfile:
                    idstr=data.get('author').get('id')
                    userfile.write('userid: '+ idstr)
                    userfile.write('\n')
                    userpage=data.get('author').get('url').replace('api/v4/','')
                    userfile.write('userpage: '+ userpage)
                soup=BeautifulSoup(data.get('content'),'lxml')
                for img in soup.find_all('img'):
                    #print(img.get('data-original'))
                    imgaddr = img.get('data-original')
                    if imgaddr is None:
                        continue
                    imgpath=os.path.join(indexpath,imgaddr.split('/')[-1])
                    print('正在爬取%s'%(imgaddr.split('/')[-1]))
                    if os.path.exists(imgpath) == True:
                        print('爬取%s'%(imgaddr.split('/')[-1]))
                        continue
                    imgfiledata=self.session_.get(imgaddr,headers=self.headers_, cookies=self.cookiejar_).content
                    time.sleep(1)
                    with open (imgpath,'wb') as imgfile:
                        imgfile.write(imgfiledata)
                    print('爬取%s'%(imgaddr.split('/')[-1]))
                print('爬取第%d项成功'%(self.nindex_))
        except:
            pass
    def getData(self):
        try:
            while True:
                response=self.session_.get(self.url_,headers=self.headers_, cookies=self.cookiejar_)
                time.sleep(1)
                #print(response.encoding)
                #print(response.text)
                #rspdata = json.loads(response.text)
                rspdata = response.json()
                #print(rspdata)
                self.getPicData(rspdata)
                #可以去掉，我只想爬取前30项
                if self.nindex_ >30:
                    break
                if rspdata.get('paging').get('is_end') == True:
                    break
                self.url_= rspdata.get('paging').get('next')
                if self.url_ is None:
                    break
                
        except:
            print('getData except!!!')


if __name__ == "__main__":
    #zhihu = ZhihuScrapy('https://www.zhihu.com/api/v4/questions/58498720/answers',20)
    #zhihu = ZhihuScrapy('https://www.zhihu.com/api/v4/questions/265767940/answers',20)
    zhihu = ZhihuScrapy('https://www.zhihu.com/api/v4/questions/268409414/answers',20)
    zhihu.getData()
    pass
    

   
    
    
