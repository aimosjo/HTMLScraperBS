# need to install wget before importing
import wget

# url = input("Enter website's url:")

# [LATER] check that user can connect to URL, otherwise return message to try again later

def urlToHTML(url):
	# use wget to download the HTML text
	down = wget.download(url)

	# create a file to hold the opened down file in read only mode
	with open(down) as f:
		htmlText = ".\n".join(f.readlines())

	# return the necessary HTML text from the webpage as a string
	return(htmlText)