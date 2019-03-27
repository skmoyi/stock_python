#!/usr/bin/python3
# import pymysql
#
# db = pymysql.connect('localhost','root','123456','test')
#
# cursor = db.cursor()
#
# cursor.execute('SELECT VERSION()')
#
# data = cursor.fetchone()
#
# print('Database version : %s'% data)
#
# db.close()

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
