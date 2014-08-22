# Scraper to collect post info from the Drury University Humanities blog

from BeautifulSoup import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 

# Base page
page_to_scrape = 'http://humanities.drury.edu'

#What info do we want? 
headers = ["url","is_post", "publish_date", "author", "post_title", "comment_count"]

#Where do we save info?
filename = "DU_posts.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

#Use these in making sure the right things get scraped
links = []
links2 = []
visited = []
links_index = 0 

#keep looking while there are unvisited links and while you haven't started
while ((len(links2) + 1) != len(visited) ) or (len(visited) == 0):
		
	#where are we now?
	print page_to_scrape
	
	#keep track of where you've been
	visited.append(page_to_scrape) #add the current page to places you've been
	
	#open current page
	webpage = urllib2.urlopen(page_to_scrape)

	# Parse it
	soup = BeautifulSoup(webpage.read())
	soup.prettify()

	#add all links to posts and other pages of posts on current page to links list
	for link in soup.findAll("h1", attrs = {'class':'post-title'}):
  		links.append(link.find("a").get('href'))
  	for link in soup.findAll("div", attrs = {'class':'pagenav clearfix'}):
  		for ref in link.findAll("a"): #not sure how this could've been not a nested for loop. 
  			links.append(ref.get("href"))
  
  	#add all links on current page that haven't been visited and aren't already on the list
  	#inspiration for this step taken from David Carlson's code
	for link in links:
		if (link not in links2) and (link not in visited):
			links2.append(link)

	if len(soup.findAll(content = "article")) != 0: #is it a post? If so add info and if not move to next
		is_post = True
		date = soup.findAll("time", attrs = {'class':"post-date"})
		for i in date:
			post_date =  clean_html(str(i))
		author = soup.findAll("a", attrs = {'rel':"author"})
		for i in author:
			post_author =  clean_html(str(i))	
		title = soup.findAll("h1", attrs = {'class':'post-title'})
		for i in title:
			post_title =  clean_html(str(i))
		comments = soup.findAll("span", attrs = {'class':'post-comment'})
		for i in comments:
			post_comments =  clean_html(str(i))
			if post_comments == "No Comments":
				post_comments = 0
		csvwriter.writerow([page_to_scrape, is_post, post_date, post_author, post_title, post_comments]) #Write these to the CSV  
	else:
		csvwriter.writerow([page_to_scrape, False, None, None, None, None]) #Write these to the CSV
	
	if ((len(links2) + 1) == len(visited) ):
		break
		
	#get the next page on the list	
	page_to_scrape = links2[links_index] 
	links_index += 1

readFile.close()