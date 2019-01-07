from twitter_framework import Tweet
from twitter_framework import tweetunpacking

# TO DO: Get bash script working to rapidly query from the API
#        Have q= be input 1 and the output file to be input 2
# 	 Run the query as much as possible before the API kicks you off
# 	 Schedule it to run every day
jovan_list = []
for i in range(1, 5):
	jovan_list.append("jovan{}.json".format(i))

print (jovan_list)
all_tweets = tweetunpacking(jovan_list)
users = []
for tweet in all_tweets:
	users.append(tweet.user.screenname)

print (len(users))
