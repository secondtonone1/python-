#-*-coding:utf-8-*-
import requests
import re
import time
from lxml import etree
from bs4 import BeautifulSoup
import os
import sys
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
COOKIES = '__cfduid=d78f862232687ba4aae00f617c0fd1ca81537854419; bg5D_2132_saltkey=jh7xllgK; bg5D_2132_lastvisit=1540536781; bg5D_2132_auth=479fTpQgthFjwwD6V1Xq8ky8wI2dzxJkPeJHEZyv3eqJqdTQOQWE74ttW1HchIUZpgsyN5Y9r1jtby9AwfRN1R89; bg5D_2132_lastcheckfeed=7469%7C1541145866; bg5D_2132_ulastactivity=2bbfoTOtWWimnqaXyLbTv%2Buq4ens5zcXIiEAhobA%2FsWLyvpXVM9d; bg5D_2132_sid=wF3g17; Hm_lvt_b8d70b1e8d60fba1e9c8bd5d6b035f4c=1540540375,1540955353,1541145834,1541562930; Hm_lpvt_b8d70b1e8d60fba1e9c8bd5d6b035f4c=1541562973; bg5D_2132_lastact=1541562986%09home.php%09spacecp'
class AsScrapy(object):
    def __init__(self,pages=1):
        try:
            self.m_session = requests.Session()
            self.m_headers = {'User-Agent':USER_AGENT,
                        #'referer':'https://www.aisinei.org/',
                        }
           
            self.m_cookiejar = requests.cookies.RequestsCookieJar()
            for cookie in COOKIES.split(';'):
                key,value = cookie.split('=',1)
                self.m_cookiejar.set(key,value)
            self.m_path =os.path.dirname(os.path.abspath(__file__))  
        except:
            print('init error!!!')
    def getOverView(self):
        try:
            req = self.m_session.get('https://www.aisinei.org/portal.php',headers=self.m_headers, cookies=self.m_cookiejar, timeout=5)
            classattrs={'class':'bus_vtem'}
            soup = BeautifulSoup(req.content.decode('utf-8'),'lxml')
            buslist = soup.find_all(attrs=classattrs)
            #print(len(buslist))
            time.sleep(1)
            for item in buslist:
                if(item.a.attrs['title'] ==  "紧急通知！紧急通知！紧急通知！"):
                    continue
                print(item.a.attrs['title'])
                print(item.a.attrs['href'])
                #print(self.m_path)
                dirname = os.path.join(self.m_path, item.a.attrs['title']).split('[',1)[0].replace(' ','').replace('/','')
                print(dirname)
                if(os.path.exists(dirname)==False):
                    os.makedirs(dirname)
                albumreq = self.m_session.get(item.a.attrs['href'],headers=self.m_headers,cookies=self.m_cookiejar,timeout=5).content.decode('utf-8')
                #print(albumreq)
                bsoup=BeautifulSoup(albumreq,'lxml')
                album_regexp = re.compile(r"只看大图",re.S)
                #emailid_regexp = re.compile("\w+@\w+\.\w+",re.S)　
                findres = bsoup.find(text=album_regexp)
                print(findres.parent)
                albumaddr = findres.parent['href']
                print(albumaddr)
                time.sleep(1)
                albumhtml=self.m_session.get(albumaddr,timeout=5).content.decode('utf-8')
                #print(type(findres))
                #print(findres)
                self.getAlbumPic(dirname,albumhtml)
                time.sleep(1)
                break; 
            time.sleep(1)
            pass
        except IOError:
            print('IOError')
        except:
            print('get over view error')
    def getAlbumPic(self,albumdir,albumhtml):
        filename=os.path.join(albumdir,'album.html')
        with open(filename, 'w',encoding='utf-8') as file:
            file.write(albumhtml)
        #print(albumhtml)
        #imagelis_reg = re.compile(r'''<script type="text/javascript" reload="1">.*?imglist['url'] =.*?[(.*?)];''', re.S)
        #imagematch=imagelis_reg.findall(albumhtml)
        #print(imagematch)
        pass

if __name__ == "__main__":
    asscrapy = AsScrapy()
    asscrapy.getOverView()
    

    
    
    
