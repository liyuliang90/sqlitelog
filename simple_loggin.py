#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
sys.path.append('..')

import logging

from mongodb_handler import MongoHandler

#if __name__ == '__main__':

def test():
    log = logging.getLogger('example')
    formatter = logging.Formatter(fmt='%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s', datefmt='%F %H:%M:%S') 
    #log.setFormatter(formatter)
    log.setLevel(logging.DEBUG)
    handler = MongoHandler() 
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
 
    log.addHandler(handler)
    

    log.debug("1 - debug message")
    '''
    log.info("2 - info message")
    log.warn("3 - warn message")
    log.error("4 - error message")
    log.critical("5 - critical message")
    '''
if __name__ == '__main__':
    test()
