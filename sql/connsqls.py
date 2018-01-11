#-*-coding:utf-8-*-
#pip install mysql-connector==2.1.4
import mysql.connector
conn = mysql.connector.connect(user='root',password='123456',database='test')
cursor = conn.cursor()
#创建user表
cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user(id, name) values(%s,%s)',['1','Michael'])
print(cursor.rowcount)
cursor.close()
conn.commit()
cursor = conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
#获取结果集
values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection:
cursor.close()

conn.close()

