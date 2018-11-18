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
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

from selenium.webdriver import ActionChains#引入动作链

if __name__ == "__main__":
    browser = webdriver.Chrome()
    try:
        #browser.get('https://www.zhihu.com/explore')
        browser.get('https://www.taobao.com/')
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        browser.execute_script('alert("To Bottom")')
        #browser.close()        
    except:
        #
        print('exception')
        pass
   
    
    
    
