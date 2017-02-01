import tweet
import nltk
import operator
#extracts movie titles
def extract_movie_titles(tweets):
	for i in range(2,5):
		list = extract_phrase_count(tweets, i)
		temp_1= max(stats.iteritems(), key=operator.itemgetter(1))[0]
		list.pop(temp_1, None)
		temp_2 = 
		


#extracts phrases
def extract_phrase_count(tweets, length):
	dict = {}
	tokens = []
	for tweet in tweets:
		tokens.append(nltk.word_tokenize(tweet.content)
	for t in tokens:
		phrases = nltk.util.ngrams(token, length)
		if phrase in dict:
			dict[phrase] +=1
		else:
			dict[phrase] = 1
		
	return remove_punctuation(dict)

#removes phrases that have punctuation; presumably phrases with punctuation
#are not movie titles
def remove_punctuation(dict):
	for phrase in dict:
		if not all(word not in string.punctuation for word in phrase):
			my_dict.pop(phrase, None)
	return dict
		
	
		
		