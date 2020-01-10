# takes in a table and reports back the schema of the table
import getpath
import sqlite3

def formcheck(fname, tname):
	# fname is the name of the database
	# tname is the name of the table inside the database to be checked

	"""Return a string representing the table's CREATE"""
	conn = sqlite3.connect(fname + ".db")
	cursor = conn.execute("SELECT sql FROM sqlite_master WHERE name=?;", [tname])
	sql = cursor.fetchone()[0]
	cursor.close()
	print(sql)