#!/usr/bin/python
# Copyright 2018 - Drew Mahler andrew.h.mahler@gmail.com

'''
General Framework for analyzing tweets 
	1. Reads all tweet files into a list of tweet objects
		--> Tweet object: tweet information + User Object
'''
import json

class TwitterUser():
	def __init__(self, screenname, profilename, user_id, user_since):
		self.screenname = screenname
		self.profilename = profilename
		self.id = user_id
		self.since = user_since

class Tweet():
	# Note to self: objects can inherit! And its useful
	def __init__(self, tweet, tweeted_at, result_type, screenname, profilename, user_id, user_since):
		self.tweet = tweet
		self.tweeted_at = screenname
		self.result_type = result_type
		self.user = TwitterUser(screenname, profilename, user_id, user_since)

def tweetunpacking(filelist):
	# Create a list with all of the tweets
	tweets = []
	for json_file in filelist:
		with open(json_file) as json_data:
		    outermost = json.load(json_data)
		    current_tweets = outermost['statuses']
		    for tweet in current_tweets:
		    	user = tweet['user']
		    	metadata = tweet['metadata']
		    	tweet = Tweet(tweet['text'], tweet['created_at'], metadata['result_type'], \
		    		          user['screen_name'], user['name'], user['id'], user['created_at'])
		    	tweets.append(tweet)
	
	# Tweets hierarchy - high level
	## file (dictionary) -> key: search-metadata (dictionary)
	##                   -> key: statuses (AKA tweets) (list of dictionaries) -> tweet (dictionary) -> user (dictionary)                                   

	# A list of tweets
	return tweets
