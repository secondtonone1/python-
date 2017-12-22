#-*-coding:utf-8-*-
'''
输入宅福利单个文章地址，爬取内容
如：http://yxpjw.club/luyilu/2017/1205/4295.html
'''
import re,os,random
from urllib import request, parse
from datetime import datetime
from urllib import error

import time, threading

import urllib.request
import random

import http.client  
  
http.client.HTTPConnection._http_vsn = 10  
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
PATTERN1 = r'<meta property="og:title" content="(.*?)"/'
PATTERN2 = r'<p><img src="(.*?)"'
PATTERN3 = r'''<li class='next-page'><a target="_blank" href='(.*?)'>下一页'''
PATTERN4 = r'^(.*)/'
PATTERN5 = r'^.*/(.*?)$'

class GetMMPic(object):
	def __init__(self,path,httpstr):
		# 去除首位空格
		path = path.strip()
		# 去除尾部 \ 符号
		path = path.rstrip('\\')
		self.path = path
		self.url = httpstr
		self.user_agent = USER_AGENT

	def requestData(self,url, user_agent):
		try:
			req = request.Request(url)
			req.add_header('User-Agent', user_agent)
			response = request.urlopen(req,timeout = 3)
			#bytes变为字符串
			content = response.read().decode('gbk')
			return content
		except error.URLError as e:
			if hasattr(e,'code'):
				print (e.code)
			if hasattr(e,'reason'):
				print (e.reason)
		except error.HTTPError as e:
			if hasattr(e,'code'):
				print(e.code)
			if hasattr(e,'reason'):
				print(e.reason)
			print('HTTPError!!!')

    	
	def makedir(self,dirname):
		joinpath = os.path.join(self.path,dirname)
		print(joinpath)
		isExists = os.path.exists(joinpath)
		if isExists:
			print('目录已经存在\n')
			return None
		else:
			os.makedirs(joinpath)
			print('创建成功\n')
			return joinpath

	def setpath(self,path):
		self.path = path

	
	def getPageData(self,httpstr):

		headpattern = re.compile(PATTERN4,re.S)
		headrs = re.search(headpattern,httpstr)
		headstr = headrs.group(0)

		print('headstr....%s' %(headstr))
		content = self.requestData(self.url, self.user_agent)
		namepattern = re.compile(PATTERN1,re.S)
		nameresult = re.search(namepattern, content)
		namestr = nameresult.group(1)
		dirpath = self.makedir(namestr)
		if not dirpath:
			print('目录已存在')
			return
		picpattern = re.compile(PATTERN2,re.S)
		nextpagepattern = re.compile(PATTERN3,re.S)
		lastpattern = re.compile(PATTERN5, re.S)
		pageindex = 1
		while(1):
			print('正在爬取第%d页......' %(pageindex))
			picitems = re.findall(picpattern,content)
			for item in picitems:
				picrs = re.search(lastpattern, item)
				picname = picrs.group(1)
				filedir = os.path.join(dirpath,picname)
				#print(dirpath)
				#print(filedir)
				print(item)
				#print(picname)
				req = request.Request(item)
				req.add_header('User-Agent',USER_AGENT)
				response = request.urlopen(req)
				picdata =response.read()
				with open(filedir,'wb') as file:
					file.write(picdata)
				time.sleep(random.random())
				
			
			nextrs = re.search(nextpagepattern, content)
			if not nextrs:
				print('\n%s爬取成功.......'%(namestr))
				break
			nextstr = headstr+nextrs.group(1)
			content = self.requestData(nextstr, self.user_agent)
			print('第%d页爬取成功......' %(pageindex))
			pageindex = pageindex + 1
			print('next page is : %s' %(nextstr))



if __name__ == "__main__":
	print('请输入网页地址：...\n')
	httpstr = input()
	getMMPic = GetMMPic('./',httpstr)
	getMMPic.getPageData(httpstr)
	
    
