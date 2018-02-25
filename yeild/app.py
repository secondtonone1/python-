#-*-coding:utf-8-*-

def getnum(maxnum):
	beginindex = 0
	while beginindex < maxnum:
		yield beginindex
		beginindex += 1

genorator = getnum(10)
print(next(genorator))
print(next(genorator))

for i in genorator:
	print(i)
	pass


#复习菲波那切数列
def fib(maxnum):
	index = 0
	a,b=0,1
	while index < maxnum:
		yield b
		a,b = b, a+b
		index += 1

for i in fib(10):
	print(i)


import time

#融入携程send
def lazy_fib(maxnum):
	index = 0
	a,b = 0,1
	while index < maxnum:
		sleeptime = yield b
		if sleeptime is None:
			sleeptime = 0.3
		print('sleep time is %f' %(sleeptime))
		time.sleep(sleeptime)
		a,b = b,a+b
		index += 1


import random
lfib = lazy_fib(10)
fibnum = next(lfib)
while True:
	print(fibnum)
	try:
		fibnum = lfib.send(random.uniform(0,0.5))
	except StopIteration:
		break


def jumping_range(up_to):
	index = 0
	while index < up_to:
		jump = yield index
		if jump is None:
			jump = 1
		index += jump


if __name__ == '__main__':
	iterator = jumping_range(5)
	print(next(iterator))
	print(iterator.send(2))
	print(next(iterator))
	print(iterator.send(-1))
	for x in iterator:
		print(x)



def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return 
		print('[consumer] consuming %s...' % n)
		r = '200 OK'


def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n+1
		print('[produce] producing %s...' %n)
		r = c.send(n)
		print('[produce] consumer return: %s ' %r)
	c.close()

c = consumer()
produce(c)









