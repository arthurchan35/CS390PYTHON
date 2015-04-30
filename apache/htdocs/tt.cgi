#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('mylink.db')
c = conn.cursor()

head = """Content-type: text/html


"""
print(head)

username = "chen1123@purdue.edu"
password = "konlove"
#if commit == "New_Account":
#	c.execute("INSERT INTO users (username, password) VALUES ('"+username+"', '"+password+"')")
#	for row in c.execute('SELECT * FROM users') :print row
#elif commit == "Login":
c.execute("SELECT * FROM users WHERE (username = '"+username+"' AND password = '"+password+"')")
result = c.fetchone()
if result is None:
	print ("Wrong Username OR Password")
	print result
else:
	print ("login successful")
	print result
conn.commit()