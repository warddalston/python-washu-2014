#Register an app: https://dev.twitter.com/

#pip install tweepy
import time
import tweepy

#First parameter is Consumer Key, second is Consumer Secret 
auth = tweepy.OAuthHandler('your consumer key', '')
auth.set_access_token('your consumer secret', '')    
api = tweepy.API(auth)

#See rate limit
api.rate_limit_status()

# #Get all tweets, https://dev.twitter.com/docs/api/1/get/statuses/public_timeline
# public_tweets = api.public_timeline()
# for t in public_tweets:
#   #Note I am handling UTF encoded strings so I convert them to ASCII-compatible for my mac
#   print "{0}: {1}".format(t.user.screen_name.encode('ascii', 'ignore'), t.text.encode('ascii', 'ignore'))

#Get some user
target = api.get_user('kiethschnak')

followers = []
for page in tweepy.Cursor(api.followers, screen_name=target.screen_name).pages():
    followers.extend(page)
    
for f in followers:
  #Note I am handling UTF encoded strings so I convert them to ASCII-compatible for my mac
  print "{0}".format(f.screen_name.encode('ascii', 'ignore'))


#### prints everything 
targets_followers = {}
#the .items bit says how many users to look at 
for user in tweepy.Cursor(api.followers, screen_name=target.screen_name).items():
     targets_followers[user.screen_name] = user.followers_count
     time.sleep(5)

#prints the user's followers 
for user in targets_followers.keys():
	if targets_followers[user] == max(targets_followers.values()):
		print user
		
		