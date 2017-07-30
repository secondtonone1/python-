#-*-coding:utf-8-*-
import time
import functools
'''
it = map(lambda x:x*x, (1,3,5,7,9))
print(list(it))

def lazy_squart():
	return lambda x:x*x
f = lazy_squart()
print(f(3) )
'''
'''
def decoratorfunc(func):
	def wrapperfunc():
		print('func name is: %s'%(func.__name__))
		func()
	return wrapperfunc


def helloword():
	print('Helloworld !!!')

helloword = decoratorfunc(helloword)
helloword() 
'''

'''
def decoratorfunc(func):
	def wrapperfunc():
		print('func name is: %s'%(func.__name__))
		func()
	return wrapperfunc
@decoratorfunc
def helloword():
	print('Helloworld !!!')

helloword()
'''

#带参数的
'''
def decoratorfunc(func):
	def wrapperfunc(*args, **kw):
		time1 = time.time()
		func(*args, **kw)
		time2 = time.time()
		print('cost %d secondes'%(time2-time1))
	return wrapperfunc


@decoratorfunc
def output(str):
	print(str)
	time.sleep(2)

output('hello world!!!')
'''
#相当于
# output = decoratorfunc(output)
# output('hello world!!!')


#装饰器需要传递参数
'''
def decoratorfunc(param):
	def decoratorfunc(func):
		def wrapperfunc(*arg, **kw):
			print('%s %s' %(param, func.__name__))
			func(*arg, **kw)
		return wrapperfunc
	return decoratorfunc

@decoratorfunc('execute')
def output(str):
	print(str)

output('nice to meet u')
print(output.__name__)
'''
#实际执行过程
#decorator = decoratorfunc('execute')
#output = decorator(now)

#output('nice to meet u')


#函数名字变了，可以在装饰器中调用python提供的api设置
'''
def decoratorfunc(param):
	def decoratorfunc(func):
		@functools.wraps(func)
		def wrapperfunc(*arg, **kw):
			print('%s %s' %(param, func.__name__))
			func(*arg, **kw)
		return wrapperfunc
	return decoratorfunc

@decoratorfunc('execute')
def output(str):
	print(str)

print(output.__name__)
'''

#偏函数

intnew = functools.partial(int, base = 2)
print(intnew('100'))

def add(a,b):
	return a+b
print(add(3,7))

addnew = functools.partial(add, 3)
print(addnew(7))

addnew2 = functools.partial(add, b = 7)
print(addnew2(3))



