# use this function to create a database in the specified location,
# after doesdbexist is ran

''' 
:param fpath def: location of new database to be created; can be null, so that database
is saved in current folder where .py function is called from
:param fname def: name of new database

'''

import sqlite3

def createDB(fname, fpath = None):
	# [LATER] want to implement a path so database can be created in new
	# location if desired
	conn = sqlite3.connect("{}.db".format(fname))
	conn.commit()
	conn.close()