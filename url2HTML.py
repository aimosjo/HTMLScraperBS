# import requests library so user can connect to url
import requests

#import url2domain script so user can scrape the domain name from the url
import url2domain

# [LATER] check that user can connect to URL, otherwise return message to try again later

def urlToHTML(url):
	# call url2domain and use function to name the html file appropriately
	# add time stamp function to this s.t. the saved html file will not be overwritten
	webname = url2domain.urlToDomain(url)
	webname += ".html"

	# use requests library to scrape the HTML text from the website
	r = requests.get(url)

	Html_file= open(webname,"w")
	Html_file.write(r.text)
	Html_file.close()