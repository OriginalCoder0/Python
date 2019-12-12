'''
 Name: connect to MySQL database test
 Athor: 卢华东
 Date: 2018-07-04
 Description:
'''

import pymysql

# open and connect database
db = pymysql.connect(host="localhost",
                     user="root",
                     password="lu1010",
                     db="blogdb",
                     charset="utf8")

# get cursor object
cursor = db.cursor()

try:
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version: %s" % data)
except Exception as err:
    print("SQL执行出错！原因：", err)

print("-"*48)

sql = "SELECT * FROM users"

try:
    cursor.execute(sql)
    print("结果数目：", cursor.rowcount)

    '''
    while True:
        data = cursor.fetchone()
        if data == None:
            break
        print(data)
    '''
    alist = cursor.fetchall()
    for vo in alist:
        print(vo)
except Exception as err:
    print("SQL执行出错！原因：", err)

db.close()

