#!/usr/bin/python
#-*- coding:utf-8 -*-

import sqlite3
from datetime import datetime

class LogMsg(object):
    def __init__(self):
        db_name = 'log.db'
        self.conn = sqlite3.connect(db_name)
        table_name = 'logmsg'

    def create_table(self):
        sql = 'create table logmsg(id integer primary key autoincrement,\
                            time datetime,\
                            filename char(50),\
                            lineno int,\
                            funcName char(50),\
                            levelname char(8),\
                            msg text);'

