#-*-coding:utf-8-*-
f = open('openfile.txt','r')
print(f.read())
f.close()

f = open('./openfile.txt','rb')
print(f.read())
f.close()

with open('openfile.txt','r') as f:
    print(f.read())


f = open('openfile.txt','r')
print(f.readline())
f.close()

f = open('openfile.txt','r')
for line in f.readlines():
    print(line.strip())
f.close()

f = open('openfiles.txt','r',encoding='gbk' )
print(f.read())

with open('openfile.txt', 'a') as f:
    f.write('\n')
    f.write('Hello World!!!')


from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world !')
print(f.getvalue() )

from io import StringIO
f = StringIO("Hello\nWorld\nGoodBye!!")
while True:
    s = f.readline()
    if(s==''):
        break
    print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8') )
print(f.getvalue())

from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()

import os
print(os.name)
print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))


# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
print(os.path.join('/Users/michael','testdir') )
# 然后创建一个目录:
#print(os.mkdir('/Users/michael/testdir') )
# 删掉一个目录:
#print(os.rmdir('/Users/michael/testdir') )

print(os.path.split('/path/to/file.txt') )
print(os.path.splitext('/path/to/file.txt') )

# 对文件重命名:
#print(os.rename('test.txt', 'test.py') )
#print(os.remove('test.py'))

print([x for x in os.listdir('.') if  os.path.isdir(x) ])

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

#写入文件
f = open('openfile3.txt','wb')
print(pickle.dump(d, f) )
f.close()

f = open('openfile3.txt','rb')
d = pickle.load(f)
f.close()
print(d)


import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def convertFunc(std):
    return {'name':std.name,
    'age':std.age,
    'score':std.score}


s = Student('Bob', 20, 88)
print(json.dumps(s,default=convertFunc))
print(json.dumps(s,default=lambda obj:obj.__dict__))

def revert(std):
    return Student(std['name'], std['age'], std['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=revert ) )
