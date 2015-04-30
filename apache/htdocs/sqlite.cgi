#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('mylink.db')
c = conn.cursor()

#c.execute("INSERT INTO users (username, password) VALUES ('timd', 'sanspurs')")
head = """Content-type: text/html

<H1>Hello world!!!</H1>
"""
print(head)
#for row in c.execute('SELECT * FROM users') :print row
#conn.commit()