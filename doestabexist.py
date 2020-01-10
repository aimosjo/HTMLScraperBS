# use doesdbexist to verify if table exists in file in designated path
import doesdbexist
import sqlite3

def tablecheck(fpath, fname, tname):
	if doesdbexist.checkdb(fpath,fname):
		# only reach this point if the database exists

		# connect to the db and open cursor for access
		conn = sqlite3.connect(fname + ".db")
		c = conn.cursor()

		c.execute("SELECT count('{}') FROM sqlite_master WHERE type='table' AND name='{}'".format(tname, tname))

		# if the count is 1, then table exists
		if c.fetchone()[0] == 1:
			print("Table " + tname + " exists in " + fname + ".db")
			return True;
		else:
			print("Table " + tname + " does not exist in " + fname + ".db")
			return False;


	else:
		print("Database not found in that location, please try again.")
		return False;