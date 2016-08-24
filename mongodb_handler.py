import sqlite3
import logging
import getpass
from datetime import datetime

class MongoHandler(logging.Handler):
    """ Custom log handler
    Logs all messages to a mongo collection. This  handler is 
    designed to be used with the standard python logging mechanism.
    """

    def __init__(self,level=logging.NOTSET):
        """ Init log handler and store the collection handle """
        logging.Handler.__init__(self, level)
        conn = sqlite3.connect('test.db')

    def emit(self,record):
        """ Store the record to the collection. Async insert """
        try:
            tm = datetime.now()
            print tm          
            print record.filename,type(record.filename)
            print record.lineno,type(record.lineno)
            print record.funcName,type(record.funcName)
            print record.levelname,type(record.levelname)
            print record.msg,type(record.msg)
            
            #self.collection.save(record)
        except Exception as e:
            logging.error("Unable to save log record: %s", e.message ,exc_info=True)

