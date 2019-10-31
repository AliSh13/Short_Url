import MySQLdb
from config import DevelopConfig
import sql_request

"""
скрипт создает бд
"""
host = DevelopConfig.host
user = DevelopConfig.user
password = DevelopConfig.password
db = DevelopConfig.db

create_table = sql_request.create_table_url
index = sql_request.add_index

conn = MySQLdb.connect(host , user , password, db)

cursor = conn.cursor()
cursor.execute(create_table)
cursor.execute(index)

conn.close()