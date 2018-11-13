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
COOKIES = 'cna=GckCFG0yEU4CASRm0NbUoE2C; _m_h5_tk=24e507e1469c6413e33c55b81cb8402a_1541748207288; _m_h5_tk_enc=f65a4db97268f95ad86281a622bf80ba; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; hng=CN%7Czh-CN%7CCNY%7C156; t=3bb6c88ed71a6bd56a58298c110368ae; tracknick=crazy%5Cu8FB0; lid=crazy%E8%BE%B0; _tb_token_=f77eeee39779e; cookie2=1577c0c8c39c76da8d87364555c2bba5; pnm_cku822=098%23E1hvZpvUvbpvUvCkvvvvvjiPR2qvgjr2RFqytjivPmPwlj38PFSvgjD8Rsq96jDviQhvCvvvpZptvpvhvvCvpvGCvvpvvPMMvphvC9mvphvvvbyCvm9vvhv9vvvvvvvvp6hvvUHnvvCj1Qvvv3QvvhNjvvvmmvvvBGwvvUHnuphvmvvvpoO%2BKW6UkphvC9hvpyPZgvyCvhAvsXKfjc7JeE9fwydO1EkwVEZDNr3lHd8rV1693E7rVug7EcqhQ8TJybUfbc7QrETAdcHCaNAX5E9XJyFWsE97RqwiLO2v5fVQKoZH; cq=ccp%3D1; isg=BJmZv2AMJuKuSPoaA2j9nHyapoWzjox2ZwN6ybtOPUK8wrlUA3TkqjjIwMYR4SUQ'
from selenium.webdriver import ActionChains#引入动作链

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    options.add_argument('user-agent="'+USER_AGENT+'"')
    options.add_argument('cookie="'+COOKIES+'"')
    browser = webdriver.Chrome(chrome_options=options)

    try:
        browser.get('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.1bd663b51xC1vK&id=13708921279&skuId=3867841200352&user_id=820708319&cat_id=2&is_b=1&rn=5d952ad1e21b5d79bb3b7fbbffc35212')
        wait = WebDriverWait(browser,5)
        time.sleep(10)
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(10)
        #inputbt = wait.until(EC.element_to_be_clickable( ( By.CSS_SELECTOR,'#J_RateWithPicture1542094514279') ) )
        #inputbt = wait.until(EC.element_to_be_clickable( ( By.CSS_SELECTOR,'#col-extra') ) )
        #inputbt.click()
        #target = browser.find_element_by_id('J_RateWithPicture1542094514279')
        #browser.execute_script("arguments[0].scrollIntoView(false);",target)
    except NoSuchElementException:
        print('No Element')
    #except TimeoutException :
        #print('TimeoutException')
   
    except:
        #
        print('exception')
        browser.close()
        pass
    
    
    
    
