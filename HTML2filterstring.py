from bs4 import BeautifulSoup

def filterHTML(htmlstring, cssid=None, tag=None):
	#parse the HTML code using BeautifulSoup, so we can filter the HTML by cssid and tags
	soup = BeautifulSoup(htmlstring, 'html.parser')

	# store the result of the soup's filtered contents in a string
	# user will need to inspect webpage and HTML to find appropriate parameters
	filteredSoup = soup.find_all(tag, id=cssid)
	lines = []
	print(len(filteredSoup))

	for x in range(0, len(filteredSoup)):
		lines.append(filteredSoup[x].get_text())
		# print(filteredSoup[x].get_text())
	#filtSoupType = type(soup.find_all(tag, id=cssid))
	

	return(lines)
