import nltk
from nltk.util import ngrams
import operator
from parser import parser
import string

def test(inputFileName):
	tweets = parser(inputFileName)
	tweets = tweets[:10000]
	return extract_movie_titles(tweets)
	


#extracts movie titles
def extract_movie_titles(tweets):
	possible_movie_titles= []
	for i in range(2,5):
		list = extract_phrase_count(tweets, i)
		for i in range(5):
			temp_1 = max(list.iterkeys(), key = lambda key: list[key])
			list.pop(temp_1, None)
			possible_movie_titles.append(temp_1)
	return possible_movie_titles
		


#extracts phrases
def extract_phrase_count(tweets, length):
	dict = {}
	for tweet in tweets:
		t = nltk.word_tokenize(tweet.content)
		phrases = ngrams(t, length)
		for phrase in phrases:
			if phrase in dict:
				dict[phrase] +=1
			else:
				dict[phrase] = 1
	return remove_punctuation(dict)

#removes phrases that have punctuation; presumably phrases with punctuation
#are not movie titles
def remove_punctuation(dict):
	remove = []	
	for phrase in dict:
		for word in phrase:
			if word in string.punctuation:
				remove.append(phrase)
	for i in remove:
		dict.pop(i, None)
	return dict
		
	
		
		