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
COOKIES = '''usertrack=ezq0o1vmclAbmmk5OMxAAg==; _ntes_nnid=b096f727593c0259a23b83aca197d880,1541829216671; reglogin_hasopened=1; 
gdxidpyhxdE=AG%2FoH2LmznRZOLc2KqOrbQkAxRdr6oYGOlxByIxcCZka8WEH6yWMjCJCe%2FCX0VQoSRCTtpeRuYPLcPCliEhCqi%2BQWLIi78D8yf601VP9e%5C8JHktUf%5CYQCl73M3mZlfPtRjgX6YIP3G15%2F6kt2lkAcAhkidxHp%2BQ%2F%2B9SgKg4KEsNfW2Y%2B%3A1541830339384; 
_9755xjdesxxd_=32; 
firstentry=%2Flogin.do%3FX-From-ISP%3D1|https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DIZ2_Y5pqQrQYNjC_aRFYQePBqUrUYX1307i62FwRNy7%26wd%3D%26eqid%3Dba1637e00000a9ab000000035c17030c; 
LOFT_SESSION_ID=VVU7ndD7X8iMvEEmVo8hnohFqX1IDrwl; 
JSESSIONID-WLF-XXD=0d0f9e55b848ffbec124f3428d131b6c8a3ff082129cea88e7988f59375fd8509ced1296b52973eda4794e4a6474daaf66c85d6e1f662c6f40b1cf43980fce383c358c708b2e1fd828307b464cc616911d08a6982c5c3682feaa095e1a46f905921a3d21193cc994ec9bf54cf02a2dbdd47eb50ad367bc0554f59b766e75464d1ac7f2b6; fastestuploadproxydomainkey=uploadbj|1545011951875; hb_MA-BFD7-963BF6846668_source=zzzzzz562.lofter.com; reglogin_isLoginFlag=1; NTES_SESS=Tw6rySIkhnb.v0UOfECfCZqDRSDONRIcPfvgapTD0TfXLJgka6ijVuatN6.Uer3cNX4u7OXPQ6wIJqlPBSfZIWjaghchTCs_BM_M5RsRMOZ0J4Z2VLYB88LPEYyIS6h7BBQiN_TdyxxktYxlzRUVpPww46ueXXPf05neZgnAav2SMEEUNVJxhtzYkcLjBDkVOiAKKShOkZv2Uh46z0CrSXG7YF5q8L9bz; S_INFO=1544761481|0|3&amp; P_INFO=secondtonone1@163.com|1544761481|0|mail163|11&amp; NTESwebSI=E4F9CBC1DAD98D9AB2C3D06FC8D149D1.hzayq-lofter-web1.server.163.org-8010; regtoken=1000; _ga=GA1.2.1311476988.1541829217; _gid=GA1.2.649157831.1545011952; mp_MA-BFD7-963BF6846668_hubble=%7B%22sessionReferrer%22%3A%20%22http%3A%2F%2Fwww.lofter.com%2Flogin%22%2C%22updatedTime%22%3A%201545034246304%2C%22sessionStartTime%22%3A%201545033889496%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%209%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%229210bd51-6445-4ad9-9452-457bad1a328a%22%2C%22persistedTime%22%3A%201541829217311%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_u_logout%22%2C%22time%22%3A%201545034246304%7D%2C%22sessionUuid%22%3A%20%22fd902575-f8ee-4966-8345-485383dc9c23%22%7D; __utma=61349937.1311476988.1541829217.1545014533.1545033878.4; __utmb=61349937.15.9.1545034247320; __utmc=61349937; __utmz=61349937.1541829217.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; noAdvancedBrowser=0; LOFTER-PHONE-LOGINNUM=18301152001; LOFTER-PHONE-LOGIN-FLAG=1; 
LOFTER-PHONE-LOGIN-AUTH=HGWxetmhJ_KlftEvizRrPZiW393INrlAftO4MpEXf9DDHjYCXIPIqe5kATMe-vHW3IhcVa-HX94y%0ALORc1CJmNHJGWbzFhfdS'''
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
            time.sleep(2)
            
            phonebtn=self.wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"手机账号登录")]') ) )
            phonebtn.click()
            time.sleep(2)
            phoneitem = self.wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"contl-tel")]') )  )
            inputphone=phoneitem.find_element_by_xpath('.//input[contains(@type,"tel")]')
            inputphone.clear()
            #设置用户名输入框
            inputphone.send_keys('18301152001')            
            #设置密码
            password = phoneitem.find_element_by_xpath('.//input[contains(@type,"password")]')
            password.clear()
            password.send_keys('18301152001')
            loginbtn = self.wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"telnum-login")]') ))
            loginbtn.click()
            time.sleep(5)
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
                photolist = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='m-filecnt m-filecnt-1']" ) ) )
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
                self.driver_.switch_to_window(self.driver_.window_handles[-1])
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except:
            print('cycleScroll exception!!!!')    
   
    def dealPhotoItem(self,photoitem):
        try:
            photolist=photoitem.find_elements_by_xpath(".//li[@class='img']")
            for photo in photolist:
                photo.click()
                time.sleep(3)
                self.driver_.switch_to_window(self.driver_.window_handles[-1])
                jscode='window.scrollTo(0,document.body.scrollHeight)'
                self.driver_.execute_script(jscode)
                time.sleep(3)
                self.driver_.execute_script(jscode)
                time.sleep(3)
                elements=self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class,'imgclasstag')]" ) ) )
                self.savePhoto(*elements)
                self.driver_.close()
                self.driver_.switch_to_window(self.driver_.window_handles[-1])    
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except:
            print('dealPhotoItem exception!!!!')    

    def savePhoto(self,*elementlist):
        try:
            for element in elementlist:
                imgaddr=element.get_attribute('bigimgsrc')
                #.jpg .png .gif
                srctype=self.getSrcType(imgaddr,*SRCTYPES)
                if srctype is None:
                    continue
                imgname=imgaddr.split(srctype,1)[0].split('/')[-1]
                print('photo name is %s'   %(imgname+srctype))
        except:    
            print('savePhoto exception')
    
    def getSrcType(self,imgaddr,*types):
        for i in types:
            if imgaddr.find(i) != -1:
                return i
        return None


if __name__ == "__main__":
    #seleniumcookie = SeleniumCookie('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.2e0d63ffvOPH2N&id=575198548137&skuId=3774938064975&areaId=110100&user_id=1644123097&cat_id=2&is_b=1&rn=a2781533c3ad59ab4c24d1f4246113b2')
    seleniumcookie = SeleniumCookie('http://www.lofter.com/login?urschecked=true')
    seleniumcookie.open_window('http://sifanduizhangf8.lofter.com/view')
    seleniumcookie.cycleScroll()
    
    
    
    
