#-*-coding:utf-8-*-

import re,os
from urllib import request, parse
from datetime import datetime
from urllib import error

class GetMMPic(object):
	def __init__(self,path):
		# 去除首位空格
		path = path.strip()
		# 去除尾部 \ 符号
		path = path.rstrip('\\')

		self.path = path
		self.url = 'http://yxpjw.club/luyilu/'
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    	
	def makedir(self,dirname):
		joinpath = os.path.join(self.path,dirname)
		print(joinpath)
		isExists = os.path.exists(joinpath)
		if isExists:
			print('目录已经存在\n')
			return False
		else:
			os.makedirs(joinpath)
			print('创建成功\n')
			return True


	def getDetailPic(self, item):
		strurl = 'http://yxpjw.club'+item[0]
		print(strurl)
		picname = item[1]
		print('正在爬取%s...........................\n' %(picname))
		print('%s数据爬取成功！！！\n')

	def getDetailList(self,content):
		pattern =re.compile(r'<h2><a target="_blank" href="(.*?)"'\
			+r'title="(.*?)">', re.S
			)
		#uf-8编码方式打开
		file = open('file.txt', 'w',encoding='gbk')

		file.write(content)

		file.close()

		result = re.findall(pattern, content)
		if not result:
			print('匹配规则不适配..............') 
		for item in result:
			self.getDetailPic(item)

	def getAbstractInfo(self):
		
		try:
			req = request.Request(self.url)
			req.add_header('User-Agent', self.user_agent)
			response = request.urlopen(req)
			#bytes变为字符串
			content = response.read().decode('gbk')
			self.getDetailList(content)
			
		except error.URLError as e:
			if hasattr(e,'code'):
				print (e.code)
			if hasattr(e,'reason'):
				print (e.reason)
		except error.HTTPError as e:
			print('HTTPError!!!')




if __name__ == "__main__":
	#getMMPic = GetMMPic('D:/python/args')
	#getMMPic = GetMMPic('./')
	#now = datetime.now()
	#timestr=now.strftime('%Y%m%d')
	#getMMPic.getAbstractInfo()

	

	s1 = r'<p><img src="(.*?)"'
	s2 = r'http://images.zhaofulipic.com:8818/allimg/.*?/(.*?)$'
	s3 = r'''<li class='next-page'><a target="_blank" href='(.*?)'>下一页'''

	pattern1 =re.compile(s1, re.S)
	pattern2 = re.compile(s2, re.S)
	pattern3 = re.compile(s3, re.S)

	with open('[Tpimage]No.649期极品少妇Mira无圣光套图[56P].txt','r', encoding='gbk') as f:
		data = f.read()


	result = re.findall(pattern1, data)

	
	
	for rs in result:
		
		picname1 = re.search(pattern2,rs)
		picname = picname1.group(1)
		
		req = request.Request(rs)
		

		req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
		response = request.urlopen(req)
		picdata =response.read()
		
		with open(picname,'wb') as file:
			file.write(picdata)
	
	result3 = re.search(pattern3, data)	
	
	nextpage = 'http://yxpjw.club/'+result3.group(1)
	print(nextpage)
	req = request.Request(nextpage)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
	response = request.urlopen(req)
	nextdata = response.read()	
	
	
		

	
	

	
	
    
