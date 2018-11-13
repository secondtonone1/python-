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
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
#COOKIES = '__cfduid=d78f862232687ba4aae00f617c0fd1ca81537854419; bg5D_2132_saltkey=jh7xllgK; bg5D_2132_lastvisit=1540536781; bg5D_2132_auth=479fTpQgthFjwwD6V1Xq8ky8wI2dzxJkPeJHEZyv3eqJqdTQOQWE74ttW1HchIUZpgsyN5Y9r1jtby9AwfRN1R89; bg5D_2132_lastcheckfeed=7469%7C1541145866; bg5D_2132_ulastactivity=2bbfoTOtWWimnqaXyLbTv%2Buq4ens5zcXIiEAhobA%2FsWLyvpXVM9d; bg5D_2132_sid=wF3g17; Hm_lvt_b8d70b1e8d60fba1e9c8bd5d6b035f4c=1540540375,1540955353,1541145834,1541562930; Hm_lpvt_b8d70b1e8d60fba1e9c8bd5d6b035f4c=1541562973; bg5D_2132_lastact=1541562986%09home.php%09spacecp'
from selenium.webdriver import ActionChains#引入动作链

if __name__ == "__main__":
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.taobao.com/')
        inputline = browser.find_element_by_id('q')
        inputline.send_keys('图书')
        time.sleep(1)
        inputline.clear()
        inputline.send_keys('内衣')
        searchbtn = browser.find_element_by_class_name('search-button')
        searchbtn.click()
        browser.close()        
    except:
        #
        print('exception')
        pass
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser = webdriver.Chrome()
    browser.get(url)
    browser.switch_to.frame('iframeResult')#切换到iframeResult框架
    source = browser.find_element_by_css_selector('#draggable')#找到被拖拽对象
    target = browser.find_element_by_css_selector('#droppable')#找到目标
    actions = ActionChains(browser)#声明actions对象
    actions.drag_and_drop(source, target)
    actions.perform()#执行动作
    browser.close()
    
    
    
