#-*-coding:utf-8-*-
## try except
'''
try:
    print('try...')
    r = 10/0
    print('result is :', r)
except ZeroDiversionError as e:
    print('except is :', e)
finally:
    print('finally ...')
print('END')
'''
'''
try:
    print('try...')
    r = 10/int('a')
    print('result is: ', r)
except ValueError as e:
    print('ValueError : ', e)
except ZeroDiversionError as e:
    print('ZeroDivisionError is : ', e)
finally:
    print('finally ...')
print('END')
'''

'''
try:
    print('try... ')
    r = 10/int('2')
    print('result is : ', r)
except ValueError as e:
    print('ValueError : ', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError is : ', e)
else:
    print('no error')
finally:
    print('finally ...')
print('END')
'''

'''
def foo(s):
    return 10/int(s)
def bar(s):
    return  foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Exception is : ', e)
    finally:
        print('finally...')
main()
'''
'''
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')
'''

'''
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid error is : %s' %s)
    return 10/n
foo('0')
'''

'''
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid error is: %s' %s)
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise

bar()
'''
'''
def foo(s):
    n = int(s)
    assert n != 0 ,'n is zero'
    return 10/n

def main():
    foo('0')

main()
'''
'''
import logging 
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    return 10/n

def main():
    m = foo('0')
    logging.info('n is : %d' %m)
main()
'''
#pdb调试用 python -m pdb 文件名.py
'''
import pdb
def foo(s):
    n = int(s)
    pdb.set_trace()
    return 10/n
def main():
    m = foo('0')
main()
'''
''' 
class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except exception as e:
            raise AttributeError('AttributeError is :%s', e)
    def __setattr__(self, key, value):
        self[key] =  value

dictobj = Dict()
#print(dictobj.name)
'''

import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d  %d...' % (n,n))
        r = '%d  %d = %d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
print('worker exit.')
