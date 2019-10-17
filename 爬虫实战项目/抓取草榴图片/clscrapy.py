#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory, askopenfilename
import threading, time, re, os, requests, math
import time
import datetime

#https://cc.vttg.pw/htm_data/1909/7/3663612.html
#https://cc.vttg.pw/htm_mob/1910/7/3674908.html

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
HEADERS = {'User-Agent':USER_AGENT,}
def thread_run(func):
    def wraper(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()

    return wraper

class BasicFrame(object):
    """Frame基类，实现grid方法"""

    def __init__(self, root=None, **args):
        super(BasicFrame, self).__init__()
        self.root = None
        if root:
            self.root = tk.Frame(root)
        if args and 'root' in args.keys:
            self.root = tk.Frame(args.root)

        if not self.root:
            raise Exception("no root")

    def grid(self, row='default', column='default', **args):
        if row == 'default' or column == 'default':
            if args:
                self.root.grid(**args)
        else:
            self.root.grid(row=row, column=column)


class DownloadFrame(BasicFrame):
    """docstring for SearchFrame"""

    def __init__(self, root=None, **args):
        super(DownloadFrame, self).__init__(root=root, **args)
        self.entry = tk.StringVar()
        self.cnt = 0
        self.num = tk.StringVar()
        self.num.set(300)
        self.name = 0
        self.flag = False

        row = 0

        tk.Label(self.root, text='----请输入要下载的免翻地址---').grid(row=row, column=1)

        row += 1
        tk.Label(self.root,width=10, justify='right' ,text='地址').grid(row=row, column=0)
        tk.Entry(self.root, textvariable=self.entry, width=24).grid(row=row, column=1)
        tk.Button(self.root, width=9,text='下载图片', command=self.downloadnow).grid(row=row, column=2)


        row += 1

        tk.Label(self.root,   text='---代理功能更新中---').grid(row=row, column=1)


    @thread_run
    def downloadnow(self):
        _input = self.entry.get().replace(' ', '')

        if self.flag:
            messagebox.showinfo("警告", "尚有后台下载任务进行中")
        elif _input == ''  :
            messagebox.showinfo("警告", "链接不能为空")
        else:
            self.entry.set('')
            self.prepare(_input)

    def prepare(self, downloadlinks):
        self.flag = True
        self.downloadlinks = downloadlinks
        self.base_url =   self.downloadlinks

        fail = 0

        try:
            url = self.base_url
            result = requests.get(url, headers=HEADERS,timeout=10)
            restxt = result.content.decode('gbk')            
            pic_url = re.findall("data-src='(.*?)'", restxt, re.S)
            print(pic_url)
            titles = re.findall('<title>(.*?)</title>',  restxt, re.S)
            title = ''
            if titles == None or len(titles) == 0:
                title = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                pass
            else:
                title = titles[0]
            titlelist = re.split(r'[;,\s]',title)
            title = titlelist[0]
            print(title)
            curdir = os.path.dirname(os.path.abspath(__file__))
            picpath = os.path.join(curdir,title)
            if not os.path.exists(picpath):
                os.mkdir(picpath)

            if len(pic_url) == 0:
                fail += 1
            else:
                self.downloadPic(pic_url, picpath)
        except Exception as e:
            print(e)
            time.sleep(3)


        # print("图片下载完成")

    def downloadPic(self, urls, path):

        # 每过三秒检查一次当前正在运行的线程数，超标则沉睡等待线程结束
        '''
        while threading.activeCount() > 5:
            print("线程超标---%s" % threading.activeCount())
            time.sleep(3)
        '''
        for url in urls:
            if url:
                print(url)
                self.download(url, path)


    @thread_run
    def download(self, url, path):
        try:
            if lock.acquire():
                self.name += 1
                imgname = str(self.name)+'.'+url.split('.')[-1]
                filename = os.path.join(path,imgname)
                lock.release()
                print(url)
                print(filename)
                # res = requests.get(url,  headers=header  )
                res = requests.get(url, headers=HEADERS,timeout=10 )
                with open(filename, 'wb') as f:
                    f.write(res.content)
            # 下载完后检查是否完成下载
            if lock.acquire():
                  if self.flag:
                    self.flag = False
                    messagebox.showinfo("提示", "下载完成")

        except Exception as e:
            print(e)
            if lock.acquire():
                self.cnt -= 1
                lock.release()



if __name__ == '__main__':
    lock = threading.Lock()
    root = tk.Tk()
    root.title("草榴社区图片下载器免翻墙版 -- mooncoder")
    root.geometry('440x150+600+200')
    root.resizable(False, False)

    downloadnow = DownloadFrame(root)
    downloadnow.grid(0, 0)


    tk.Label(text="created BY mooncoder").grid(row=2, column=0)

    root.mainloop()