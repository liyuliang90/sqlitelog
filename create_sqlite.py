#!/usr/bin/python
#-*- coding:utf-8 -*-

import sqlite3
from datetime import datetime

conn = sqlite3.connect('log.db')

sql = 'create table logmsg(id integer primary key autoincrement,\
                            time datetime,\
                            filename char(50),\
                            lineno int,\
                            funcName char(50),\
                            levelname char(8),\
                            msg text);'
#conn.execute(sql)

time1=datetime.now()
filename='test.py'
lineno=12
funcName='test'
levelname='debug'
msg='error'

insert_sql = "insert into logmsg (time,filename,lineno,funcName,levelname,msg) values ('%s','%s',%s,'%s','%s','%s')" % (time1,filename,lineno,funcName,levelname,msg)
conn.execute(insert_sql)
conn.commit()

a='select * from logmsg;'
c=conn.execute(a)
for i in c:
    print i

conn.close()
