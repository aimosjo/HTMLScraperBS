# need to import numpy to use modulus operator
import numpy as np

# input 	> string of HTML code, each entry split by comma + number of attributes per row [n]
# output 	> list of strings, each list of length [n]

# [LATER] implement a check if there is incomplete data or incorrectly categorized data being added

def commaatt(stringofatt, n):
	# create a list of the split att
	att = stringofatt.split(',')

	# check if there will be leftover values after
	# placing the string into a list of strings of length with n attributes
	if not (np.mod(len(att),n)) == 0:
		print("Check the dimensions of the data.")
		return -1

	# check how many copies of n there are in len(att) [use this number to iterate up to, placing values]
	# should be int, since len(att)%n == 0 by check above

	# for troubleshooting, going to coerce this into an integer to see where things are going wrong
	ind = int(len(att)/n)

	# initialize the list
	att_strings = ['']
	# use for loop to make list of n-attribute strings
	for x in range(0,ind):

		# increase the list by appending another empty string to the end
		att_strings.append('')
		
		for y in range(0,n):
			# iterate over the 
			# e.g., if ind = 20, n = 3 -> 	att_string[0] = att[0] + att[1] + att[2]
			# 								att_string[1] = att[3] + att[4] + att[5]
			att_strings[x] += att[x*n + y] + ","
	
	# print(list(att_strings)[:-1])

	# only return up to the last string, since the last item will still have a ',' in place
	return list(att_strings[:-1])