#-*-coding:utf-8-*-
import time
import functools


class Chain(object):
    def __init__(self,path=''):
        self._path=path

    def __getattr__(self,path):
        if path=='users':
            return lambda name:Chain('%s/users/%s'%(self._path,name))
        else:
            return Chain('%s/%s'%(self._path,path))

    def __str__(self):
        return self._path

    __repr__=__str__

#print(Chain().users('lidu').repos)

class Chain(object):

    def __init__(self, path='GET '):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self,path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


#print(Chain().users('michael').group('student') )

#Chain().users('michael').group('student').repos
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


#print(Chain().test.temper)
#
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def printinfo(self):
		print('name is %s, score is %d'%(self.name, self.score))

s1 = Student('niuniu',78)
print(s1.name)
print(s1.score)
s1.printinfo()

s2 = Student('gg',100)
s2.printinfo()
s2.age = 100
print('s2 age is %s'%(s2.age))

#print('s1 age is %s' %(s1.age))

class Student2(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def getname(self):
		return self.__name
	def getscore(self):
		return self.__score 

	def printinfo(self):
		print('name is %s, score is %d' %(self.__name, self.__score))


s3 = Student2('s3',99)
s3.printinfo()
name = s3.getname()
print(name)
s3.__name = 'iloveu'
print(s3.__name)
name = s3.getname()
print(name)
s3.printinfo()
#print(s3.__name)


class Peaple(object):
	def __init__(self, name):
		self.__name = name
	def job(self):
		pass

class Worker(Peaple):
	def job(self):
		print("worker")

class Student(Peaple):
	def job(self):
		print("student")

s1 = Student('student')
s1.job

w1 = Worker('worker')
w1.job

p = Peaple("abc")
w = Worker("abc")
s = Student("abc")
'''
print(isinstance(p, Peaple))
print(isinstance(w,Peaple))
print(isinstance(s,Peaple))
print(isinstance(s,Worker))
print(isinstance(p,Student))
'''
class Designer(Worker):
	def __init__(self,name,age):
		self.__name = name
		self.age = age
	def job(self):
		print("Designer")

designer = Designer('David',18) 

#判断类中是否有某个实例
#print(hasattr(designer, 'age') )
#print(hasattr(designer,'job'))
#print(hasattr(designer,'name'))

#设置sex属性，属性值为'female'
setattr(designer, 'sex', 'female')

#print(designer.sex)

#获取job属性，返回值为job函数对象
fn = getattr(designer, 'job')
#调用fn函数
fn()

#通过self变量或者实例自身可以实现实例属性绑定
#在类中直接定义一个变量，这个属性归类所有，类似于C++的static变量。
class Temple(object):
	staticmember = 1000

temp1 = Temple()
#temp1没有自身属性成员staticmember，
#而Temple类含有共享属性
#下面这种方式打印的是类的共有属性
print(temp1.staticmember)
#为实例temp1绑定其自身的成员staticmember
#并且设置数值为2048
temp1.staticmember = 2048
#打印实例变量temp1的属性staticmember
print(temp1.staticmember)
#打印类的共有属性
print(Temple.staticmember)
#删除实例的属性staticmember
del temp1.staticmember
#打印出类共享的属性
print(temp1.staticmember)

from types import MethodType


def setage(self, age):
	self.__age = age
def getage(self):
	return self.__age
###给实例绑定方法
temp1.setage = MethodType(setage, temp1)
temp1.getage = MethodType(getage,temp1)
temp1.setage(125)
print(temp1.getage())

def setname(self, name):
	self.__name = name

def getname(self):
	return self.__name

#给类绑定方法
Temple.setname= setname
Temple.getname = getname

temp2 = Temple()
temp2.setname('name')
print(temp2.getname())



class People:
    def __init__(self,name):
        self.__name = name
    def get_name(self):
        print('calling the get function')
        return self.__name
    def set_name(self,name):
        print('calling the set function')
        self.__name = name
    def del_name(self):
        del self.__name
    name = property(get_name,set_name,del_name)

a = People('libai') 
print(People.name.fget)
print(People.name.fset)
print(People.name.fdel)

class Definetion(object):
	def __init__(self, member):
		self.__member = member
	@property
	def member(self):
		print("call getter")
		return self.__member
	@member.setter
	def member(self, member):
		print("call setter")
		if not isinstance(member,int):
			raise TypeError("member must be int type")
		self.__member = member
	@member.deleter
	def member(self):
		print("call deleter")
		raise AttributeError("Cann't delete member")
definetioner = Definetion(3)
print(definetioner.member)
definetioner.member = 1024
print(definetioner.member)



















