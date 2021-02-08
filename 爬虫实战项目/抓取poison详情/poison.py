#!/usr/bin/env python
#-*-coding:utf-8-*-
from tkinter import *
import hashlib
import time
import os
from pathlib import Path
from os.path import abspath
from tkinter.filedialog import (askopenfilename, 
                                    askopenfilenames, 
                                    askdirectory, 
                                    asksaveasfilename)

from concurrent.futures import ThreadPoolExecutor
import threading
import exifread
from shutil import copyfile
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from datetime import datetime
from queue import Queue
import threading
import queue


class SeleniumDriver(object):
    def __init__(self, path):
        options = webdriver.ChromeOptions() 
        options.add_argument('--ignore-certificate-errors') 
        options.add_argument('--ignore-ssl-errors') 

        self.driver_ = webdriver.Chrome(chrome_options=options)
        self.path = path
        self.wait = WebDriverWait(self.driver_,10)
        #self.saveCookies()
    def refresh_page(self):
        self.driver_.refresh()

    def open_window(self,urlnew):
        self.driver_.execute_script('window.open()')
        self.driver_.switch_to_window(self.driver_.window_handles[-1])
        self.driver_.get(urlnew)
        time.sleep(1)

    def get_url(self, urlnew):
        self.driver_.get(urlnew)
        pass

    def close_window(self):
        self.driver_.close()
        pass

    def quit_window(self):
        self.driver_.quit()
        pass

    #网页可视区高度
    def getcrollTop(self):
        js = "var q=document.body.clientHeight ;return(q)" 
        return self.driver_.execute_script(js) 
    #滚动条得高度
    def getbottomHeight(self):
        js = "var q=document.body.scrollHeight ;return(q)"
        return self.driver_.execute_script(js)

    def cycleScroll(self):
        try:
            bottom = self.getbottomHeight()
            js = "var q=document.body.clientHeight;return(q)"
            begin=0
            stop= 0
            temp = 0
            while(True):
                print('*************')
                jscode='window.scrollBy(0,50000)'
                self.driver_.execute_script(jscode)
                time.sleep(2)
                #判断是否到底部
                cur = self.getcrollTop()
                print('cur scroll top is %d' %(cur))
                print('bottom scroll height is %d' %(bottom))
                recommand = self.driver_.find_element_by_xpath('//*[@id="product"]/uni-view[4]/uni-view[11]/uni-view[2]')
                if recommand == None:
                    continue
                print(recommand)
                list_infos = recommand.find_elements_by_class_name('list-info')
                if temp == len(list_infos):
                    break
                temp = len(list_infos)
                #print(list_infos)
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except Exception as e:
            print('cycleScroll exception!!!! error is ', e)

    #品牌   主货号   品名    销量   颜色   码数  价格  下单日期  发货日期
    def get_detail(self):
        try:
            title = self.driver_.find_element_by_xpath('//*[@id="product"]/uni-view[4]/uni-view[1]/uni-view[2]/uni-text/span')
            print("title is ", title)
            if title == None:
                return
            print("title text is ", title.text)

            dir_path = os.path.join(self.path, title.text)
            if os.path.exists(dir_path) == False:
                os.mkdir(dir_path)

            detail_txt_path  = os.path.join(dir_path, title.text+".txt")
            detail_txt=open(detail_txt_path, "a",encoding='utf-8')
            detail_txt.write("品牌 {} \n" .format(title.text))
            price = self.driver_.find_element_by_xpath('//*[@id="product"]/uni-view[4]/uni-view[1]/uni-view[3]/uni-view/uni-text[2]/span')
            if price != None:
                detail_txt.write("价格 {} \n" .format(price.text))
            self.cycleScroll()
            element_find = self.driver_.find_element_by_xpath('//*[@id="product"]/uni-view[4]/uni-view[10]/uni-view[2]')
            if element_find != None:
                extra_lists = element_find.find_elements_by_class_name('extra-list')
                print("extra_lists are : ", extra_lists)
                for extra_data in extra_lists:
                    extra_title = extra_data.find_element_by_class_name('extra-list-title')
                    extra_info = extra_data.find_element_by_class_name('extra-list-info')
                    detail_txt.write(extra_title.text + ": " + extra_info.text) 
                    print('extra-list-title is ', extra_title.text)
                    print('extra-list-info is ', extra_info.text)
                    detail_txt.write('\n')
            
            try:
                detail_txt.write('尺码对照表: \n')
                detail_txt.write("=======================\n")
                size_info = self.driver_.find_element_by_xpath(
                    '//*[@id="product"]/uni-view[4]/uni-view[10]/uni-view[8]/uni-view/uni-view[2]/uni-view')
                report_info_list = size_info.find_elements_by_class_name('size-report-info')
                for report_info in report_info_list:
                    size_key_list = report_info.find_elements_by_class_name('size-key')
                    for size_key in size_key_list:
                        size_element = size_key.find_element_by_css_selector('span')
                        detail_txt.write(size_element.text + '   ')
                    detail_txt.write('\n')
                detail_txt.write("=======================\n")
            except Exception as e:
                print("catch ruler exception is ", e)
            
            near_buy = self.driver_.find_element_by_xpath('//*[@id="product"]/uni-view[4]/uni-view[7]/uni-view/uni-view[1]/uni-view[1]')
            desc = near_buy.find_element_by_class_name('desc')
            detail_txt.write(near_buy.text + " : " + desc.text +'\n')

            img_father = self.driver_.find_element_by_xpath('//*[@id="product"]/uni-view[4]/uni-view[9]/uni-view/uni-view[2]')
            img_lists = img_father.find_elements_by_css_selector('img')
            
            buyer_show = os.path.join(dir_path, '买家秀')
            if os.path.exists(buyer_show) == False:
                os.mkdir(buyer_show)
            img_index = 0
            for img in img_lists :
                img_url = img.get_attribute('src')
                img_index = img_index + 1
                img_name = str(img_index)+'.webp'
                img_path = os.path.join(buyer_show, img_name)
                rsp = requests.get(img_url)
                with open(img_path, 'wb') as img_file:
                    img_file.write(rsp.content)
                #print('img_url is ', img_url)
            sell_show = os.path.join(dir_path, '商品样图')
            if os.path.exists(sell_show) == False:
                os.mkdir(sell_show)
            sell_img = self.driver_.find_element_by_xpath('//*[@id="product"]/uni-view[4]/uni-view[10]/uni-view[5]/uni-image/img')
            sell_img_url = sell_img.get_attribute('src')
            print('sell img url is ', sell_img_url)
            rsp = requests.get(sell_img_url)
            sell_img_path = os.path.join(sell_show,  'sell.jpg')
            with open(sell_img_path, 'wb') as sell_img_file:
                sell_img_file.write(rsp.content)


        except Exception as e:
            print("exception is ", e)
        finally:
            detail_txt.close()
       
    #滚动直到某个元素出现
    def scrollBy_find(self,xpath):
        failes = 0
        while self.driver_.find_element_by_xpath(xpath) == None :
            if failes >= 3:
                break
            jscode='window.scrollBy(0,5000)'
            self.driver_.execute_script(jscode)
            time.sleep(1)
            failes = failes + 1
        print("failes is ", failes)
        element = self.driver_.find_element_by_xpath(xpath)
        print("element is ", element)
        return element    


