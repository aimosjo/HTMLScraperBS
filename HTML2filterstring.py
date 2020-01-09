from bs4 import BeautifulSoup
import os

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
		lines += filteredSoup[x].get_text() + ","
		# print(filteredSoup[x].get_text())
	#filtSoupType = type(soup.find_all(tag, id=cssid))
	

	return(lines)
