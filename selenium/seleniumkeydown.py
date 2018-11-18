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
        browser.get('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.1bd663b51xC1vK&id=13708921279&skuId=3867841200352&user_id=820708319&cat_id=2&is_b=1&rn=5d952ad1e21b5d79bb3b7fbbffc35212')
        
        wait = WebDriverWait(browser,15)
        comment = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_TabBar"]/li[2]'    ) ))
        comment.click()

        title = wait.until( EC.presence_of_element_located((By.XPATH, '//*[@id="J_TabBarBox"]'    ) ) )
        title.click()
        actions = ActionChains(browser)
        i = 0
        while i < 5 :
            actions.key_down(Keys.DOWN).key_down(Keys.UP).perform()
            time.sleep(1)
            i=i+1
        print('..........................................')
        #inputbt = wait.until(EC.element_to_be_clickable( ( By.CSS_SELECTOR,'#J_RateWithPicture1542094514279') ) )
        #inputbt = wait.until(EC.element_to_be_clickable( ( By.CSS_SELECTOR,'#col-extra') ) )
        #inputbt.click()
        #target = browser.find_element_by_id('J_RateWithPicture1542094514279')
        #browser.execute_script("arguments[0].scrollIntoView(false);",target)
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
    
    
    
    
