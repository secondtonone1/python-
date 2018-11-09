#-*-coding:utf-8-*-
import requests
import re
import time
from lxml import etree

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
COOKIES = r'__cfduid=d78f862232687ba4aae00f617c0fd1ca81537854419; bg5D_2132_saltkey=jh7xllgK; bg5D_2132_lastvisit=1540536781; bg5D_2132_auth=479fTpQgthFjwwD6V1Xq8ky8wI2dzxJkPeJHEZyv3eqJqdTQOQWE74ttW1HchIUZpgsyN5Y9r1jtby9AwfRN1R89; bg5D_2132_lastcheckfeed=7469%7C1541145866; bg5D_2132_st_p=7469%7C1541642338%7Cda8e3f530a609251e7b04bfc94edecec; bg5D_2132_visitedfid=52; bg5D_2132_viewid=tid_14993; bg5D_2132_ulastactivity=caf0lAnOBNI8j%2FNwQJnPGXdw6EH%2Fj6DrvJqB%2Fvv6bVWR7kjOuehk; bg5D_2132_smile=1D1; bg5D_2132_seccode=22485.58c095bd095d57b101; bg5D_2132_lip=36.102.208.214%2C1541659184; bg5D_2132_sid=mElHBZ; Hm_lvt_b8d70b1e8d60fba1e9c8bd5d6b035f4c=1540540375,1540955353,1541145834,1541562930; Hm_lpvt_b8d70b1e8d60fba1e9c8bd5d6b035f4c=1541659189; bg5D_2132_sendmail=1; bg5D_2132_checkpm=1; bg5D_2132_lastact=1541659204%09misc.php%09patch'
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
            html = etree.HTML(req.content.decode('utf-8'))
            #result=html.xpath('//div[@class="bus_vtem"]/a[@title!="紧急通知！紧急通知！紧急通知！"]/attribute::*')
            #print(result)
            htmllist = html.xpath('//div[@class="bus_vtem"]/a[@title!="紧急通知！紧急通知！紧急通知！" and @class="preview"]/@href')
            titlelist = html.xpath('//div[@class="bus_vtem"]/a[@title!="紧急通知！紧急通知！紧急通知！" and @class="preview"]/@title')
            print(htmllist)
            print(titlelist)
            print(len(htmllist))
            print(len(titlelist))            
            time.sleep(1)
            pass
        except:
            print('get over view error')

if __name__ == "__main__":
    asscrapy = AsScrapy()
    asscrapy.getOverView()
    

    
    
    
