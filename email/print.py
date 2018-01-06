#-*-coding:utf-8-*-
#!/usr/bin/python

 
#coding=utf-8
'''
import smtplib
from email.mime.text import MIMEText
msg_from='XXXXX@163.com'                                 
passwd='XXXXX'                                  
msg_to='XXXXX@qq.com'                                  
                            
subject="python邮件测试"                                       
content="这是我使用python smtplib及email模块发送的邮件"

msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    #s = smtplib.SMTP_SSL("smtp.163.com",465)
    s = smtplib.SMTP("smtp.163.com",25)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except smtplib.SMTPException as e:
    print ("发送失败")
finally:
    s.quit()
'''

'''
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

msg_from='XXXXX@163.com'                                 
passwd='XXXXX'                                  
msg_to='XXXXX@qq.com'
receivers = ['XXXXX@qq.com']                                
                            
subject="python邮件测试"                                       
content="这是我使用python smtplib及email模块发送的邮件"

msg = MIMEText(content,'plain','utf-8')
msg['Subject'] = Header(subject,'utf-8').encode()
msg['From'] = _format_addr('恋恋风辰 <%s>' %msg_from)
msg['To'] = msg_to

try:
    #s = smtplib.SMTP_SSL("smtp.163.com",465)
    s = smtplib.SMTP("smtp.163.com",25)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, receivers, msg.as_string())
    print ("发送成功")
except smtplib.SMTPException as e:
    print ("发送失败")
finally:
    s.quit()
'''
#发送html文件
'''
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
msg_from = 'XXXXXX@163.com'
passwd = 'XXXXX'
msg_to='XXXXXX@qq.com'
receivers = ['XXXXXX@qq.com']
subject = 'python邮件测试html'
content = '<html><body><h1>Hello</h1>' +\
    '<p>send by <a href="http://www.python.org">Python</a>...</p>'

msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8').encode()
msg['From'] = _format_addr('恋恋风辰 <%s>' %msg_from)
msg['To'] = msg_to

try:
    s = smtplib.SMTP("smtp.163.com",25)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, receivers, msg.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print('发送失败')
finally:
    s.quit()
'''
#发送附件

'''
import smtplib
import email
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg_from = 'XXXXX@163.com'
passwd = 'XXXXX'
msg_to='XXXXXX@qq.com'
receivers = ['XXXX@qq.com']
subject = 'python邮件测试附件'
content = '<html><body><h1>Hello</h1>' +\
    '<p>send by <a href="http://www.python.org">Python</a>...</p>'

#附件邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('恋恋风辰 <%s>' %msg_from)
msg['To'] = msg_to
msg['Subject'] = Header(subject, 'utf-8').encode()
#添加正文
text = MIMEText(content, 'html','utf-8')
msg.attach(text)
#添加附件就是创建一个MIMEBase对象，然后attach到msg上。
with open('./email.jpg','rb') as f:
    #设置附件名字
    mime = MIMEBase('image', 'jpg', filename='text.jpg')
    #加上头信息
    mime.add_header('Content-Disposition','attachment',filename='test.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    #读取内容放入附件
    mime.set_payload(f.read())
    #用Base64编码
    email.encoders.encode_base64(mime)
    #添加到MIMEMultipart中
    msg.attach(mime)

try:
    s = smtplib.SMTP("smtp.163.com",25)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, receivers, msg.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print('发送失败')
finally:
    s.quit()
'''

#添加图片的html邮件
'''
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg_from = 'XXXXXXXXXXXX@163.com'
passwd = 'XXXXX'
msg_to='XXXXXXXXX@qq.com'
receivers = ['XXXXXXXXXX@qq.com']
subject = 'python邮件测试附件'
content = '<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!'

#附件邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('恋恋风辰 <%s>' %msg_from)
msg['To'] = msg_to
msg['Subject'] = Header(subject, 'utf-8').encode()
#添加正文
text = MIMEText(content, 'html','utf-8')
msg.attach(text)

#添加附件就是创建一个MIMEBase对象，然后attach到msg上。
with open('./email.jpg','rb') as f:
    #设置附件名字
    mime = MIMEImage(f.read())
    #加上头信息
    mime.add_header('Content-Disposition','attachment',filename='test.jpg')
    mime.add_header('Content-ID','<image1>')
   
    #添加到MIMEMultipart中
    msg.attach(mime)

try:
    s = smtplib.SMTP("smtp.163.com",25)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, receivers, msg.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print('发送失败')
finally:
    s.quit()
'''

#多种附件全部发送
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg_from = 'XXXXXXXXX@163.com'
passwd = 'XXXXXXXXXXX'
msg_to='XXXXXXXXX@qq.com'
receivers = ['XXXXXXXXXXX@qq.com']
subject = 'python邮件测试附件'
content = '多种附件'

#附件邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('恋恋风辰 <%s>' %msg_from)
msg['To'] = msg_to
msg['Subject'] = Header(subject, 'utf-8').encode()
#添加正文
text = MIMEText(content, 'html','utf-8')
msg.attach(text)

os.chdir('./res')    
dir = os.getcwd()

for fn in os.listdir(dir):
    print(fn)
    with open(fn,'rb') as f:
        mime = MIMEText(f.read(), 'base64', 'utf-8')
        mime.add_header('Content-Disposition','attachment',filename = fn)
        mime.add_header('Content-Type', 'application/octet-stream')
        msg.attach(mime)

try:
    s = smtplib.SMTP("smtp.163.com",25)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, receivers, msg.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print('发送失败')
finally:
    s.quit()
'''

#采用MIMEApplication发送邮件

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg_from = 'xxxxxxxxx@163.com'
passwd = 'xxxxxxxxxx'
msg_to='xxxxxxxxxxx@qq.com'
receivers = ['xxxxxxxxx@qq.com']
subject = 'python邮件测试附件'
content = '多种附件'

#附件邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('恋恋风辰 <%s>' %msg_from)
msg['To'] = msg_to
msg['Subject'] = Header(subject, 'utf-8').encode()
#添加正文
text = MIMEText(content, 'html','utf-8')
msg.attach(text)

os.chdir('./res')    
dir = os.getcwd()

for fn in os.listdir(dir):
    print(fn)
    with open(fn,'rb') as f:
        mime = MIMEApplication(f.read())
        mime.add_header('Content-Disposition','attachment',filename = fn)
        mime.add_header('Content-Type', 'application/octet-stream')
        msg.attach(mime)

try:
    s = smtplib.SMTP("smtp.163.com",25)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, receivers, msg.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print('发送失败')
finally:
    s.quit()