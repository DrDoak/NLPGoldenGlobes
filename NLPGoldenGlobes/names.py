import nltk
import re

def most_frequent_name(tweets):
  names_dict = count_names(tweets)
  return max(names_dict.iterkeys(), key=lambda key: names_dict[key])

def count_names(tweets):
  names_dict = {}
  for tweet in tweets:
    names = extract_names(tweet.content)
    for name in names:
      names_dict[name] = names_dict.get(name, 0) + 1
  return names_dict  

def extract_names(text):
  names = []
  for sent in nltk.sent_tokenize(text):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
      if type(chunk) == nltk.tree.Tree:
        if chunk.label() == 'PERSON':
          names.append(' '.join([c[0] for c in chunk]))
  return names
  
def extract_handles(text):
  return re.findall(r'@(\w+)', text)      