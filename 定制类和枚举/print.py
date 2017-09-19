#-*-coding:utf-8-*-
class Student(object):
    def __init__(self, name):
        self.name =name

student = Student("lilei")
print(student)

##实现定制类
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return ("self name is %s" %(self.name))

student2 = Student("hanmeimei")
print(student2)


class Fib(object):
    def __init__(self):
        self.a , self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a+ self.b
        if self.a > 30:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

class OddNum(object):
    def __init__(self):
        self.num = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.num = self.num +2
        if self.num > 10:
            raise StopIteration()
        return self.num 
    '''
    def __getitem__(self,n):
        temp = 1
        for i in range(n):
            temp += 2
        return temp
    '''
    ## 切片处理

    def __getitem__(self, n):
        if isinstance(n ,int):
            temp =1
            for i in range(n):
                temp +=2
            return temp
        if isinstance(n, slice):
            start = n.start
            end = n.stop
            if start is None:
                start = 0
            tempList = []
            temp = 1
            for i in range(end):
                if i >= start:
                    temp += 2
                    tempList.append(temp)
            return tempList
    def __getattr__(self,attr):
        if attr == 'name':
            return 'OddNum'
        if attr == 'data':
            return lambda:self.num
        raise AttributeError('\'OddNum\' object has no attribute \'%s\'' %attr)
    def __call__(self):
        return "My name is OddNum!!"


for n in OddNum():
    print(n)
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
oddnum = OddNum()
print(oddnum[3])

print(oddnum[1:4])
print(oddnum.num)
print(oddnum.name)
print(oddnum.data)
#print(oddnum.func)
print(oddnum())

class Chain(object):
    def __init__(self, path=''):
        self.path = path
    def __getattr__(self,attr):
        return Chain('%s/%s'%(self.path, attr))
    def users(self, users):
        return Chain('%s/users/%s' %(self.path, users))
    def __str__(self):
        return self.path
    __repr__ = __str__
print(Chain().users('michael').repos)

class Chain(object):
    def __init__(self, path=''):
        self.path = path
    def __getattr__(self,attr):
        return Chain('%s/%s'%(self.path, attr))
    def __call__(self, param):
        return Chain('%s/%s'%(self.path, param))
    def __str__(self):
        return self.path
    __repr__ = __str__

print(Chain().get.users('michael').group('doctor').repos)

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum  import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec') )
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import  unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name , member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)


