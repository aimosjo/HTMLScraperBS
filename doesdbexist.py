# use os to verify if file exists in designated path
# returns true or false

# parameter fpath must be fully qualified and unambiguous, no ~/
# file extension is assumed to be .db, and should not be passed into the function check

import os

import getpath

def checkdb(fpath, fname):
	# concatenate the two strings (file path and the file name)

	f = getpath.getpath(fpath,fname)
	print(f)

	# true or false, depending if the file is in the directory
	exists = os.path.isfile(f)
	return exists