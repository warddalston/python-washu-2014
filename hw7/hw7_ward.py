####################
# Homework 7 - Databases - Dalston Ward - August 23 2014
####################
import csv
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

####### web scrape ############

engine = sqlalchemy.create_engine('sqlite:////Users/clockbob1/Documents/PythonTraining/python-washu-2014/hw7/scrape.db', echo=True)

Base = declarative_base() 

#Define some schemas: for Scrape and Source
class Scrape(Base):
  __tablename__ = 'Scrape'
  
  #Have an ID column because player attributes (name, etc) are not unique
  id = Column(Integer, primary_key=True)
  url = Column(String)
  is_post = Column(String)
  date = Column(String)
  title = Column(Integer)
  author = Column(String)  
  comments = Column(String)								
  blog = Column(Integer, ForeignKey("Source.id")) #this is a primary key in another table 
  
  def __init__(self, url, is_post, date, title, author, comments):
    self.url = url
    self.is_post = is_post
    self.date = date
    self.title = title.decode('ascii','ignore')
    self.author = author
    self.comments = comments
    
  def __repr__(self):
	if self.is_post == "False":
		return "Not a post! URL: %s" % self.url
	else:
		return "Title: %s, Author: %s, URL: %s" % (self.title, self.author, self.url)
		
class	Source(Base):
	__tablename__ = 'Source' #for relationships this little line needs to match up with the foreign key call
	
	id = Column(Integer, primary_key = True)
	title = Column(String)
	url = Column(String)
	posts = relationship('Scrape') #one Source, many scrapess 
	
	def __init__(self, title, url):
		self.title = title.decode('ascii', 'ignore')
		self.url = url
	
	def __repr__(self):
		return "Blog: %s, URL: %s" % (self.title, self.url)

# First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

#this is the blog I scraped.  make it and add it to the session 
DU_humanities = Source("Human, all-too-Human", "http://www.humanities.drury.edu")
session.add(DU_humanities)

#posts are stored in this CSV.  Open it.
with open('DU_posts.csv', 'rb') as f:
  my_reader = csv.reader(f)
  my_reader.next()
  for row in my_reader: #add the posts as entries on the post table with a relationship to DU_humanities on the blog table. 
	 DU_humanities.posts.append(Scrape(row[0], row[1], row[2], row[4], row[3], row[5]))

#print them out to make sure they've all worked as expected 	
for scrape, source in session.query(Scrape, Source).filter(Scrape.is_post == "True"):
  print source
 
for source in session.query(Source):
	print source
	
session.commit()   #save this session and move onto twitter   


##########
# Twitter
##########
     
engine = sqlalchemy.create_engine('sqlite:////Users/clockbob1/Documents/PythonTraining/python-washu-2014/hw7/twitter.db', echo=True)

Base = declarative_base() 

#Define some schemas.  Friend and Followers tables have the data.  They have foreign keys to a crawl table.  Each crawl then has a foreign key to a user on the user table. Why? Users can be crawled multiple times, and each crawl obtains data on several friends and followers.  
class Friend(Base):
  __tablename__ = 'Friend'
  
  #Have an ID column because player attributes (name, etc) are not unique
  id = Column(Integer, primary_key=True)
  screen_name = Column(String)
  tweets = Column(Integer)
  favourites = Column(Integer)						
  crawl = Column(Integer, ForeignKey("Crawl.id")) #this is a primary key in another table 
  
  def __init__(self, screen_name, tweets, favourites):
    self.screen_name = screen_name
    self.tweets = tweets
    self.favourites = favourites
    
  def __repr__(self):
	return "%s has posted %s tweets and favourited %s tweets" % (self.screen_name, self.tweets, self.favourites)

#Define some schemas
class Follower(Base):
  __tablename__ = 'Follower'
  
  #Have an ID column because player attributes (name, etc) are not unique
  id = Column(Integer, primary_key=True)
  screen_name = Column(String)
  followers = Column(Integer)					
  crawl = Column(Integer, ForeignKey("Crawl.id")) #this is a primary key in another table 
  
  def __init__(self, screen_name, followers):
    self.screen_name = screen_name
    self.followers = followers
    
  def __repr__(self):
	return "%s has %s followers" % (self.screen_name, self.followers)
		
class	User(Base):
	__tablename__ = 'User' #for relationships this little line needs to match up with the foreign key call
	
	id = Column(Integer, primary_key = True)
	screen_name = Column(String)
	crawls = relationship('Crawl')
	
	def __init__(self, screen_name):
		self.screen_name = screen_name
	
	def __repr__(self):
		return "%s has a Twitter!" % (self.screen_name)

class Crawl(Base):
	__tablename__ = 'Crawl'
	
	id = Column(Integer, primary_key = True)
	date = Column(String)
	user = Column(Integer, ForeignKey('User.screen_name'))
	friends = relationship('Friend')
	followers = relationship('Follower')
		
	def __init__(self, date):
		self.date = date
		
	def __repr__(self):
		return "We crawled %s's page on %s." % (self.user, self.date)
		
# First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

Keith = User("keithschnak") #create an entry on the users table for keith 
myCrawl = Crawl("Aug-22-2014") #create a crawl

session.add(Keith) #save Keith to the session. 

#open the csv of people following Keith
with open('followers.csv', 'rb') as f:
  my_reader = csv.reader(f)
  my_reader.next()
  for row in my_reader:
	 myCrawl.followers.append(Follower(row[0], row[1])) #append these as followers to a row on the crawl table.

#open my csv of people keith follows
with open('friends.csv', 'rb') as f:
  my_reader = csv.reader(f)
  my_reader.next()
  for row in my_reader:
	 myCrawl.friends.append(Friend(row[0], row[1], row[2])) #append these as friends to a row on the crawl table

Keith.crawls.append(myCrawl) #append the row of the crawl table to a row on the users table.  
	 
#print the followers	 	
for follower in session.query(Follower):
  print follower
 
 #print the friends
for friend in session.query(Friend):
	print friend
	
#print a bit about when we crawled
for crawl in session.query(Crawl):
	print crawl
	
session.commit()        #now end the session 


	