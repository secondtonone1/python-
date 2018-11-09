#-*-coding:utf-8-*-
import requests
import re
import time
from lxml import etree
from bs4 import BeautifulSoup
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
        except:
            print('init error!!!')
    def getOverView(self):
        try:
            req = self.m_session.get('https://www.aisinei.org/portal.php',headers=self.m_headers, cookies=self.m_cookiejar, timeout=5)
            classattrs={'class':'bus_vtem'}
            soup = BeautifulSoup(req.content.decode('utf-8'),'lxml')
            buslist = soup.find_all(attrs=classattrs)
            print(len(buslist))  
            time.sleep(1)
            pass
        except:
            print('get over view error')

if __name__ == "__main__":
    asscrapy = AsScrapy()
    asscrapy.getOverView()
    

    
    
    
