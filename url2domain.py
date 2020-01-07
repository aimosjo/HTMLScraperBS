import tldextract

# url = input("Enter website's url:")

def urlToDomain(url):
	# create tldextract objects to get the domain, subdomain and suffix from the url
	ext = tldextract.extract(url)

	# use the tldextract objects to rejoin domain + subdomain + suffix for URLs
	website = '.'.join(ext[0:3])
	return(website)