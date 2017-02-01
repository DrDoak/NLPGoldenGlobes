#A General Python Class intended to represent the contents of a single tweet

# Format of a tweet:
# Text: Contents of the tweet as a string
# 
from datetime import datetime

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

  def has_word(self, targetWord):
    words = self.content.split(' ')
    for word in words:
      if word == targetWord:
        return True
    return False