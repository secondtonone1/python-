#-*-coding:utf-8-*-

import re

'''
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))


from datetime import datetime
dt = datetime(2017,12,13,13,7)
# 把datetime转换为timestamp
print( dt.timestamp() )
 

from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))


#根据时间戳转化为本地时间和utc时间

from datetime import datetime
t = 1429417200.0
# 本地时间
print(datetime.fromtimestamp(t))
# UTC时间 
print(datetime.utcfromtimestamp(t))

from datetime import datetime
cday = datetime.strptime('2017-6-1 18:22:22','%Y-%m-%d %H:%M:%S')
print(cday)

from datetime import datetime
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))

from datetime import datetime , timedelta
now = datetime.now()
print( now )
print(now + timedelta(hours = 10))
print(now + timedelta(days = 1))
print(now + timedelta(days = 2, hours = 12))


from datetime import datetime, timedelta, timezone
# 创建时区UTC+8:00
timezone_8 = timezone(timedelta(hours = 8) )
now = datetime.now()
print(now)
# 强制设置为UTC+8:00
dt = now.replace(tzinfo=timezone_8)
print(dt)


from datetime import datetime, timedelta, timezone

# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8) ))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9) ) )
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours = 9) ) )
print(tokyo_dt2)


#可命名tuple
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(1,2)
print(p.x)

from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)


from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])


from collections import OrderedDict
d = dict([ ['a',1], ['b',2],['c',3]])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)

od2 = OrderedDict([['Bob',90],['Jim',20],['Seve',22]])
print(od2)

from collections import Counter
c = Counter()

for ch in 'programming':
	c[ch]=c[ch]+1
'''

'''
#itertools.count(start , step)
import itertools
natuals = itertools.count(1)
for n in natuals:
	print(n)
'''
'''
import itertools
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
	print(c)
'''
'''
import itertools
ns = itertools.repeat('A',5)
for n in ns:
	print(n)


natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(ns)
print(list(ns) )


for c in itertools.chain('ABC','XYZ'):
	print(c)

print(list(itertools.chain('ABC','XYZ')) )

for key, group in itertools.groupby('AAABBBCCAAA'):
	print(key, list(group))
	print(key, group)

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper() ):
	print(key,list(group))

#open 返回的对象才可用with
# 在类中实现__enter__和__exit__可以使该类对象支持with用法


class Query(object):
	def __init__(self, name):
		self.name = name
	
	def __enter__(self):
		print('Begin')
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			print('Error')
		else:
			print('End')

	def query(self):
		print('Query info about %s...' %self.name)		


with Query('BBBB') as q:
	if q:
		q.query()
'''

''' 
with EXPR as VAR:
实现原理:
在with语句中, EXPR必须是一个包含__enter__()和__exit__()方法的对象(Context Manager)。
调用EXPR的__enter__()方法申请资源并将结果赋值给VAR变量。
通过try/except确保代码块BLOCK正确调用，否则调用EXPR的__exit__()方法退出并释放资源。
在代码块BLOCK正确执行后，最终执行EXPR的__exit__()方法释放资源。
'''




#通过python提供的装饰器contextmanager，作用在生成器函数，可以达到with操作的目的
'''
from contextlib import contextmanager
class Query(object):
	def __init__(self, name):
		self.name = name

	def query(self):
		print('Query info about %s ...' %self.name)

@contextmanager
def create_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')

with create_query('aaa') as q:
	if q:
		print(q.query())
'''

#contextmanager源码
'''
class GeneratorContextManager(object):
	def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        try:
            return self.gen.next()
        except StopIteration:
            raise RuntimeError("generator didn't yield")
​
    def __exit__(self, type, value, traceback):
        if type is None:
            try:
                self.gen.next()
            except StopIteration:
                return
            else:
                raise RuntimeError("generator didn't stop")
        else:
            try:
                self.gen.throw(type, value, traceback)
                raise RuntimeError("generator didn't stop after throw()")
            except StopIteration:
                return True
            except:
                # only re-raise if it's *not* the exception that was
                # passed to throw(), because __exit__() must not raise
                # an exception unless __exit__() itself failed.  But
                # throw() has to raise the exception to signal
                # propagation, so this fixes the impedance mismatch 
                # between the throw() protocol and the __exit__()
                # protocol.
                #
                if sys.exc_info()[1] is not value:
                    raise
​
def contextmanager(func):
    def helper(*args, **kwds):
        return GeneratorContextManager(func(*args, **kwds))
    return helper
'''

'''
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
'''

##closing 实现原理
'''
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
'''
'''
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
'''

'''
上述代码执行结果为：

<h1>
hello
world
</h1>
代码的执行顺序是：

with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
'''
'''
from urllib import request 
with request.urlopen('http://www.limerence2017.com/') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' %(k,v))
	print('Data:', data.decode('utf-8') )
'''
'''
from urllib import request
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:

	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' %(k,v))
	print('Data:', f.read().decode('utf-8'))


from urllib import request, parse
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s:%s' %(k,v))
	print('Data: ', f.read().decode('utf-8'))


proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.bulid_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
	pass


proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
'''

'''
from urllib import request, parse


url = 'https://www.zhihu.com/question/28591246/answer/276466494'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
refer = 'https://www.zhihu.com/question/28591246/answer/276466494'
req = request.Request(url)
req.add_header('User-Agent',user_agent)
req.add_header('Referer', refer)

with request.urlopen(req) as f:
	print(f.read().decode('utf-8'))
'''
#先将数据读入文件
'''
from urllib import request, parse
from urllib import error
page = 1
url = 'https://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
try:
	req = request.Request(url)
	req.add_header('User-Agent', user_agent)
	response = request.urlopen(req)
	#bytes变为字符串
	content = response.read().decode('utf-8')
	print(type(content))
	#uf-8编码方式打开
	file = open('file.txt', 'w',encoding='utf-8')

	file.write(content)
	
except error.URLError as e:
	if hasattr(e,'code'):
		print (e.code)
	if hasattr(e,'reason'):
		print (e.reason)
finally:
	file.close()
'''

#从文件中读取并用正则表达式解析
'''
import re

with open('file.txt','r', encoding='utf-8') as f:
	data = f.read()

pattern = re.compile(r'<div.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?number">(.*?)</i>.*?'+
	r'"number">(.*?)</i>', re.S )
result = re.search(pattern, data)
#print(result)
#print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))
print(result.group(4))
'''
#利用findall批量爬取段子


from urllib import request, parse
from urllib import error
page = 1
url = 'https://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
try:
	req = request.Request(url)
	req.add_header('User-Agent', user_agent)
	response = request.urlopen(req)
	#bytes变为字符串
	content = response.read().decode('utf-8')
	pattern = re.compile(r'<div.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?number">(.*?)</i>.*?'+
	r'"number">(.*?)</i>', re.S )
	result = re.findall(pattern, content)
	files = open('findfile.txt','w+', encoding='utf-8')
	for item in result:
		author =  item[0]
		contant = item[1]
		vote = '赞：'+item[2]
		commit = '评论数：'+item[3]
		infos = vote +' '+commit+' '+'\n\n'
		print(author)
		print(contant)
		print(infos)
		files.write(author)
		files.write(contant)
		files.write(infos)
		

except error.URLError as e:
	if hasattr(e,'code'):
		print (e.code)
	if hasattr(e,'reason'):
		print (e.reason)
finally:
	files.close()