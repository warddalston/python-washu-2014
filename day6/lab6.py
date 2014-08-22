# Scraper to collect petition info from petitions.whitehouse.gov

#pip install....

from BeautifulSoup import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 

# What page? 
page_to_scrape = 'https://petitions.whitehouse.gov/petitions'

# What info do we want? 
headers = ["Summary", "Signatures"]

# Where do we save info?
filename = "whitehouse-petitions.csv" #what to name a file
readFile = open(filename, "wb") # make this file, say what can be done to it ("wd")
csvwriter = csv.writer(readFile) #now declare that file as a csv
csvwriter.writerow(headers) #write the first row of the CSV 

# Open webpage
webpage = urllib2.urlopen(page_to_scrape) 

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

# Extract petitions on page
#petitions = soup.findAll("a", href=re.compile('^/petition'))
petitions = soup.findAll("div", attrs={'class':'title'}) #find petitions 
print len(petitions)
for petition in petitions:
  p = clean_html(str(petition.find("a"))) #clean out their strings? 
  print p

signatures = soup.findAll("div", attrs={'class':'num-sig'})
print len(signatures)
for signature in signatures:
  s = clean_html(str(signature.find("span", attrs={'class':'num'})))
  print s

for i in range(20):
  petition = petitions[i]
  p = clean_html(str(petition.find("a")))
  signature = signatures[i]
  s = clean_html(str(signature.find("span", attrs={'class':'num'})))
  csvwriter.writerow([p, s]) #Write these to the CSV  

readFile.close()