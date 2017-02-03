import nltk
from nltk.util import ngrams
import operator
from parser import parser
import string
import regex

def test(inputFileName):
	tweets = parser(inputFileName)
	mp=regex.any_match(tweets,[r'(?i)\bmotion picture\b'])
	comedy=regex.any_match(mp,[r'(?i)\banimated\b'])
	return extract_movie_titles(comedy)
	


#extracts movie titles
def extract_movie_titles(tweets):
	possible_movie_titles= []
	for i in range(2,5):
		dict = extract_phrase_count(tweets, i)
		dict = remove_punctuation(dict)
		queries = ['Best', 'Motion', 'Picture', 'Drama', 'or' , 'in', 'a', 'actor', 'best', 'motion', 'actress']
		dict = remove_query_type(dict, queries)
		for i in range(5):
			temp_1 = max(dict.iterkeys(), key = lambda key: dict[key])
			dict.pop(temp_1, None)
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
	return dict

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
		
def remove_query_type(dict, queries):
	remove = []	
	for phrase in dict:
		for word in phrase:
			if word in queries:
				remove.append(phrase)
	for i in remove:
		dict.pop(i, None)
	return dict
		
		
		