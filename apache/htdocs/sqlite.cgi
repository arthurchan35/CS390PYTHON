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
# username = "chen1123@purdue.edu"
# password = "1234556"
# commit = "New_Account"

if commit == "New_Account":
	c.execute("SELECT * FROM users WHERE (username = '"+username+"')")
	res = c.fetchone()
	if res is None:
		key = sendValidationEmail(username, password, "create")
		c.execute("INSERT INTO users (username, password, istemp, key) VALUES ('"+username+"', '"+password+"', 'true', '"+key+"')")
		c.execute("SELECT userid FROM users WHERE (username = '"+username+"')")
		res = c.fetchone()
		uid = str(res[0])
		c.execute("CREATE TABLE friendsof_" + uid + " (friends INTEGER UNIQUE NOT NULL)") 
		c.execute("CREATE TABLE filesof_" + uid + " (files VARCHAR (32) NOT NULL)") 
		c.execute("CREATE TABLE circlesof_" + uid + " (circles VARCHAR (64) UNIQUE NOT NULL)")
		print("A verification Email has been sent to your address")
	else:
		print("username is taken, please choose anther one")

elif commit == "Login":
	c.execute("SELECT userid FROM users WHERE (username = '"+username+"' AND password = '"+password+"' AND istemp = 'false')")
	res = c.fetchone()
	if res is None:
		c.execute("SELECT * FROM users WHERE (username = '"+username+"' AND password = '"+password+"' AND istemp = 'true')")
		res = c.fetchone()
		if res is None: 
			print("Wrong Username OR Password")
		else:
			print("this account has not yet been activated")
	else:
		uid = str(res[0]) 
		print("Set-Cookie: userid=" + uid) 
		redir = "<head><meta http-equiv=\"refresh\" content=\"1;url=home.cgi?userid=\"></head>" 

		print(redir)

elif commit == "Change":
	print("comes here")
	c.execute("SELECT * FROM users WHERE (username = '"+username+"' AND istemp = 'false')")
	print("baba")
	res = c.fetchone()
	print(res)
	if res is None:
		print("No such Email account in our database or this account is not activated")
	else:
		key = sendValidationEmail(username, password, "change")
		c.execute("UPDATE users SET Key = '"+key+"' WHERE (username = '"+username+"')")
		print("A verification Email has been sent to your address")

else:
	print("soemthing")
	print("unkown input")
conn.commit()