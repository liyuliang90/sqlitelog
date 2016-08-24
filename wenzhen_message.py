#!/usr/bin/python
#-*- coding:utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime, Text
from sqlormenv import Base
 
class WenzhenMessage(Base):
    __tablename__ = 'wenzheng_message'
    id = Column(Integer, primary_key=True)
    from_id = Column(String(255))
    to_id = Column(String(255))
    msg_type = Column(Integer)
    msg_body = Column(Text)
    create_time = Column(DateTime)
    status = Column(Integer)
    app_id = Column(Integer)
    channel = Column(Integer)
    style = Column(Integer)
    flag = Column(Integer)

