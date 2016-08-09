#encoding utf-8
import MySQLdb


def writedb():
    try:
        conn1 = MySQLdb.connect(host='localhost', user='root', passwd='111111', port=3306)
        conn1.select_db('spiderdb')
        cur1 = conn1.cursor()
        fin = open('data','r')
        data =[
                ('12','Q'),
                ('13','W'),
                ('14','H'),
                ('3','A')
               ]

        sql = "insert into test(id,name) values (%s,%s)"
        cur1.executemany(sql,data)
        fin.close()
        conn1.commit()
        cur1.close()
        conn1.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def readdb():
    try:
        conn2=MySQLdb.connect(host='localhost',user='root',passwd='111111',port=3306,charset = 'utf8' )
        conn2.select_db('spiderdb')
        cur2=conn2.cursor()
        cur2.execute("select * from test ")
        data=cur2.fetchall()
        file_object = open('thefile.txt', 'w')
        for row in data:
            file_object.write('%s|%s\n') % (row[0],row[1])
        file_object.close()
        conn2.commit()
        cur2.close()
        conn2.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

#writedb()
readdb()

