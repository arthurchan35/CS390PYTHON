#!/usr/bin/python
import sqlite3
import cgi
import cgitb
from emailSender import sendValidationEmail
conn = sqlite3.connect('mylink.db')
c = conn.cursor()
form = cgi.FieldStorage()

head = """Content-type: text/html


"""
print(head)

username = form.getvalue('login')
password = form.getvalue('password')
commit = form.getvalue('commit')
print (username)
if commit == "New_Account":
	key = sendValidationEmail(username, password, "create")
	c.execute("INSERT INTO users (username, password, istemp, key) VALUES ('"+username+"', '000000', 'true', '"+key+"')")

elif commit == "Login":
	c.execute("SELECT * FROM users WHERE (username = '"+username+"' AND password = '"+password+"' AND istemp = 'false')")
	res = c.fetchone()
	if res is None:
		print ("Wrong Username OR Password")
	else:
		print ("login successful")

elif commit == "Change":
	key = sendValidationEmail(username, password, "change")
	c.execute("UPDATE users SET (Key = '"+key+"') WHERE (username = '"+username+"')")

else:
	print("unkown input")
conn.commit()