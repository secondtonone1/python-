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
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

from selenium.webdriver import ActionChains#引入动作链

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    options.add_argument('user-agent="'+USER_AGENT+'"')
    browser = webdriver.Chrome(chrome_options=options)

    try:
        browser.get('https://weibo.com/mumianmian123?refer_flag=0000015010_&from=feed&loc=nickname&is_all=1')
        
        wait = WebDriverWait(browser,15)
        i = 0
        while(i < 1000):
            browser.execute_script('window.scrollBy(0,1000)')
            i=i+1
            time.sleep(5)
    except NoSuchElementException:
        print('No Element')
        browser.close()
    except TimeoutException :
        print('TimeoutException')
        browser.close()
    except:
        #
        print('exception')
        browser.close()
        pass
    
    
    
    
