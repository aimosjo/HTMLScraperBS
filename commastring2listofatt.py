# need to import numpy to use modulus operator
import numpy as np

# input 	> string of HTML code, each entry split by comma + number of attributes per row [n]
# output 	> list of strings, each list of length [n]

# [LATER] implement a check if there is incomplete data or incorrectly categorized data being added

def commaatt(stringofatt, n):
	# create a string of the split att
	att = stringofatt.split(',')

	# check if there will be leftover values after
	# placing the string into a list of strings of length with n attributes
	
	## turn this back on!!
	##if not (np.mod(len(att),n)) == 0:
	##	print("Check the dimensions of the data.")
	##	return -1

	# check how many copies of n there are in len(att) [use this number to iterate up to, placing values]
	# should be int, since len(att)%n == 0 by check above
	ind = len(att)/n

	# initialize the array
	att_strings = []
	# use for loop to make list of n-attribute strings
	for x in range(0,ind):
		for y in range(0,n):
			# att_strings[x*n] += att[x*n + y]
			print(x*n + y)