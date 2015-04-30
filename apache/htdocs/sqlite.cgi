#!/usr/bin/python
import sqlite3
import cgi
import cgitb
conn = sqlite3.connect('mylink.db')
c = conn.cursor()
form = cgi.FieldStorage()

head = """Content-type: text/html


"""
print(head)

username = form.getvalue('login')
password = form.getvalue('password')
c.execute("INSERT INTO users (username, password) VALUES ('"+username+"', '"+password+"')")
for row in c.execute('SELECT * FROM users') :print row
conn.commit()