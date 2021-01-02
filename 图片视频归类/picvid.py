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

class MyGui(object):
    def __init__(self,init_window_name):
        self.init_window_name=init_window_name

    def set_init_window(self):
        self.init_window_name.title("图片视频归类工具")
        self.init_window_name.geometry('540x320+10+10')
        self.init_data_label = Label(self.init_window_name, text="源文件夹地址")
        self.init_data_label.grid(row=0, column=0)
        self.to_label = Label(self.init_window_name, text="分类到")
        self.to_label.grid(row=0, column=12)

        self.result_data_label = Label(self.init_window_name, text="目的文件夹地址")
        self.result_data_label.grid(row=0, column=20)
        
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=30, height=10)  #源文件夹地址
        self.init_data_Text.grid(row=1, column=0, rowspan=5, columnspan=5)
        self.result_data_Text = Text(self.init_window_name, width=30, height=10)  #目的文件夹地址
        self.result_data_Text.grid(row=1, column=20, rowspan=5, columnspan=5)
       
        self.select_src_dir_btn = Button(self.init_window_name, text="选择源文件夹", bg="lightblue", 
        width=10,command=self.select_src_dir_func)# 调用内部方法  加()为直接调用
        self.select_src_dir_btn.grid(row=20, column=0, rowspan=5)

        self.select_dest_dir_btn = Button(self.init_window_name, text="选择目标文件夹", bg="lightblue", 
        width=15,command=self.select_dest_dir_func)# 调用内部方法  加()为直接调用
        self.select_dest_dir_btn.grid(row=20, column=20, rowspan=5)

        self.copy_calculate_btn = Button(self.init_window_name, text="分类到不同文件夹", bg="lightblue", 
        width=20,command=self.copy_calculate_func)# 调用内部方法  加()为直接调用
        self.copy_calculate_btn.grid(row=26, column=0, rowspan=5)

        self.copy_enable = True

    #源文件按钮回调函数
    def select_src_dir_func(self):
        self.init_data_Text.delete('0.0','end')
        self.src_dir = askdirectory()
        print("src dir is ",self.src_dir)
        self.init_data_Text.insert('end',self.src_dir)
        
    #目标文件按钮回调函数
    def select_dest_dir_func(self):
        self.result_data_Text.delete('0.0','end')
        self.dest_dir = askdirectory()
        print("dest dir is ",self.dest_dir)
        self.result_data_Text.insert('end',self.dest_dir)
        pass

    #分类回调函数
    def copy_calculate_func(self):
        if self.copy_enable == False:
            return
        self.copy_enable = False
        try:
            for file_name in os.listdir(self.src_dir):
                print("resource name is ", file_name)
                name, ftype = os.path.splitext(file_name)
                ftype = ftype.lower()
                if ftype != '.jpg' and ftype != '.jpeg' and ftype != '.avi' and ftype != '.png' and ftype != '.mp4' and ftype != '.wmv' and ftype != '.mov':
                    print("file type error , ftype is", ftype)
                    continue
                res_data = ResData(res_src=self.src_dir, res_dest=self.dest_dir, res_name=file_name)
                future = threadPool.submit(save_res,res_data)
                print("future res is" ,future.result())
        except Exception as e:
            print("exception is ", repr(e))
        finally:
            self.copy_enable = True

def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MyGui(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

#图片或者资源信息
class ResData(object):
    def __init__(self,* , res_src, res_dest, res_name):
        #源路径
        self.res_src = res_src
        #目的路径  
        self.res_dest = res_dest
        #资源名称
        self.res_name = res_name

# res_data ResData
def save_res(res_data):
    print("%s threading is printed %s"  %(threading.current_thread().name, res_data.res_name))
    src_path = os.path.join(res_data.res_src, res_data.res_name)
    
    print(src_path)
    # 利用文件读写字节流实现复制
    '''
    with open(src_path, 'rb') as f:
        read_file = f.read()
        print("图片拍摄时间：", img_exif.get('EXIF DateTimeOriginal'))
        with open(dest_path, 'wb') as wf:
            wf.write(read_file)
    '''

    #获取文件exfi信息
    fifo = os.stat(src_path)
    m_time = fifo.st_mtime
    time_local = time.localtime(m_time)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m", time_local)
    dest_path = os.path.join(res_data.res_dest, dt)
    isExists=os.path.exists(dest_path)
    if isExists == False:
        os.makedirs(dest_path)
    dest_path = os.path.join(dest_path, res_data.res_name)
    if os.path.exists(dest_path) == False:
        copyfile(src_path, dest_path)
    return 'finished'

if __name__ == "__main__":
    #启动线程池
    threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="saveres_")
    #启动图形库
    gui_start()
    #关闭线程池
    threadPool.shutdown(wait=True)