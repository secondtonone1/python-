#-*-coding:utf-8-*-

'''
批量爬去豆瓣租房小组信息
'''

import re,os,random
from urllib import request, parse
from datetime import datetime
from urllib import error

from urllib.parse import quote
import string

import time, threading

import http.client  
  
http.client.HTTPConnection._http_vsn = 10  
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

contents=""
def requestData(url, user_agent):
	global contents
	try:
		req = request.Request(url)
		req.add_header('User-Agent', user_agent)
		response = request.urlopen(req,timeout = 8)
		#bytes变为字符串
		contents = response.read().decode('utf-8')
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
	return contents
	
def workthread(item, user_agent,path):
	strurl = item[0]
	picname = item[1]
	dirname = re.search(r'www.douban.com/group/topic/(.*?)/',strurl).group(1)
	print('正在爬取%s...........................\n' %(picname))
	content = requestData(strurl,user_agent)
	httpstr = r'<div class="tabs".*?>.*?<a href="(.*?)#sep'
	httppattern = re.compile(httpstr,re.S)
	patternstr = r'<div class="topic-content">(.*?)<div class="sns-bar" id="sep">'
	pattern =re.compile(patternstr , re.S )
	patterncontent = re.findall(pattern,content)
	if(len(patterncontent)==0 ):
		print('no content\n')
		return
	httpcontent = re.findall(httppattern,content)
	dirname = os.path.join(path,dirname);
	if(os.path.exists(dirname)==False):
		os.makedirs(dirname)
	filetxt = "file.txt"
	filename = os.path.join(dirname,filetxt)
	if(os.path.exists(filename)):
		os.remove(filename)
	replacedStr = re.sub(r'<div.*?>|<p.*?>|<img.*?>|</p>|\n|<span style.*?>|</span>|<iframe.*?>|</iframe>|</div.*?>', r'\n', patterncontent[0])
	with open(filename,'a',encoding='utf-8') as file:
		file.write(httpcontent[0]+'\n')
		file.write(item[1]+'\n')
		file.write(replacedStr+'\n')

	##生成图片
	picstr=r'<div class="image-wrapper"><img src="(.*?)"'
	piccontent = re.findall(picstr,patterncontent[0])
	for i in piccontent:
		lastindex=i.rfind('/')
		if(lastindex==-1):
			continue
		picture = i[lastindex+1:]
		picturename = os.path.join(dirname,picture)
		if(os.path.exists(picturename)):
			os.remove(picturename)
		print('正在爬取%s...........................\n' %(picture))
		req = request.Request(i)
		req.add_header('User-Agent',USER_AGENT)
		try:
			response = request.urlopen(req,timeout = 8)
			picdata =response.read()
			with open(picturename,'wb') as file:
				file.write(picdata)
			time.sleep(random.randint(1,2))
		except Exception :
			print("error code ")
		print('爬取成功%s...........................\n' %(picture))
	print('%s数据爬取成功！！！\n' %(picname))
	



class GetMMPic(object):
	def __init__(self,path):
		# 去除首位空格
		path = path.strip()
		# 去除尾部 \ 符号
		path = path.rstrip('\\')

		self.path = path
		self.url = 'https://www.douban.com/group/sofamap/'
		self.user_agent = USER_AGENT
    	
	def makedir(self,dirname):
		joinpath = os.path.join(self.path,dirname)
		print(joinpath)
		isExists = os.path.exists(joinpath)
		if isExists:
			print('目录已经存在\n')
			return joinpath
		else:
			os.makedirs(joinpath)
			print('创建成功\n')
			return joinpath

	def setpath(self,path):
		self.path = path

	def getDetailList(self,content):
		patternstr = r'<td class="title">.*?<a href="(.*?)" title="(.*?)" class='
		filetemp ='file.txt'
		itempattern =re.compile(patternstr , re.S )
		result = re.findall(itempattern, content)
		if not result:
			print('匹配规则不适配..............')
		#print('匹配条目:%s' %(result))
		filepathtemp = os.path.join(self.path,filetemp);
		with open(filepathtemp,'w',encoding='utf-8') as f:
			for item in result:
				f.write(item[1]+'\n');
				f.write(item[0]+'\n');
		threadsList=[] 
		for item in result:
			#t = threading.Thread(target = workthread, args=(item, self.user_agent, self.path))
			#threadsList.append(t)
			#t.start()
			workthread(item, self.user_agent,self. path);
			pass
			
			
		for threadid in threadsList:
		 	threadid.join()		

		
	def getAbstractInfo(self):
		
		try:
			contenta = requestData(self.url, self.user_agent)
			self.getDetailList(contenta)
				
		except error.HTTPError as e:
			if hasattr(e,'code'):
				print(e.code)
			if hasattr(e,'reason'):
				print(e.reason)
			print('HTTPError!!!')
		except error.URLError as e:
		 	if hasattr(e,'code'):
		 		print (e.code)
		 	if hasattr(e,'reason'):
		 		print (e.reason)



if __name__ == "__main__":
	#getMMPic = GetMMPic('D:/python/args')
	filepath = os.path.abspath(__file__)
	getMMPic = GetMMPic(os.path.dirname(filepath))
	now = datetime.now()
	timestr=now.strftime('%Y%m%d')
	todaypath = getMMPic.makedir(timestr)
	if  todaypath:
		getMMPic.setpath(todaypath)
		getMMPic.getAbstractInfo()
	

	
    
