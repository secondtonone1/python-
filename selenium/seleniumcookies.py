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
        self.url_=url
        self.driver_ = webdriver.Chrome()
        self.driver_.get(self.url_)
        self.path=os.path.dirname(os.path.abspath(__file__))
        self.cookiepath = os.path.join(self.path,"seleniumcookies.pk1")
            
    def login(self):
        time.sleep(30)
        #此时扫码登陆
        self.driver_.refresh()
        self.save_cookie()
        self.driver_.refresh()
    def openWindow(self):
        #打开选项卡
        self.driver_.execute_script('window.open()')
        self.driver_.switch_to_window(self.driver_.window_handles[1])
        self.driver_.get(self.url_)
    def save_cookie(self):
        try:
            pickle.dump(self.driver_.get_cookies(),open (self.cookiepath,"wb"))
        except:
            print("exception")
        # with open ("seleniumcookies.pk1","wb") as f:
        #     pickle.dump(self.driver_.get_cookies(),f)
    def load_cookie(self):
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
    def refresh_page(self):
        self.driver_.refresh()
        self.driver_.get(self.url_)   
if __name__ == "__main__":
    seleniumcookie = SeleniumCookie('https://www.taobao.com/')
    seleniumcookie.login()
    #seleniumcookie.load_cookie()
    seleniumcookie.openWindow()
    seleniumcookie2 = SeleniumCookie('https://www.taobao.com/')
    seleniumcookie2.load_cookie()
    seleniumcookie2.refresh_page()
    

   
    
    
    
    
