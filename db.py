#!/usr/bin/python
# type ./db.py to execute file

import MySQLdb
db = MySQLdb.connect(host="localhost",
			user="root",
			passwd="zzz",
			db="test")
print("Connected to database succesfully.")

cur = db.cursor()

cur.execute("INSERT INTO PogChamp (name) VALUES('Google')")
cur.execute("SELECT * FROM PogChamp")

for row in cur.fetchall():
	print row
cur.close()
db.commit()
db.close()
