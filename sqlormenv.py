#!/usr/bin/python
#-*- codig:utf-8 -*-

import sys
sys.path.append('..')
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

mysql_con = 'sqlite:///mnt/work/test4.db'

Engine = create_engine(mysql_con, echo=False)
DB_Session = sessionmaker(bind=Engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(Engine)

def drop_db():
    Base.metadata.drop_all(Engine)
