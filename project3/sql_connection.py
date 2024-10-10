import os
import mysql.connector as mc

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mc.connect(user='root', password=os.getenv('DB_PASSWORD'),
                           host='127.0.0.1', database='gs')
    return __cnx

get_sql_connection()