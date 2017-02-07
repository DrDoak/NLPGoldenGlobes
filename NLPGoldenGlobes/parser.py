from tweet import Tweet
from query import Query
import nltk
from nltk.corpus import stopwords
import string

stops = set(stopwords.words("english"))

def parse_tweets(inputFileName):
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

def parse_queries(inputFileName):
	list_queries = []
	with open(inputFileName, 'r') as datasource:
		for query in datasource:
			tokens = nltk.word_tokenize(query)
			filtered_words = [word for word in tokens if word not in stops and word not in string.punctuation]
			new_query = Query(query.rstrip(), filtered_words)
			list_queries.append(new_query)
	return list_queries

def parse_result(results):
	list_result = []
	for result in results:
		tokens = nltk.word_tokenize(result.value)
		print tokens
		tokens += nltk.word_tokenize(result.title)

		print tokens
		filtered_words = [word for word in tokens if word not in stops and word not in string.punctuation]
		new_query = Query(result.title.rstrip(), filtered_words)
		list_result.append(new_query)
	return list_result



# finalString = ""
# for token in tokens
# 	if len(token) > 2:
# 		finalString = finalString + token + ' '
# finalString = finalString[0:(len(finalString)-1)]
# best_winners = regex.any_match(tweets,[])[3:00]

# dict = names.count_names(best_winners)[3:00]  
# sorted_winners = sorted(dict.items(), key=operator.itemgetter(1))	


