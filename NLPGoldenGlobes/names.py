import nltk
import re

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
