import tfidf as tfidf

def correlatedWords(targetWord, corpus):
  releventTweets = []
  tfidf.cache_tfidf(corpus)
  for tweet in corpus:
    if tweet.has_word(targetWord):
      releventTweets.append(tweet)

  sums = dict()
  print "total Relevant tweets", len(releventTweets)
  tweetNum = 1
  for tweet in releventTweets:
    print "tweet Num: ", tweetNum
    tweetNum = tweetNum + 1
    for wordName, tfScore in tweet.tf.items():
      if wordName != targetWord:
        if wordName in sums.keys():
          #print "old word: ", wordName
          sums[wordName] = sums[wordName] + tfScore
        else:
          #print "new word: ", wordName
          sums[wordName] = tfScore

  return sums
