# Only need to run this if there are extra '\n' valules in the string (happens)

def commastring(filterstring):
	split_list = filterstring.split('\n')

	# Check to make sure it's functioning
	# print(list(split_list))

	# Initialize the string for holding comma separated values
	split_str = ""

	# Using for loop, store the split_list in a single string, skipping the empty lines
	# on last line, need to change the addition to remove the trailing ","
	for x in range(0, len(split_list)):
		if not split_list[x] == '':
			split_str += split_list[x] + ","

	# Return the full string where each attribute is separated by a single comma except for last character
	# which will be a ","
	return split_str[:-1]
