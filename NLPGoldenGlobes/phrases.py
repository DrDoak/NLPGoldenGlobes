import nltk
from nltk.util import ngrams
import string

def extract_unigrams(tweets):
  phrases_dict = phrase_count(tweets, 1)
  return remove_punctuation(phrases_dict)

def extract_ngrams(tweets):
  all_phrases_dict = {}
  for i in range(2, 6):
    phrases_dict = phrase_count(tweets, i)
    phrases_dict = remove_punctuation(phrases_dict)
    all_phrases_dict.update(phrases_dict)
  return all_phrases_dict 

#extracts phrases
def phrase_count(tweets, length):
  phrases_dict = {}
  for tweet in tweets:
    tokens = nltk.word_tokenize(tweet.content)
    phrases = ngrams(tokens, length)
    for phrase in phrases:
      phrases_dict[phrase] = phrases_dict.get(phrase, 0) + 1
  return phrases_dict

#removes phrases that have punctuation; presumably phrases with punctuation
#are not movie titles
def remove_punctuation(phrases_dict):
  remove = [] 
  for phrase in phrases_dict:
    for word in phrase:
      if word in string.punctuation:
        remove.append(phrase)
  for i in remove:
    phrases_dict.pop(i, None)
  return phrases_dict
    
def remove_query_type(phrases_dict, queries):
  remove = [] 
  for phrase in phrases_dict:
    for word in phrase:
      if word in queries:
        remove.append(phrase)
  for i in remove:
    phrases_dict.pop(i, None)
  return phrases_dict
    