#-*-coding:utf-8-*-
#函数的定义
def judgeint(x):
	if not isinstance(x,(int)):
		raise TypeError('类型不匹配')
	else:
		return x

def abs_(x):
	if not isinstance(x,(int, float)):
		raise TypeError('类型不匹配')
	elif x > 0:
		return x
	else: 
		return -x
#空函数
def emptyfun(x):
	pass
#多个返回值
def getposition(x,y):
	return x, y
#位置参数
def power(x):
	return x*x
#默认参数
def power(x,n = 2):
	imul =1
	while(n > 0):
		imul = x*imul
		n = n-1
	return imul
#默认参数
def getinfo(name, age, sex, city="北京"):
	return name,age,sex,city
#默认参数需要指向不可变对象，否则会出现默认参数随着
#函数调用导致变化
def getList(L=[]):
	L.append("end")
	return L

def getList2(L = None):
	if L is None:
		L = []
		return L.append("end")
	else:
		return L.append("end")


def calsum(*nums):
	sum = 0
	for i in nums:
		sum = sum+ i
	return sum


def getinfo2(name, age, **info):
	print("姓名：", name, "年龄：", age, "其他信息:", info)

def getinfo3(name,age,**info):
	if 'city' in info:
		print("有城市信息")
	if 'job' in info:
		print("有工作记录")
	print("姓名：", name, "年龄：", age, "其他信息:", info)


def getinfo8(name, age, *,city, job):
	print("姓名：", name, "年龄：", age, "城市:", city, "工作：", job)
def getinfo7(name, age, *infolist, city, job):
	print("姓名：", name, "年龄：", age, "城市:", city, "工作：", job, "其他信息:", infolist)

def getinfo4(name, age,*,city='沈阳',job):
	print("姓名：", name, "年龄：", age, "城市:", city, "工作：", job)
#参数混用 位置参数，默认参数，可变参数，命名关键字参数，关键字参数
def getinfo5(name,age,city='沈阳',**info):
	print("姓名：", name, "年龄：", age, "城市:", city, "其他信息:", info)
def getinfo6(name,age,city='沈阳',*infolist ,health = '良好', job,**otherinfo):
	print("姓名：", name, "年龄：", age, "城市:", city, '工作信息：',job,'\n',
		"身体状况", health, "个人备注",infolist,'\n',
		"其他信息:", otherinfo)
	

#递归计算阶乘函数
def imul2(num=1):
	if num ==1:
		return num
	else:
	    return num * imul2(num-1)
#编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
def move(n,A,B,C):
	if n==1:
		print("%s --> %s" %(A,C))
		return
	else:
		move(n-1,A,C,B)
		move(1,A,B,C)
		move(n-1,B,A,C)