#-*-coding:utf-8-*-
import requests
import re
import time
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains#引入动作链
import pickle
import os
import sys
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
COOKIES = '''SINAGLOBAL=2649989373301.307.1534843664455; 
UM_distinctid=1658a0b6124890-079f3bc67a0c5c-10724c6f-1fa400-1658a0b6125d94; 
sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221655bd8059b16e-0637d6563149ba-10724c6f-2073600-1655bd8059ca65%22%2C%22%24device_id%22%3A%221655bd8059b16e-0637d6563149ba-10724c6f-2073600-1655bd8059ca65%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; 
wvr=6; Ugrow-G0=5b31332af1361e117ff29bb32e4d8439; 
login_sid_t=2fc6b49d277063ef23d7d80afc40bd02; cross_origin_proto=SSL; YF-V5-G0=2da76c0c227d473404dd0efbaccd41ac;
 _s_tentry=passport.weibo.com; wb_view_log=1920*10801; Apache=8404223678000.171.1544076367182; 
ULV=1544076367199:21:1:1:8404223678000.171.1544076367182:1543570140993; SSOLoginState=1544076399; 
SCF=AomA4wk3E9GyyVH1ekTlDicybOwuh2HAZh7jAsFcnZPBit07Y8us0EnocxsP17NtUfSqGPLhG9COmD-8Y70IuS8.; 
SUB=_2A25xDMwpDeRhGedG4lQV8SzKyD-IHXVSe7rhrDV8PUNbmtAKLXPekW9NUOdR3C307RWnH87dF0HlwSgaGrHjTHBQ; 
SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5uTk4Kxuonmhpxb9WRPNqJ5JpX5K2hUgL.Fo2R1KqXeKzce0e2dJLoIEBLxKBLB.zL122LxKqL1heL1-eLxKBLB.BL1K-LxK-LBKBL1K-t; 
SUHB=0jBJD2CO2AYKVH; ALF=1575612408; un=secondtonone1@163.com; YF-Page-G0=0dccd34751f5184c59dfe559c12ac40a; wb_view_log_1896412633=1920*10801; 
wb_timefeed_1896412633=1; 
UOR=v.ifeng.com,widget.weibo.com,www.baidu.com'''

