#!/usr/bin/python

head = """Content-type: text/html

"""
id = 1
origin = """<head><meta http-equiv="refresh" content="1;url=home.cgi"></head>"""
redir = "<head><meta http-equiv=\"refresh\" content=\"1;url=home.cgi?"
uid = str(id)
add = "\"></head>"

print(head)
print(redir + uid + add)

conn.commit()
