#-*-coding:utf-8-*-
def application(environ, start_response):
	start_response('200 OK', [('Content-Type','text/html')])
	return [b'<h1>Hello, web!</h1>']

#environ是包含所有HTTP请求信息的dict对象
#start_response 是发送http响应的函数
