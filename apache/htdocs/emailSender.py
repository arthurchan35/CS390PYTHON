#! /usr/bin/python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from randomString import id_generator
def sendValidationEmail(addr, pw, mode):
	me = "support@mylink.com"
	you = addr
	key = id_generator()
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Link"
	msg['From'] = me
	msg['To'] = you
	htmlpart1 = """\
		<html>
		<head></head>
		<body>
			<p>Hi!<br>
			How are you?<br>
			Here is the <a href="http://borg05.cs.purdue.edu:3141/validate.cgi?"""
	htmlpart2 = ""
	html = ""

	if mode == "create":
		htmlpart2 = """">link</a> to validate your Email.<br><br>
			Thanks for joining MyLink!<br>
			- The world's leading social website
			</p>
		</body>
		</html>
		"""	
		html = htmlpart1 + "username=" + addr + "&newpassword=" + pw + "&key=" + key + "&mode=create" + htmlpart2

	elif mode == "change":
		htmlpart2 = """">link</a> to change your password.<br><br>
			MyLink<br>
			- The world's leading social website
			</p>
		</body>
		</html>
		"""
		html = htmlpart1 + "username=" + addr + "&newpassword=" + pw + "&key=" + key + "&mode=change" + htmlpart2
	
	else:
		print("unkown command")



	part2 = MIMEText(html, 'html')

	msg.attach(part2)

	s = smtplib.SMTP('localhost')
	s.sendmail(me, you, msg.as_string())
	s.quit()
	return key