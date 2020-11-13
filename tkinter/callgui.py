#-*-coding:utf-8-*-

from tkinter import *
import hashlib
import time

LOG_LINE_NUM = 0
class MY_GUI():
	def __init__(self, init_window_name):
		self.init_window_name = init_window_name
		
	def set_init_window(self):
		self.init_window_name.title("对讲部署程序")
		self.extern_ip_label = Label(self.init_window_name, text="外网地址和端口号")
		self.extern_ip_label.grid(row=0, column=0)
		self.inner_ip_label = Label(self.init_window_name, text="内网地址和端口号")
		self.inner_ip_label.grid(row=0, column=12)
		self.extern_ip_text = Text(self.init_window_name, width=20, height=2)  #外网地址录入框
		self.extern_ip_text.grid(row=1, column=0, rowspan=10, columnspan=10)
		self.inner_ip_text = Text(self.init_window_name, width=20, height=2)  #内网地址录入框
		self.inner_ip_text.grid(row=1, column=12, rowspan=15, columnspan=10)
		 #按钮
		self.str_trans_to_md5_button = Button(self.init_window_name, text="确定", bg="lightblue", 
		width=10,command=self.start_server)  # 调用内部方法  加()为直接调用
		self.str_trans_to_md5_button.grid(row=30, column=0)
		pass
	def start_server(self):
		print("extern ip is ", self.extern_ip_text.get('0.0','end'))
		print("inner ip is ", self.inner_ip_text.get('0.0','end'))
		print("start_server...")
		pass

def gui_start():
	init_window = Tk()              #实例化出一个父窗口
	ZMJ_PORTAL = MY_GUI(init_window)

	# 设置根窗口默认属性
	ZMJ_PORTAL.set_init_window()
	init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
	pass

if __name__ == '__main__':
	gui_start()