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
from datetime import datetime
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
SRCTYPES=['.jpg','.png','.gif']
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
        now = datetime.now()
        timestr=now.strftime('%Y%m%d')
        self.path=os.path.join( self.path,timestr)
        if os.path.exists(self.path)==False:
            os.mkdir(self.path)
        self.wait = WebDriverWait(self.driver_,10)
        self.initSession()
        self.chromeLogin()
        #self.saveCookies()
    def refresh_page(self):
        self.driver_.refresh()

    def open_window(self,urlnew):
        self.driver_.execute_script('window.open()')
        self.driver_.switch_to_window(self.driver_.window_handles[-1])
        self.driver_.get(urlnew)
        time.sleep(1)
    
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
    #弹窗保存cookies
    def saveCookies(self):
        js_code='alert(document.cookie)'
        self.driver_.execute_script(js_code)

    def chromeLogin(self):
        try:
            self.driver_.maximize_window()
            time.sleep(5)
            loginname=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginname"]') ) )
            loginname.click()
            #设置用户名输入框
            loginname.send_keys('18301152001')
            #设置密码
            password = self.wait.until(EC.presence_of_element_located( (By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input') )   )
            password.click()
            password.send_keys('')
            password.send_keys('18301152001c')
            loginbtn = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[6]/a') ))
            loginbtn.click()
            validbtn = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="dmCheck"]') ))
            validbtn.click()
            sendvalidbtn = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="send_dm_btn"]') ))
            sendvalidbtn.click()
            time.sleep(20)
            return True
        except NoSuchElementException:
            print('No Element')
            return False
            #self.driver_.close()
        except TimeoutException :
            print('TimeoutException')
            #self.driver_.close()
            return False
        except:
            print('chromeLogin exception')
            return False    

    #网页可视区高度
    def getcrollTop(self):
        js = "var q=document.body.clientHeight ;return(q)" 
        return self.driver_.execute_script(js) 
    def getbottomHeight(self):
        js = "var q=document.body.scrollHeight ;return(q)"
        return self.driver_.execute_script(js)

    #处理一个相簿里的图片列表
    def getPhotos(self,*photolist):
        try:
            for photoitem in photolist:
                self.dealPhotoItem(photoitem)
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except:
            print('getPhotos exception!!!!')    
            pass        

    def cycleScroll(self):
        try:
            bottom = self.getbottomHeight()
            js = "var q=document.body.clientHeight;return(q)"
            begin=0
            stop= 0
            while(True):
                #jscode='window.scrollTo(0,document.body.scrollHeight)'
                jscode='window.scrollBy(0,5000)'
                self.driver_.execute_script(jscode)
                time.sleep(10)
                photolist = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='photo_album_list clearfix']" ) ) )
                photolen = len(photolist)
                if(photolen == 0):
                    break
                if(photolen == begin):
                    print('photolen == begin')
                    if stop>=20:
                        break
                    stop = stop+1
                    jscode2='window.scrollBy(0,5000)'
                    self.driver_.execute_script(jscode2)
                    time.sleep(10)
                    continue
                stop=0
                self.getPhotos(*photolist[begin:])
                begin=photolen
                #判断是否到底部
                cur = self.getcrollTop()
                print('cur scroll top is %d' %(cur))
                print('bottom scroll height is %d' %(bottom))
                if(cur == bottom):
                    break
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except:
            print('cycleScroll exception!!!!')    
    #获取资源类型
    def getSrcType(self,photosrc):
        global SRCTYPES
        for type in SRCTYPES:
            if photosrc.find(type)!=-1:
                return type
        return None
    #根据资源类型获取xpath选择器
    def getSrcaddrByType(self,srctype):
        try:
            if(srctype=='.gif'):
                srcitem=self.wait.until(EC.visibility_of_element_located( (By.XPATH,"//div[contains(@class,'W_layer layer_multipic_preview')]//div[@node-type='gif_box']//video") )  )
                return srcitem.get_attribute('src')
            else:
                srcitem=self.wait.until(EC.visibility_of_element_located( (By.XPATH,"//div[contains(@class,'W_layer layer_multipic_preview')]//img[@hidefocus]") )  )
                return srcitem.get_attribute('src')
        except:
            return None
    #保存图片
    def savePhoto(self,photosrc,dirname):
        try:
            srctype=self.getSrcType(photosrc)
            if srctype is None:
                return
            imgaddr = self.getSrcaddrByType(srctype)
            if imgaddr is None:
                return
            imgname=os.path.join(dirname,imgaddr.split('?',1)[0].split('/')[-1])
            print('开始抓取%s' %(imgname))
            if os.path.exists(imgname)==False:
                img=self.session_.get(imgaddr,headers=self.headers_, cookies=self.cookiejar_).content
                with open(imgname,'wb') as imgfile:
                    imgfile.write(img)
            print('成功抓取%s' %(imgname))
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except:
            print('savePhoto exception!!!!')    

    #处理图片列表，一个相簿里的
    def dealPhotoItem(self,photoitem):
        try:
            dirname=photoitem.get_attribute('group_id')
            photolist=photoitem.find_elements_by_xpath(".//img[contains(@class,'photo_pict')]")
            if len(photolist) == 0:
                return
            print('photolist size is %d'%(len(photolist)))
            dirname = os.path.join(self.path,dirname)
            if os.path.exists(dirname)==False:
                os.mkdir(dirname)
            for photo in photolist:
                try:
                    photosrc=photo.get_attribute('src')
                    print('photosrc is %s'%(photosrc) )
                    if photosrc[-4:]== '.jpg':
                        continue
                    if photosrc[-4:]== '.png':
                        continue
                    if self.openPhoto(photo)==False:
                        continue
                    self.savePhoto(photosrc,dirname)
                finally:
                    self.closePhoto()
                
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except:
            print('dealPhotoItem exception!!!!')    

    def openPhoto(self,photo):
        try:  
            photo.click()
            time.sleep(3)
            return True
        except NoSuchElementException:
            print('No Element')
            return False
        except TimeoutException :
            print('TimeoutException')
            return False
        except:
            print('openPhoto exception!!!!')
            return False    

    def closeSure(self):
        try:
            #self.driver_.find_elements_by_xpath("//div[@class='W_layer ']" ).click() 
            surbtn = self.driver_.find_elements_by_xpath("//a[contains(@action-type,'ok')]" )
            actions = ActionChains(self.driver_)
            actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            #surbtn.click()
            #surbtn.send_keys(Keys.ENTER)
            #self.driver_.execute_script("arguments[0].click();", surbtn);
            time.sleep(3)
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except:
            print('closeSure exception!!!!')

    def closePhoto(self):
        try:
            closebtn=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'W_layer layer_multipic_preview')]//*[@title='关闭']")))  
            closebtn.click()
            time.sleep(2)
        except NoSuchElementException:
            print('closePhoto No Element')
        except TimeoutException :
            print('closePhoto TimeoutException')
            self.closeSure() 
        except:
            print('close Photo error!!')
            self.closeSure() 
            pass
if __name__ == "__main__":
    #seleniumcookie = SeleniumCookie('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.2e0d63ffvOPH2N&id=575198548137&skuId=3774938064975&areaId=110100&user_id=1644123097&cat_id=2&is_b=1&rn=a2781533c3ad59ab4c24d1f4246113b2')
    seleniumcookie = SeleniumCookie('https://weibo.com/')
    seleniumcookie.open_window('https://weibo.com/p/1005052760817614/photos?from=page_100505&mod=TAB#place')
    seleniumcookie.cycleScroll()
    
   
    
    
