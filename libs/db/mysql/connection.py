import pymysql

from config import database

def connection():
    return pymysql.connect(
        host = database['host'],
        port = database['port'],
        user = database['user'],
        passwd = database['password'],
        db = database['db'],
        charset = database['charset']
    )