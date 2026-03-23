# Dastur : 
#     1 malumot qabul qiladi 
#     2 uni qayta ishlaydi 
#     3 saqlaydi > RAM > ROM 
#     4 natija qaytaradi


# SQL , NOSQL 
# SQL - Structured Query Language > Jadval 
# NOSQL - Not Structured Query Language


# DBMS - Database Management System > SQLite, MySQL, PostgreSQL\
# Python default dbms - SQLite
import sqlite3

conn = sqlite3.connect("user.db") 
# print(type(conn))
# print(dir(conn))
cur = conn.cursor()

# try:
#     cur.execute("""CREATE TABLE users(
#     id INTEGER,
#     name TEXT,
#     age INTEGER);""") 
# except sqlite3.DatabaseError as e:
#     print(e)
#     cur.execute("""INSERT INTO users(id,name,age) VALUES(2,'John',20); """)
#     print("OK")
#     conn.commit() # db ga o'zgarishlarni tasdiqlash

# data = cur.execute("""SELECT * FROM users""")
# print(data) # <sqlite3.Cursor object at 0x0000014BCBE60240>
# 'fetchall', 'fetchmany', 'fetchone'
# print(dir(data))
# print(data.fetchall()) # [(1, 'Abdurahmon', 30), (1, 'Abdurahmon', 30), (1, 'Abdurahmon', 30)]
# data = cur.execute("""SELECT * FROM users WHERE name='John' """)
# print(data.fetchall()) # [(2, 'John', 20)]
# data = cur.execute("""SELECT * FROM users WHERE age>20 """)
# print(data.fetchall()) # [(1, 'Abdurahmon', 30), (1, 'Abdurahmon', 30), (1, 'Abdurahmon', 30)]