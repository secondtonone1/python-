#-*-coding:utf-8-*-

import chardet
rs = chardet.detect(b'Hello, world!')
print(rs)

data = '江船火独明'.encode('gb2312')
rs = chardet.detect(data)
print(rs)

data2 = '此情可待成追忆'.encode('utf-8')
rs2 = chardet.detect(data2)
print(rs2)

'''
from tkinter import *

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text = 'Quit', command=self.quit)
		self.quitButton.pack()




app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
'''
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master = None)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alterButton = Button(self,text='Hello',command=self.hello)
		self.alterButton.pack()


	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message', 'Hello, %s' %name)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()