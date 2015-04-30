#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('mylink.db')
c = conn.cursor()

#c.execute("INSERT INTO users (username, password) VALUES ('timd', 'sanspurs')")
for a in c.execute('SELECT * FROM users') :print a
conn.commit()