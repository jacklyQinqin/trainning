"""
Python’s Built-in sqlite3 Module
SQL 是 structured Query language 的简称.就是结构化查询语言

SQL可以使用类似pipe的机制从datebase获取数据,使用python脚本处理.


套路:

    database ----->sql------->script


使用步骤:
    0.导入数据库模组
    1.创建数据库对象
        conn = sqlite3.connect("thisIsADataBase.db")
    2.

"""

import sqlite3

conn = sqlite3.connect("thisIsADataBase.db")
print("Open Database Success!\n")

conn.execute('''CREATE TABLE MT
    (ID INT PRIMARY KEY   NOT NULL,
    NAME      TEXT  NOT NULL,
    AGE      INT   NOT NULL,
    ADDRESS    CHAR(50),
    SALARY     REAL);''')
print("Table created successfully")
