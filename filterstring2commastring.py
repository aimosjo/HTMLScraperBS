def commastring(filterstring, split1=None, split2=None):
	split_list = filterstring.split(split1)

	# Check to make sure it's functioning
	# print(list(split_list))
	split_str = ""

	# Using for loop, store the split_list in a single string, skipping the empty lines
	for x in range(0, len(split_list)):
		if not split_list[x] == '':
			split_str += split_list[x] + ","

	# Return the full string where each attribute is separated by a single comma
	return split_str
