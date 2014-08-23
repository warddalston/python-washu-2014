#Homework 6  - Dalston Ward - August 2014

import time
import tweepy
import csv 

# #use this function to figure out which user is the most followed/active 
def max_finder(input):
	for user in input.keys():
		if input[user] == max(input.values()):
			return [user,input[user]]

#First parameter is Consumer Key, second is Consumer Secret 
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')    
api = tweepy.API(auth)

#See rate limit
api.rate_limit_status()

#Get some user
target = api.get_user('keithschnak')

################################
#now scrape Keith's followers ##
################################

#create CSV stuff for target's followers

#What info do we want? 
headers = ["user","N_followers"]

#Where do we save info?
filename = "followers.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)



#the .items bit says how many users to look at 
for user in tweepy.Cursor(api.followers, screen_name=target.screen_name).items():
     csvwriter.writerow([user.screen_name, user.followers_count])
     time.sleep(5)

readFile.close()

################################
#now scrape Keith's friends ####
################################


#create CSV stuff

#What info do we want? 
headers = ["user","N_tweets","N_favourites"]

#Where do we save info?
filename = "friends.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

#do the scrape 

for user in tweepy.Cursor(api.friends, screen_name=target.screen_name).items():
      csvwriter.writerow([user.screen_name, user.statuses_count, user.favourites_count])
      time.sleep(5)

readFile.close()    

#now do the calculations necessary

Keith_followers = {}
with open('followers.csv', 'rb') as f:
  my_reader = csv.reader(f)
  my_reader.next()
  for row in my_reader:
     Keith_followers[row[0]] = int(row[1])   

#most followed?       
print max_finder(Keith_followers) #['thehill', 463770]

Keith_friends = {}
with open('friends.csv', 'rb') as f:
  my_reader = csv.reader(f)
  my_reader.next()
  for row in my_reader:
     Keith_friends[row[0]] = int(row[1]) + int(row[2]) 

#most active?     
print max_finder(Keith_friends) #['HuffPostPol', 215474]

		