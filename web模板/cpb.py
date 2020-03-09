"""
file：cpb.py
author：陈先生
date：2019/8/1711:36
blog:https://chenpb-lu.github.io
"""
import mysql.connector

mydb = mysql.connector.connect(
    host='192.168.0.68',
    user='sc',
    passwd = "Sctl@1234",
    database = 'califeng',
    port='3306'

)

mycursor = mydb.cursor()
mycursor.execute("show tables")
for i in mycursor:
    print(i)

mycursor.execute("insert into student(id,name),VALUE(8,'sgJack')")
mydb.commit()