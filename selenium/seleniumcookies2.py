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
        options = webdriver.ChromeOptions()
        # 设置中文
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument(r"user-data-dir=C:\Users\secondtonone1\AppData\Local\Google\Chrome\User Data")
        self.url_=url
        self.driver_ = webdriver.Chrome(chrome_options=options)
        self.driver_.get(self.url_)
        self.path=os.path.dirname(os.path.abspath(__file__))
        
            
   
    def openWindow(self):
        #打开选项卡
        self.driver_.execute_script('window.open()')
        self.driver_.switch_to_window(self.driver_.window_handles[1])
        self.driver_.get(self.url_)
  
        # with open ("seleniumcookies.pk1","wb") as f:
        #     pickle.dump(self.driver_.get_cookies(),f)
  
    def refresh_page(self):
        self.driver_.refresh()
        self.driver_.get(self.url_)   
if __name__ == "__main__":
    seleniumcookie = SeleniumCookie('https://www.taobao.com/')
    #seleniumcookie.login()
    seleniumcookie.openWindow()
   
    

   
    
    
    
    
