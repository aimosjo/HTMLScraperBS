from bs4 import BeautifulSoup
# import os - don't need this yet?

# parameters are htmlstring (opened file), cssid is the id class from CSS, tag are the tags ('a', 'p'),
# and class_ is the CSS class (all found by looking in the HTML doc)
def filterHTML(htmlstring, cssid=None, tag=None, class_=None):
	#parse the HTML code using BeautifulSoup, so we can filter the HTML by cssid and tags
	soup = BeautifulSoup(open(htmlstring), 'html.parser')

	# store the result of the soup's filtered contents in a string
	# user will need to inspect webpage and HTML to find appropriate parameters
	filteredSoup = soup.find_all(tag, id=cssid, class_=class_)

	lines = ""
	# print(len(filteredSoup))

	for x in range(0, len(filteredSoup)):
		# 

		# check if any parts of text are "," and replace them with nothing (expecting , as separator between
		# hundreds of numbers)
		check = filteredSoup[x].get_text().split(',')

		# initialize string to be put together without commas
		value = ""
		for y in range(0,len(check)):
			value += check[y]

		# #check if any parts of text are "	" and replace them
		# check = value[x].split('	')

		# # initialize string to be put together with "	"
		# new_value = ""
		# for x in range(0,len(value)):
		# 	new_value += value[x]

		# if using tab check, change value to new_value 
		lines += value + ","
		# print(filteredSoup[x].get_text())

	#filtSoupType = type(soup.find_all(tag, id=cssid))
	
	# only return up to the second last character since the last one will be a ","
	return(lines[:-1])
