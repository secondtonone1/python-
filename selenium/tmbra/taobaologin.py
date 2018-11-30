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
class SeleniumCookie(object):
    def __init__(self,url):
        option = webdriver.ChromeOptions()
        # 设置中文
        option.add_argument('lang=zh_CN.UTF-8')
        #options.add_argument(r"user-data-dir=C:\Users\secondtonone1\AppData\Local\Google\Chrome\User Data")
        self.url_=url
        self.driver_ = webdriver.Chrome(chrome_options=option)
        self.driver_.get(self.url_)
        self.path=os.path.dirname(os.path.abspath(__file__))
        self.cookiepath = os.path.join(self.path,"seleniumcookies.pk1")
        self.save_cookie()
        self.load_cookie()
        self.refresh_page()
        self.wait = WebDriverWait(self.driver_,10)
    def save_cookie(self):
        if(os.path.exists(self.cookiepath)):
            return
        time.sleep(60)
        with open (self.cookiepath,"wb") as f:
            pickle.dump(self.driver_.get_cookies(),f)
        

    def load_cookie(self):
        self.driver_.delete_all_cookies()
        with open (self.cookiepath,"rb") as f:
            cookies=pickle.load(f)        
            for cookie in cookies:
                cookie_dict = {
                    "domain": ".taobao.com",  # 火狐浏览器不用填写，谷歌要需要
                    'name': cookie.get('name'),
                    'value': cookie.get('value'),
                    "expires": "",
                    'path': '/',
                    'httpOnly': False,
                    'HostOnly': False,
                    'Secure': False}
                self.driver_.add_cookie(cookie_dict)     
   

    def openWindow(self,urlnew):
        #打开选项卡
        self.driver_.execute_script('window.open()')
        self.driver_.switch_to_window(self.driver_.window_handles[1])
        self.driver_.get(urlnew)
  
    def refresh_page(self):
        self.driver_.refresh()

    def closeDialog(self):
        try:
            comment = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/div[2]') ))
            self.driver_.switch_to.frame('sufei-dialog-content')
            #self.driver_.switch_to.parent_frame()
            self.driver_.switch_to.default_content()
            closebtn=self.wait.until(EC.presence_of_element_located(( By.XPATH, '//*[@id="sufei-dialog-close"]'))  )
            closebtn.click()
            #actions = ActionChains(self.driver_)
            #actions.double_click(closebtn).perform()
        except NoSuchElementException:
            print('No Element')
            #self.driver_.close()
        except TimeoutException :
            print('TimeoutException')
            #self.driver_.close()
        except:
            print('exception')
        
    def clickComment(self):
        try:
            comments = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_TabBar"]/li[2]' ) ) )
            comments.click()
            time.sleep(1)
            comentall  = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_Reviews"]/div/div[5]/span[1]' )  ) )
            #J_Reviews > div > div.rate-toolbar > span.rate-filter 
            #J_Reviews > div > div.rate-toolbar > span.rate-filter > label:nth-child(2)
            comentpic = comentall.find_element_by_css_selector('input:nth-child(5)')
            comentpic.click() 
           
            time.sleep(1)
        except NoSuchElementException:
            print('No Element')
            self.driver_.close()
        except TimeoutException :
            print('TimeoutException')
            self.driver_.close()
        except:
            print('exception')    
            
        
       
       
if __name__ == "__main__":
    seleniumcookie = SeleniumCookie('https://www.taobao.com/')
    seleniumcookie.openWindow('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.2e0d63ffvOPH2N&id=575198548137&skuId=3774938064975&areaId=110100&user_id=1644123097&cat_id=2&is_b=1&rn=a2781533c3ad59ab4c24d1f4246113b2')
    seleniumcookie.closeDialog()
    seleniumcookie.clickComment()

   
    
    
    
    
