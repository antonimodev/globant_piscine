import pysqlite3

from pysqlite3 import *

def connect(*args, **kwargs):
    return pysqlite3.connect(*args, **kwargs)