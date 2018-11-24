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
import win32api
import win32con
COOKIES='__cfduid=d78f862232687ba4aae00f617c0fd1ca81537854419; \
            bg5D_2132_saltkey=jh7xllgK; \
            bg5D_2132_lastvisit=1540536781; \
            bg5D_2132_auth=479fTpQgthFjwwD6V1Xq8ky8wI2dzxJkPeJHEZyv3eqJqdTQOQWE74ttW1HchIUZpgsyN5Y9r1jtby9AwfRN1R89;\
            bg5D_2132_lastcheckfeed=7469%7C1541145866; \
            bg5D_2132_smile=1D1; \
            bg5D_2132_atarget=1; \
            bg5D_2132_visitedfid=41D38D65D44D81D2D73D52; \
            bg5D_2132_lip=113.116.247.56%2C1542974645; \
            bg5D_2132_ulastactivity=ebed2%2FIcR%2BJgOK4ZgbSMfbvb%2FoMicqXqOT9aou3X%2FT0z6h5dQfMS; \
            bg5D_2132_st_t=7469%7C1543028123%7C268cc1f5bc735c1406770754715736e3; \
            bg5D_2132_forum_lastvisit=D_41_1543028123; \
            bg5D_2132_sid=Bo8GCp; \
            Hm_lvt_b8d70b1e8d60fba1e9c8bd5d6b035f4c=1542594137,1542856492,1542937648,1543027830; \
            Hm_lpvt_b8d70b1e8d60fba1e9c8bd5d6b035f4c=1543028358; \
            bg5D_2132_lastact=1543028380%09misc.php%09patch'
class SeleniumCookie(object):
    def __init__(self,url):
        option = webdriver.ChromeOptions()
        # 设置中文
        option.add_argument('lang=zh_CN.UTF-8')
      
        self.url_=url
        self.driver_ = webdriver.Chrome(chrome_options=option)
        self.driver_.get(self.url_)
        self.wait = WebDriverWait(self.driver_,timeout=15)
        
    def login(self):
        self.driver_.delete_all_cookies()
        for item in COOKIES.split(';'):
            name, value = item.split('=',1)
            name=name.replace(' ','').replace('\r','').replace('\n','')
            value=value.replace(' ','').replace('\r','').replace('\n','')
            cookie_dict = {
                    'name':name,
                    'value':value
                }                
            self.driver_.add_cookie(cookie_dict)
        self.refresh_page()
        time.sleep(1)

    def refresh_page(self):
        self.driver_.refresh()
            
    def findItemList(self):
        try:
            itemnode = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="portal_block_36_content"]')) )
            print(type(itemnode))   
            itemlist=itemnode.find_elements_by_tag_name('li')
            for item in itemlist[1:]:
                divtag=item.find_element_by_tag_name('div')
                itemdata=divtag.find_element_by_tag_name('a')
                self.getItemPage(itemdata)
                #print(itemdata.get_attribute('href'))
            #print(itemlist)                                                               
            #//*[@id="portal_block_36_content"]/li[1]
            print("success!!!")
            pass
        except TimeoutException :
            print('TimeoutException')
            self.driver_.close()
        except NoSuchElementException:
            print('No Element')
            self.driver_.close()
        except:
            print('exception')
            self.driver_.close()
            pass

    def getItemPage(self,itemelement):
        try:
            actionChain = ActionChains(self.driver_)
            actionChain.context_click(itemelement).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            self.switchWindow()
            node=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="postlist"]/div[3]/div[1]') ) )
            print(node)
            # -1代表向下移动一个单位，-100也会向下移动一个单位，都是一个单位哦，亲~
            #win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-1)
            #self.switchWindow()
            time.sleep(2000)
            pass
        except TimeoutException :
            print('TimeoutException')
            self.driver_.close()
        except NoSuchElementException:
            print('No Element')
            self.driver_.close()
        except:
            print('exception')
            self.driver_.close()
            pass

    def switchWindow(self):
            #打开选项卡
        self.driver_.switch_to_window(self.driver_.window_handles[1])
        #self.refresh_page()

if __name__ == "__main__":
    seleniumcookie = SeleniumCookie('https://www.aisinei.org/portal.php')
    seleniumcookie.login()
    seleniumcookie.findItemList()

   
    
    
    
    
