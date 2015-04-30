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
commit = form.getvalue('commit')
if commit == "New_Account":
	c.execute("INSERT INTO users (username, password) VALUES ('"+username+"', '"+password+"')")
	for row in c.execute('SELECT * FROM users') :print row
elif commit == "Login":
	#c.execute("SELECT userid FROM users WHERE flag IN ('"+username+"', '"+password+"') GROUP BY userid HAVING COUNT(*) = 2")
	#print c.fetchone()
	print("elif")
else:
	print("unkown input")
conn.commit()