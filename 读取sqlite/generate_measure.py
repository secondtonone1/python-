#-*-coding:utf-8-*-
#从sql 读取数据


import os
import sqlite3 as db

sqlpath = "E631measure.sql"
db_path = "ESeries.DB"
max_len = len('低值白细胞CBC+DIFF+CRP+SAA测量时序1')


def readFronSqllite(db_path,exectCmd):
    conn = db.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor=conn.cursor()        # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory=db.Row     # 可访问列信息
    cursor.execute(exectCmd)    #该例程执行一个 SQL 语句
    rows=cursor.fetchall()      #该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    return rows
    #print(rows[0][2]) # 选择某一列数据

def generatorHead():
    sqldir = os.path.join(os.path.dirname(__file__),sqlpath)
    print(sqldir)
    with open(sqldir, 'w+', encoding='utf-8') as sqlfile:
        head_tips = '''-- WB:0     PB:1    PD:2        SR:3    低值白细胞(LB):4
-- CBC:0    CD:1    CDRET:2     CBCRET:3    CDC:4   CDCS:5    CRP:6   CRPSAA:7  8:SAA, 9:RET
-- type     0:(CBC, CD), 1:(RET相关), 2:(CRP, SAA相关), 3:(CRP+SAA相关)
DELETE FROM measure_function;
INSERT INTO measure_function (sample_mode, test_mode, pool_index, seq_no, type, desc) VALUES
'''
        sqlfile.write(head_tips)   #加\n换行显示

def generatorSqlDataLine(row, sqlfile, blastline):
    line_str = '('
    for index in range(len(row)):
        strcolum = str(row[index])
        if index == 0:
            continue
        if index == 6:
            strcolum = "'"+strcolum + "'"
        if index == 4:
            strcolum = '0x{:03X}'.format(row[index])
        if index != 6:
            line_str += (strcolum+', ')
        else:
            len_emptystr = max_len - len(strcolum)
            if(len_emptystr >=0):
                line_str += (strcolum+ len_emptystr*(' '))
            else:
                line_str += strcolum
    if (blastline):
        line_str +=');\n'
    else:
        line_str += '),\n'
    sqlfile.write(line_str)

def generatorSqlDataLines(rows):
    sqldir = os.path.join(os.path.dirname(__file__),sqlpath)
    with open(sqldir, "a+", encoding='utf-8') as sqlfile:
        lastindex = 0
        for index, row in enumerate(rows):
            if lastindex != row[1]:
                sqlfile.write('\n')
                lastindex = row[1]
            generatorSqlDataLine(row, sqlfile, index == (len(rows)-1))

#多个key排序
def sortRows(rows):
    rows.sort(key=lambda t: (t[1],t[2],t[3],t[4]))
    #print(rows)

if __name__ == "__main__":
    dbpath = os.path.join(os.path.dirname(__file__), db_path)
    generatorHead()
    rows = readFronSqllite(dbpath,"select * from measure_function")
    sortRows(rows)
    generatorSqlDataLines(rows)
