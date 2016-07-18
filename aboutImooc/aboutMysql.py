#coding:utf-8
__author__ = 'Joan'

import  MySQLdb

conn = MySQLdb.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'pythondb',
    charset = 'utf8'
 )
cursor =  conn.cursor();
sql = 'select * from user'
cursor.execute(sql)
rs = cursor.fetchone()
print rs
rs = cursor.fetchmany(3)
print rs
cursor.close()
conn.close()
