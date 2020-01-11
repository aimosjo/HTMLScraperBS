# this script takes in the output of commastring2listofatt, and 
# stores it in a csv file so we can add it to the sqlite db

import csv

# user should specify the name of the file, and the list of attributes

def list2csv(fname, datalist):
	# create the csv file name to be passed to the open file
	
	csvname = fname + ".csv"

	with open(csvname, 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',
			quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for x in range(0,len(datalist)):
			# format list of attributes for entry to csv file

			# print(datalist[x])

			filewriter.writerow([datalist[x]])