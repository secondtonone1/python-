#-*-coding:utf-8-*-
import requests
import re
import time
import os
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

class MaoYanScrapy(object):
    def __init__(self,pages=1):
        self.m_session = requests.Session()
        self.m_headers = {'User-Agent':USER_AGENT,}
        self.m_compilestr = r'<dd>.*?<i class="board-index.*?<img data-src="(.*?)@.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">.*?(.*?)</p'
        self.m_pattern = re.compile(self.m_compilestr,re.S)
        self.m_pages = pages
        self.dirpath = os.path.split(os.path.abspath(__file__))[0]
        
    
    def getPageData(self):
        try:
            for i in range(self.m_pages):
                httpstr = 'http://maoyan.com/board/4?offset='+str(i)
                req = self.m_session.get(httpstr,headers=self.m_headers,timeout=5)
                lists = re.findall(self.m_pattern,req.content.decode('utf-8'))
                time.sleep(1)
                for item in lists:
                    img = item[0]
                    print(img.strip()+'\n')
                    name = item[1]
                    dirpath = os.path.join(self.dirpath,name)
                    if(os.path.exists(dirpath)==False):
                        os.makedirs(dirpath)
                    print(name.strip()+'\n')
                    actor = item[2]
                    print(actor.strip()+'\n')
                    fiemtime = item[3]
                    print(fiemtime.strip()+'\n')
                    txtname = name+'.txt'
                    txtname = os.path.join(dirpath,txtname)
                    if(os.path.exists(txtname)==True):
                        os.remove(txtname)
                    with open (txtname,'w') as f:
                        f.write(img.strip()+'\n')
                        f.write(name.strip()+'\n')
                        f.write(actor.strip()+'\n')
                        f.write(fiemtime.strip()+'\n')
                    picname=os.path.join(dirpath,name+'.'+img.split('.')[-1])
                    if(os.path.exists(picname)):
                        os.remove(picname)
                    req=self.m_session.get(img,headers=self.m_headers,timeout=5)
                    time.sleep(1)
                    with open(picname,'wb') as f:
                        f.write(req.content)
                    

                

        except:
            print('get error')




if __name__ == "__main__":
    maoyanscrapy = MaoYanScrapy()
    maoyanscrapy.getPageData()

    
    
    
