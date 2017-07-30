#-*-coding:utf-8-*-
nums = (0,100,34,50,179,130,27,22)
print("nums are:", nums)
bigernums =[]
smallnums = []
for num in nums:
    if num > 50:
        bigernums.append(num)
print("大于50的数字有:", bigernums)
for num in nums:
    if num < 50:
        smallnums.append(num)
print("小于50的数字有:", smallnums)
print(range(5))
print(list(range(5)))
#1~10数字求和
sum = 0
for num in list(range(11)):
	sum += num
print("1到10数字求和结果为:%d" %sum)
#错误输出
#print("1到10数字求和结果为:%d", sum)
#换一种方式求和,while循环注意别写成死循环
i = 0
sum = 0
while i < 11:
	sum += i
	i=i+1#i++不行，习惯了C++
print("1到10数字求和结果为:%d" %sum)

