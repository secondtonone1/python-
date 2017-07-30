#-*-coding:utf-8-*-
from PIL import Image
from collections import Iterable
from collections import Iterator
import argparse

L=['a','b','c','d','e','f']
#取索引0，到索引3的元素，不包括索引3
print(L[0:3])
#开始索引为0可以省略
print(L[:3])
#下标1到3
print(L[1:3])
#取最后一个元素
print(L[-1])
#取倒数后两个元素
print(L[-2:])
#取前四个数，每两个取一个
print(L[:4:2])
#所有数，每两个取一个
print(L[::2])

dictor = {'name':'Jul','age':17,'femail':1}
#迭代key
for key in dictor:
	print(key)	
#迭代value
for value in dictor.values():
	print(value)
#迭代key,value
for k,v in dictor.items():
	print(k,v)

result = isinstance(dictor,Iterable)
print(result)

for x,y in [(1,2),(3,4),(5,6)]:
	print(x,y)
#变为索引元素对
for i,value in enumerate(['A','B','C']):
	print(i,value)
#平方
print([x*x for x in range(1,11)])
#偶数平方
print([x*x for x in range(1,11) if x%2 ])
#k:v形式的列表
strdic={'a':'a1','b':'b1','c':'c1'}
print([k+':'+v for k,v in strdic.items()])
#将列表中字符串换为小写
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if(isinstance(s,str)) ])

g = (x*2 for x in range(1,11))
print(g)
print(next(g))

#菲波那切数列
def fib(max):
	a,b,n = 0,1,0
	while n < max:
		yield b
		a,b=b,a+b
		n = n+ 1
	return "exit"

g=fib(2)
print(g)
print(next(g))
print(next(g))
#print(next(g))

g2 = fib(6)

while True:
	try:
		value = next(g2)
		print("value: ", value)
	except StopIteration as e:
		print("Generator return value is: ", e)
		break

def triangles():
	yield [1]
	yield [1,1]
	lists = [1,1]
	while True:
		i = 1
		n = len(lists)
		newlists = [1]
		while i < n:
			newlists.append(lists[i-1] + lists[i])
			i = i+1
		newlists.append(1)
		lists = newlists
		yield newlists	

	
n = 0
for t in triangles():
	print(t)
	n = n+1
	if n==10:
		break

b1 = isinstance([], Iterable)
b2 = isinstance([], Iterator)
print('[] is Iteralbe', b1)
print('[] is Iterator', b2)



b1 = isinstance({},Iterable)
b2 = isinstance({},Iterator)

print('[] is Iteralbe', b1)
print('[] is Iterator', b2)

b1 = isinstance((x*x for x in range(10)), Iterable)
b2 = isinstance((x*x for x in range(10)), Iterator)
print('x*x for x in range(10) isIterable', b1)
print('x*x for x in range(10) isIterator', b2)

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

b1 = isinstance(triangles(),Iterable)
b2 = isinstance(triangles(),Iterator)
print('triangles()', b1)
print('triangles()', b2)

#python 特性
f = abs
print(f(-10))
f = 'abs'
print(f)

it = iter([1,3,5,7,9])

while True:
	try:
		print(next(it))
	except StopIteration as e:
		print("StopIteration")
		break