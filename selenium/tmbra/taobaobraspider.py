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
COOKIES = '''cna=GckCFG0yEU4CASRm0NbUoE2C; x=__ll%3D-1%26_ato%3D0; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; tk_trace=1; 
lid=crazy%E8%BE%B0; _m_h5_tk=1412a5bb70345e741316f6b4092c5a4b_1543555914351; _m_h5_tk_enc=ce02f0ef44994e6d42a14de452917595; 
hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=V32FPkk%2FgihF%2FS5nr3O5&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTYNc5wRClZhw%3D%3D&tag=8&lng=zh_CN; 
uc3=vt3=F8dByR1X72cdQmVCMLM%3D&id2=Vv8bJyUX4ucp&nk2=AGiWgxGOaA%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=crazy%5Cu8FB0; _l_g_=Ug%3D%3D; ck1=""; unb=512125475; lgc=crazy%5Cu8FB0; 
cookie1=AiOe9QtrbFbaKePULR76ROhp4apbOZgD2v%2BKmVWx0w0%3D; login=true; cookie17=Vv8bJyUX4ucp; cookie2=1c2f09f5957a1856c79b0591f0657a47; 
_nk_=crazy%5Cu8FB0; t=3bb6c88ed71a6bd56a58298c110368ae; uss=""; 
csg=e73c9128; skt=d1c28c55ad9d8970; _tb_token_=333e565e3d4f; cq=ccp%3D0; isg=BHR0rjdplKcnrwdtllPIg-GBSzIm5ZmEymjn3g7Ukf-CeRbDNli1x3p7_fEEmtCP'''
class SeleniumCookie(object):
    def __init__(self,url):
        option = webdriver.ChromeOptions()
        # 设置中文
        option.add_argument('lang=zh_CN.UTF-8')
        self.url_=url
        self.driver_ = webdriver.Chrome(chrome_options=option)
        #先加载网站
        self.driver_.get(self.url_)
        self.path=os.path.dirname(os.path.abspath(__file__))
        #补充网络cookie
        self.initChromCookie()
        #刷新页面
        self.refresh_page()
        self.wait = WebDriverWait(self.driver_,10)
        self.initSession()
     
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

    def initChromCookie(self):
        for item in COOKIES.split(';'):
            name,value = item.split('=',1)
            name=name.replace(' ','').replace('\r','').replace('\n','')
            value = value.replace(' ','').replace('\r','').replace('\n','')
            cookie_dict={  
                    'name':name,
                    'value':value,
                    "domain": ".taobao.com",  # 火狐浏览器不用填写，谷歌要需要
                    "expires": "",
                    'path': '/',
                    'httpOnly': False,
                    'HostOnly': False,
                    'Secure': False
                    }
            self.driver_.add_cookie(cookie_dict)
        pass

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
    seleniumcookie = SeleniumCookie('https://www.taobao.com')
    #seleniumcookie.open_window('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.2e0d63ffvOPH2N&id=575198548137&skuId=3774938064975&areaId=110100&user_id=1644123097&cat_id=2&is_b=1&rn=a2781533c3ad59ab4c24d1f4246113b2')
    seleniumcookie.open_window('https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-14466875947.288.48b1e2afDwQjMa&id=44530629386&rn=d8322d2c37f5f5becd468ba8e5d37529')
    seleniumcookie.close_dialog()
    seleniumcookie.clickComment()

   
    
    
    
    
