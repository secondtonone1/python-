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

class MyGui(object):
    def __init__(self,init_window_name):
        self.init_window_name=init_window_name

    def set_init_window(self):
        self.init_window_name.title("毒详情抓取工具")
        self.init_window_name.geometry('540x320+10+10')
        self.init_data_label = Label(self.init_window_name, text="详情链接")
        self.init_data_label.grid(row=0, column=0)
      

        self.result_link_label = Label(self.init_window_name, text="==>")
        self.result_link_label.grid(row=0, column=20)

        self.result_data_label = Label(self.init_window_name, text="抓取结果")
        self.result_data_label.grid(row=0, column=28)

        #文本框
        self.init_data_Text = Text(self.init_window_name, width=30, height=10)  #链接地址
        self.init_data_Text.grid(row=1, column=0, rowspan=5, columnspan=5)
        self.result_data_Text = Text(self.init_window_name, width=30, height=10)  #链接结果
        self.result_data_Text.grid(row=1, column=26, rowspan=5, columnspan=5)
       
        
        #开始抓取按钮
        self.copy_calculate_btn = Button(self.init_window_name, text="开始抓取", bg="lightblue", 
        width=20,command=self.copy_calculate_func)# 调用内部方法  加()为直接调用
        self.copy_calculate_btn.grid(row=26, column=0, rowspan=5)

        self.copy_enable = True

    #分类回调函数
    def copy_calculate_func(self):
        if self.copy_enable == False:
            return
        self.copy_enable = False
        self.result_data_Text.delete('0.0','end')
        try:
            res_link = self.init_data_Text.get('0.0','end')
            print("res link  is ", res_link)
            if res_link==None or res_link=="":
                print("res link is empty")
                return
            threadPool.submit(save_res, res_link)
        except Exception as e:
            print("exception is ", repr(e))
        finally:
            self.result_data_Text.delete('0.0','end')
            self.init_data_Text.delete('0.0','end')

def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MyGui(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

# res_data ResData
# res_link表示资源链接
def save_res(res_link):
    driver.get_url(res_link)
    driver.cycleScroll()
    #实例化session
    # session = requests.session()
    # req_header = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    #     Chrome/75.0.3770.100 Safari/537.36',
    # }
    
    #response = session.get(res_link, headers=req_header)
    #print(response.text)
    #response = session.get('https://app.poizon.com/api/v1/h5/index/fire/flow/product/detail',headers=req_header)
    #print(response.text)
    return 'finished'

class SeleniumDriver(object):
    def __init__(self):
        options = webdriver.ChromeOptions() 
        options.add_argument('--ignore-certificate-errors') 
        options.add_argument('--ignore-ssl-errors') 

        self.driver_ = webdriver.Chrome(chrome_options=options)
        self.path=os.path.dirname(os.path.abspath(__file__))
        now = datetime.now()
        timestr=now.strftime('%Y%m%d')
        self.path=os.path.join( self.path,timestr)
        if os.path.exists(self.path)==False:
            os.mkdir(self.path)
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
                print(list_infos)
        except NoSuchElementException:
            print('No Element')
        except TimeoutException :
            print('TimeoutException')
        except Exception as e:
            print('cycleScroll exception!!!! error is ', e)    

if __name__ == "__main__":
    #web driver
    driver = SeleniumDriver()
    print(driver.getcrollTop())
    print(driver.getbottomHeight())

    #启动线程池
    threadPool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="saveres_")
    #启动图形库
    gui_start()
    #关闭线程池
    threadPool.shutdown(wait=True)