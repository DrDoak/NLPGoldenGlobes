import math

def tfidf(t,d,D):
 	return tf(t, d) * math.log(1/df(t,D))

def tf(t, d):
	d = d.content
	words = d.split(' ')
	countWords = (countOccurances(t,words) * 1.0)
	div = countWords / (len(words) * 1.0)
	return div

def countOccurances(t, words):
	numOccurs = 0
	for word in words:
		if word == t:
			numOccurs = numOccurs + 1
	return numOccurs

def df(t, D):
	numDocs = 0
	for tweet in D:
		if (tf(t,tweet) > 0):
			numDocs = numDocs + 1.0
	return  numDocs/ len(D)
