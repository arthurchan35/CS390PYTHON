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

username = form.getvalue('username')
newpassword = form.getvalue('newpassword')
key = form.getvalue('key')
mode = form.getvalue('mode')
if mode == "create":
	c.execute("SELECT istemp FROM users WHERE (username = '"+username+"' AND key = '"+key+"')")
	res = c.fetchone()
	if res is None:
		c.execute("DELETE FROM users WHERE (username = '"+username+"')")
		print ("Invalid key, return to login page")
		
	elif res == "true":
		c.execute("UPDATE users SET (password = '"+newpassword+"', istemp = 'false', Key = NULL) WHERE (username = '"+username+"')")
		print ("Accout created!")

	elif res == "false":
		print ("database error, please contact admin")

elif mode == "change":
	c.execute("SELECT istemp FROM users WHERE (username = '"+username+"' AND key = '"+key+"')")
	res = c.fetchone()
	if res is None:
		print("This user didn't ask for a password change")
		
	elif res == "true":
		c.execute("UPDATE users SET (password = '"+newpassword+"', istemp = 'false', key = NULL) WHERE (username = '"+username+"')")
		print ("Accout created!")

	elif res == "false":
		print ("database error, please contact admin")

	
else:
	print("unknown command")

conn.commit()