import MySQLdb
import config
import sql_request

"""
скрипт создает бд
"""
host = config.host
user = config.user
password = config.password
db = config.db

create_table = sql_request.create_table_url
index = sql_request.add_index

conn = MySQLdb.connect(host , user , password, db)

cursor = conn.cursor()
cursor.execute(create_table)
cursor.execute(index)

conn.close()