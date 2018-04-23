#-*-coding:utf-8-*-

import asyncio
@asyncio.coroutine
#@asyncio.coroutine把一个generator标记为coroutine类型
def hello():
	print("Hello world!")
	# 异步调用asyncio.sleep(1)
	r = yield from asyncio.sleep(1)
	print("Hello again!")

#由于asyncio.sleep()也是一个coroutine，
#所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
#当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()








