#-*-coding:utf-8-*-

import sqlite3
#连接数据库test.db文件，如果不存在则创建
conn = sqlite3.connect('test.db')
#获取游标
cursor = conn.cursor()
#通过游标创建表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20) )')
#通过游标插入数据
cursor.execute('insert into user(id, name) values(\'1\',\'Bob\')')
#打印新增的行数
print(cursor.rowcount)
#关闭cursor
cursor.close()
#提交事务
conn.commit()
#关闭连接
conn.close()


