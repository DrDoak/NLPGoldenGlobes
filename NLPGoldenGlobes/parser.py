#import sys
from tweet import Tweet
def parser(inputFileName):
	list_tweets= []
	#a = Tweet('a','a','a','a','a','2017-01-09 03:16:33')
	#print a.content
	with open(inputFileName, 'r') as datasource:
		for tweets in datasource:
			list_tokens = tweets.split('\t')
			print list_tokens
			content = list_tokens[0]
			authorID = list_tokens[2]
			authorName = list_tokens[1]
			tweetID = list_tokens[3]
			dateTime = list_tokens[4].rstrip()
			#import pdb;pdb.set_trace()
			new_tweet = Tweet(tweets, content,authorID,authorName,tweetID, dateTime)
			list_tweets.append(new_tweet)
	return list_tweets

			


