#-*-coding:utf-8-*-
str1 = 'this is a string'
#每个单词首字母大写
print(str1.title())
#全部大写
print(str1.upper())
#全部小写
print(str1.upper().lower())
#拼接字符串
firstname = 'wang'
lastname = 'wc'
fullname = firstname +' '+ lastname
print(fullname)
print(fullname.title())
#重复输出字符串
print(fullname*2)
#输出某个位置的字符
print(fullname[3])
#截取某一段字符串,索引1到3
print(fullname[1:4])
if('w' in firstname):
	print('w in %s'%(firstname))
if('W'not in firstname):
	print('W not in %s'%(firstname))
#转化为二进制字节
namebytes = fullname.encode(encoding='utf-8',errors='strict')
print('encoding utf-8 %s'%(namebytes))
#转化为unicode string
namestr = namebytes.decode(encoding='utf-8',errors='strict')
print('decode utf-8 %s'%(namestr))
#index 查找某个字符串在字符串中的位置，没有则返回异常
try:
	namestr.index('s',0,len(fullname))
except:
	print("'s' is not in %s" %(fullname))
#find 查找字符串在字符串中的位置，没有则返回-1
findindex = namestr.find('s',0,len(fullname))
print('findindex %d'%(findindex))
findindex = namestr.find('wc',0,len(fullname))
print('findindex %d'%(findindex))

