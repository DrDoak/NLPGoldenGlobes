#A General Python Class intended to represent the contents of a single tweet

# Format of a tweet:
# Text: Contents of the tweet as a string
# 
import nltk
from datetime import datetime

bannedWords = ["RT","http","https","to","the"]
bannedPrefixes = ["//"]


class Tweet:
  def __init__(self,unparsed, content,authorID,authorName,tweetID, dateTime):
    self.unparsed = unparsed
    self.content = content
    self.authorID = authorID
    self.authorName = authorName
    self.tweetID = tweetID
    self.dateTime = datetime.strptime(dateTime,'%Y-%m-%d %H:%M:%S')
    self.tf = {}
    self.tfidf = {}
    self.tokens = []
    self.createTokens()

  def has_word(self, targetWord):
    words = self.content.split(' ')
    for word in words:
      if word == targetWord:
        return True
    return False

  def createTokens(self):
    global bannedPrefixes, bannedWords
    candidateTokens = nltk.word_tokenize(self.content)
    for token in candidateTokens:
      if len(token) > 1 and not token in bannedWords:
        for testPrefix in bannedPrefixes:
          if not token[0:len(testPrefix)] == testPrefix:
            self.tokens.append(token)