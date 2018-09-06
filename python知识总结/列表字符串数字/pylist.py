#-*-coding:utf-8-*-
programlan = ['C++','python','java','php']
print(programlan)
print(programlan[0])
#将第3个字符串首字母大写
print(programlan[2].title())
#修改第四个元素
programlan[3] = 'C#'
print(programlan)
#末尾加入node.js
programlan.append('node.js')
print(programlan)
#在第二个元素位置插入delphy
programlan.insert(1,'delphy')
print(programlan)
#copy列表中所有元素
programlan2 = programlan[:]
print(programlan2)
#将末尾元素弹出，返回剩下列表
lan = programlan.pop()
print(lan)
#弹出第二个元素
lan = programlan.pop(1)
print(lan)
#删除第二个元素，再不需要使用时效率高于pop
del programlan[1]
print(programlan)
#根据名字remove元素
lan = 'java'
programlan.remove(lan)
print(programlan)
#对列表永久排序
programlan2.sort()
print(programlan2)
#反向排序
programlan2.sort(reverse=True)
print(programlan2)
#temp sort 临时排序
tempsort = sorted(programlan2)
print(tempsort)
print(programlan2)
print(len(programlan2))
#range 产生自然数列生成器，左闭右开
for value in range(1,5):
	print(value)
#将range()结果变为列表
print(list(range(1,5)))
#指定步长，生成偶数数列
even_numbers = list(range(2,11,2))
print(even_numbers)
#列表生成器自动生成
squares = [i**2 for i in range(1,11)]
print(squares)
#切片
strlist = ['li','ss','adf','ww','afdfd']
#取前三元素,从索引为0的开始，取3个
print(strlist[0:3])
#从第二个元素开始，取4个元素
print(strlist[1:4])
#不指定:前索引，则从列表第一个元素开始
print(strlist[:4])
#不指定:后数量，则取出直到列表末尾所有元素
print(strlist[2:])
#:前索引为负数表示从后第n个元素取
#从倒数第三个元素取，直到末尾
print(strlist[-3:])
#遍历切片,取出前三字符串，并title
for element in strlist[:3]:
	print(element.title())
#复制列表
strlist2 = strlist[:]
print(strlist2)
print(strlist)
