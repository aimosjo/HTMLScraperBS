# import requests library so user can connect to url
import requests

#import url2domain script so user can scrape the domain name from the url
import url2domain

# import os library so user can return current working directory (needed for later
# operating on the html file)
import os

# [LATER] check that user can connect to URL, otherwise return message to try again later

def urlToHTML(url):
	# call url2domain and use function to name the html file appropriately
	# [LATER] add time stamp function to this s.t. the saved html file will not be overwritten
	webname = url2domain.urlToDomain(url) + ".html"

	# use requests library to scrape the HTML text from the website
	r = requests.get(url)

	# get current directory so this can be passed to next function
	# which will use it to find the saved html file
	current_dir = os.getcwd()

	# save the scraped html text to file for use later
	Html_file= open(webname,"w")
	Html_file.write(r.text)
	Html_file.close()

	# After HTML file is written to current directory, return this path s.t. the next function
	# can find it and operate on it
	return(current_dir + "/" + webname)