class ReadFile(object):
    def __init__(self):
        self.data_path = os.path.dirname(os.path.abspath(__file__))
        self.data_path = os.path.join(self.data_path, "data.txt")
        #print(self.data_path) 
        pass
    def file_path(self):
        return self.data_path

class WriteFile(object):
    def __init__(self):
        self.path=os.path.dirname(os.path.abspath(__file__))
        now = datetime.now()
        timestr=now.strftime('%Y%m%d')
        self.path=os.path.join( self.path,timestr)
        if os.path.exists(self.path)==False:
            os.mkdir(self.path)
    def get_path(self):
        return self.path



def run_thread(n):
    print("thread %d begin work" %(n))
    
    chrome_driver = SeleniumDriver(write_file.get_path())
    while True:
        try:
            task = url_que.get(block=True, timeout=3)
            print(task)
            url_que.task_done()
            chrome_driver.open_window(task)
            #chrome_driver.cycleScroll()
            chrome_driver.get_detail()
        except queue.Empty:
            print('队列为空，get失败')
            break
        except Exception as e:
            print("exception is ", e)
            chrome_driver.quit_window()
            break

if __name__ == "__main__":
    read_file = ReadFile()
    write_file = WriteFile()
    url_que = Queue(maxsize=0)
    with open(read_file.file_path(), "r") as rd_file:
        lines = rd_file.readlines()
        for line in lines:
            if line == "" or line.replace('\n', '').replace('\r', '') == "":
                continue
            #print("line data is ", line)
            url_que.put(line)
            #测试一行文本用
            #break

    t1 = threading.Thread(target=run_thread, args=(1,))
    # t2 = threading.Thread(target=run_thread, args=(2,))
    t1.start()
   # t2.start()
    t1.join()
   # t2.join()
    url_que.join()
    '''
    #web driver
    driver = SeleniumDriver()
    print(driver.getcrollTop())
    print(driver.getbottomHeight())

    #启动线程池
    threadPool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="saveres_")
    #关闭线程池
    threadPool.shutdown(wait=True)
    '''