class SeleniumCookie(object):
    def __init__(self,url):
        option = webdriver.ChromeOptions()
        # 设置中文
        option.add_argument('lang=zh_CN.UTF-8')

        prefs = {
        'profile.default_content_setting_values' :
            {
            'notifications' : 2
            }
        }
        option.add_experimental_option('prefs',prefs)
        self.url_=url
        self.driver_ = webdriver.Chrome(chrome_options=option)
        #先加载网站
        self.driver_.get(self.url_)
        self.path=os.path.dirname(os.path.abspath(__file__))
        self.wait = WebDriverWait(self.driver_,10)
        self.initSession()
        self.chromeLogin()
        #self.saveCookies()
    def refresh_page(self):
        self.driver_.refresh()

    def open_window(self,urlnew):
        self.driver_.execute_script('window.open()')
        self.driver_.switch_to_window(self.driver_.window_handles[1])
        self.driver_.get(urlnew)
        time.sleep(1)
    
    def close_dialog(self):
        try:
            comment = self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[9]/div[2]')) )
            #self.driver_.switch_to.frame('sufei-dialog-content')
            #self.driver_.switch_to.default_content()
            closebtn = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="sufei-dialog-close"]')) )
            closebtn.click()
            #也可以通过ActionChains双击实现
            #actions = ActionChains(self.driver_)
            #actions.double_click(closebtn).perform()
            time.sleep(1)
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
            #self.driver_.close()
        except:
            print(' close_dialog exception')

    def close_dialogm(self):
        try:
            closebtn=self.driver_.find_element_by_xpath("//a[@class='sufei-tb-dialog-close sufei-tb-overlay-close']")
            #closebtn = self.wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='sufei-tb-dialog-close sufei-tb-overlay-close']")) )
            closebtn.click()
        except NoSuchElementException:
            print('No Element')
            #self.driver_.close()
        except TimeoutException :
            print('TimeoutException')
            #self.driver_.close()
        except:
            print('close_dialogm exception')    

    def initSession(self):
        self.session_=requests.Session()
        self.headers_ = {'User-Agent':USER_AGENT,}
        self.cookiejar_ = requests.cookies.RequestsCookieJar()
        for item in COOKIES.split(';'):
            name ,value = item.split('=',1)
            name=name.replace(' ','').replace('\r','').replace('\n','')
            value = value.replace(' ','').replace('\r','').replace('\n','')
            self.cookiejar_.set(name,value)
        pass

    def saveCookies(self):
        js_code='alert(document.cookie)'
        self.driver_.execute_script(js_code)

    def chromeLogin(self):
        try:
            self.driver_.maximize_window()
            time.sleep(1)
            loginname=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginname"]') ) )
            loginname.click()
            #设置用户名输入框
            loginname.send_keys('18301152001')
            #设置密码
            password = self.wait.until(EC.presence_of_element_located( (By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input') )   )
            password.click()
            password.send_keys('18301152001c')
            loginbtn = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[6]/a') ))
            loginbtn.click()
            return True
        except:
            return False
       
    def clickComment(self):
        try:
            comments = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_TabBar"]/li[2]' ) ) )
            comments.click()
            time.sleep(1)
            comentall  = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_Reviews"]/div/div[5]/span[1]' )  ) )
            self.close_dialogm()
            #J_Reviews > div > div.rate-toolbar > span.rate-filter 
            #J_Reviews > div > div.rate-toolbar > span.rate-filter > label:nth-child(2)
            comentpic = comentall.find_element_by_css_selector('input:nth-child(5)')
            comentpic.click() 
            time.sleep(1)
            self.close_dialogm()
            self.driver_.execute_script('window.scrollBy(0,1000)')
            time.sleep(1)
            nextpagebtn= self.wait.until(EC.element_to_be_clickable( (By.XPATH, '//*[contains(text(),"下一页")]')) )
            lastpage = nextpagebtn.get_attribute('data-page')
            while ( nextpagebtn ):
                print('正在爬取第%d页'%(int(lastpage)-1))
                self.getPhotos()
                print('爬取第%d页成功'%(int(lastpage)-1))
                nextpagebtn.click()
                time.sleep(2)
                nextpagebtn= self.wait.until(EC.element_to_be_clickable( (By.XPATH, '//*[contains(text(),"下一页")]')) )
                curpage = nextpagebtn.get_attribute('data-page')
                if(lastpage==curpage):
                    break
                lastpage = curpage
        except NoSuchElementException:
            print('No Element')
            self.driver_.close()
        except TimeoutException :
            print('TimeoutException')
            self.driver_.close()
        except:
            print('clickComment exception')    

    def getPhotos(self):
        try:
            waitcomment = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='tm-rate-content']" ) ) )
            commentss=self.driver_.find_elements_by_xpath("//div[@class='tm-rate-content']")
            #print(type(commentss))
            #print(len(commentss))
            self.getPhoto(*commentss)
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except:
            print('getPhotos exception!!!!')    
            pass        
        
    def getPhoto(self,*comentlist):
        try:
            for comments in comentlist:
                #print(len(comentlist))
                #print(type(comments))
                desc=comments.find_element_by_class_name('tm-rate-fulltxt').text
                if len(desc) == 0:
                    desc='abcdef'
                dirfix=desc[0:6]
                dirname=os.path.join(self.path,dirfix)
                if os.path.exists(dirname) == False:
                    os.makedirs(dirname)
                txtname=os.path.join(dirname,desc[0:6]+'.txt')
                if os.path.exists(txtname) == False:
                    with open (txtname,'w',encoding='utf-8') as file:
                        file.write(desc)
                photos=comments.find_element_by_class_name('tm-m-photos')
                photos=photos.find_element_by_class_name('tm-m-photos-thumb')
                photos=photos.find_elements_by_tag_name('li')
                for ph in photos:
                    phaddr=ph.get_attribute('data-src')
                    print(phaddr)
                    bigph=phaddr.split('_4')[0]
                    print(bigph)
                    imgname= os.path.join(dirname ,bigph.split('/')[-1])
                    if os.path.exists(imgname) :
                        continue
                    img=self.session_.get('http:'+bigph,headers=self.headers_,cookies=self.cookiejar_).content
                    print('正在爬取%s' %(bigph))
                    with open (imgname,'wb') as imgfile:
                        imgfile.write(img)
                    print('爬取成功%s' %(bigph))
                    time.sleep(2)
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except:
            print('getPhoto exception')    
            pass        
       
       
if __name__ == "__main__":
    #seleniumcookie = SeleniumCookie('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.2e0d63ffvOPH2N&id=575198548137&skuId=3774938064975&areaId=110100&user_id=1644123097&cat_id=2&is_b=1&rn=a2781533c3ad59ab4c24d1f4246113b2')
    seleniumcookie = SeleniumCookie('https://weibo.com/')
   

   
    
    
    
    
