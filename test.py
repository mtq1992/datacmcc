import MySQLdb
conn = MySQLdb.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       passwd = '111111',
                       db ='spiderdb',
                       charset = 'utf8'
                        )

cursor = conn.cursor()
sql_insert = "insert into test(id,name) values(10,'hello')"
sql_update = "update test set name='mtq' where id = 1"
sql_delete = "delete from test where id1 <3 "
try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    conn.commit()
except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()
