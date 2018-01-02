#-*-coding:utf-8-*-

import socket
import threading
import time

#线程处理函数
def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello, %s' %data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.'%addr)



#服务器tcp编程流程
#创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定套接字
s.bind(('127.0.0.1',9999))
#监听套接字
s.listen(5)



print('Waiting for connection...')
# 调用accept接受连接
while True:
	# 接收新的连接
	sock, addr = s.accept()
	# 创建新的线程处理TCP
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()





