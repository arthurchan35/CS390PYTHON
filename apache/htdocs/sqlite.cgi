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
gusername = form.getvalue('login')
password = form.getvalue('password')
commit = form.getvalue('commit')
#username = "chen1123@purdue.edu"
#password = "1234556"
#commit = "New_Account"

if commit == "New_Account":
	c.execute("SELECT * FROM users WHERE (username = '"+username+"')")
	res = c.fetchone()
	if res is None:
		key = sendValidationEmail(username, password, "create")
		c.execute("INSERT INTO users (username, password, istemp, key) VALUES ('"+username+"', '"+password+"', 'true', '"+key+"')")
		print("A verification Email has been sent to your address")
	else:
		print("username is taken, please choose anther one")

elif commit == "Login":
	c.execute("SELECT * FROM users WHERE (username = '"+username+"' AND password = '"+password+"' AND istemp = 'false')")
	res = c.fetchone()
	if res is None:
		c.execute("SELECT * FROM users WHERE (username = '"+username+"' AND password = '"+password+"' AND istemp = 'true')")
		res = c.fetchone()
		if res is None: 
			print ("Wrong Username OR Password")
		else:
			print ("this account has not yet been activated")
	else:
		print ("login successful")

elif commit == "Change":
	c.execute("SELECT * FROM users WHERE (username = '"+username+"' AND istemp = 'false')")
	res = c.fetchone()
	if res is None:
		print ("No such Email account in our database or this account is not activated")
	else:
		key = sendValidationEmail(username, password, "change")
		c.execute("UPDATE users SET Key = '"+key+"' WHERE (username = '"+username+"')")
		print("A verification Email has been sent to your address")

else:
	print("soemthing")
	print("unkown input")
conn.commit()