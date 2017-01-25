from tweet import Tweet

def parser(inputFileName):
	list_tweets= []
	with open(inputFileName, 'r') as datasource:
		for tweet in datasource:
			list_tokens = tweet.split('\t')
			if len(list_tokens)<5:
				continue
			content = list_tokens[0]
			authorID = list_tokens[2]
			authorName = list_tokens[1]
			tweetID = list_tokens[3]
			dateTime = list_tokens[4].rstrip()
			new_tweet = Tweet(tweet, content,authorID,authorName,tweetID, dateTime)
			list_tweets.append(new_tweet)
	return list_tweets

			


