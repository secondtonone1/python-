#-*-coding:utf-8-*-
from multiprocessing import Process
import os

import re
s = 'AB\\-001'
print(s)
s = r'AB\-001'
print(s)

import re
result = re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print(result)
result2 = re.match(r'^\d{3}\-\d{3,8}$','010 12345')
print(result2)
#切串
s1 = 'a b   c'
print(s1.split(' ') )
s2 = re.split(r'\s+', s1)
print(s2)
s3 = re.split(r'[\s\:\,]+','a,b  c::d e, f')
print(s3)
#分组
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

#贪婪匹配
r1 = re.match(r'^(\d+)(0*)$','102300').groups()
print(r1)
r2 = re.match(r'^(\d+?)(0*)$','102300').groups()
print(r2)
#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
r3 = re_telephone.match('010-12345').groups()
print(r3)
r4 = re_telephone.match('043-12345').groups()
print(r4)

pattern = re.compile(r'hello')
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo, aaa')
result3 = re.match(pattern, 'helo AAB')
result4 = re.match(pattern, 'helloww')

if result1:
	print(result1 )
else:
	print('failed!!!')

if result2:
	print(result2.group() )
else:
	print('failed!!!')

if result3:
	print(result3.group() )
else:
	print('failed!!!')

if result4:
	print(result4.group() )
else:
	print('failed!!!')

res = re.match(r'(hello)','hellooaaa')
if res:
	print(res.groups())
else:
	print('failed!!!')

'''
1.string: 匹配时使用的文本。
2.re: 匹配时使用的Pattern对象。
3.pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
4.endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
5.lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
6.lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
方法：
1.group([group1, …]):
获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；
不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
2.groups([default]):
以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
3.groupdict([default]):
返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
4.start([group]):
返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
5.end([group]):
返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
6.span([group]):
返回(start(group), end(group))。
7.expand(template):
将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。\id与\g是等价的；
但\10将被认为是第10个分组，如果你想表达\1之后是字符’0’，只能使用\g0。
'''

#匹配：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P<sign>.*)','hello world!')

print('m.string is %s' %(m.string) )
print('m.re: %s' %(m.re) )
print('m.pos: %d' %(m.pos))
print('m.endpos: %d' %(m.endpos))
print('m.lastindex: %d' %(m.lastindex))
print('m.lastgroup: %s' %(m.lastgroup))
print('m.groups: ' , m.groups())
print('m.group: ' , m.group())
print('m.group(1,2): ' , m.group(1,2))
print('m.groupdict():', m.groupdict())
print('m.start(2):',m.start(2))
print('m.end(2):',m.end(2))
print('m.span(2):',m.span(2))
print("m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3') )

import re
pattern = re.compile(r'world')
sr = re.search(pattern, 'hello world!')
if sr:
	print(sr.group())

pattern = re.compile(r'\d+')
splitrs = re.split(pattern, 'one1two2three3four45six797five')
if sr:
	print(splitrs)

pattern = re.compile(r'\d+')
find = re.findall(pattern, 'one1two2three3four45six797five')
if find:
	print(find)

pattern = re.compile(r'\d+')
finditer = re.finditer(pattern, 'one1two2three3four45six797five')
if(finditer):
	print(finditer)
	for m in finditer:
		print(m.group())


pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world'
print(re.sub(pattern,r'\2 \1', s))

def func(m):
	return m.group(1).title() + ' '+ m.group(2).title()

sub = re.sub(pattern, func, s)
print(sub)


pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world'
print(re.subn(pattern,r'\2 \1', s))

def func(m):
	return m.group(1).title() + ' '+ m.group(2).title()

sub = re.subn(pattern, func, s)
print(sub)

