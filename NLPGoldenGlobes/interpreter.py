import regex
import phrases
from collections import Counter
from result import Result

xgram_threshold = 0.75

def get_winners_xgrams(tweets, queries):
  results = []

  for query in queries:
    matched_tweets = regex.all_match(tweets, query.get_patterns())

    xgrams = []
    xgrams_count = []
    for ii in range(1,6):
      xgrams.append(phrases.extract_xgrams(matched_tweets,ii))

    for x in xgrams:
      phrases.remove_query(x,query)
      phrases.remove_stopwords(x)
      phrases.remove_twitter_stopwords(x)
      xgrams_count.append(Counter(x))

    if len(xgrams_count) > 4:
      max_xgrams=[]
      for ii in range(0,5):
        max_xgrams.append(xgrams_count[ii].most_common(5))
      for ii in range(0,5):
        if ii < 4 and max_xgrams[ii][0][1] >= 2*max_xgrams[ii+1][0][1]:
          #print max_xgrams[ii]
          winner = ' '.join(max_xgrams[ii][0][0])
          break
        #subsets
        elif ii < 4 and is_subset(xgrams[ii],xgrams[ii+1]):
          continue
        elif ii < 4 and max_xgrams[ii+1][0][1] > max_xgrams[ii][0][1]*xgram_threshold:
          continue
        else:
          einner = ' '.join(max_xgrams[ii][0][0])


      results.append(Result(query.unparsed, winner))

  return results

def is_subset(xgrams,ygrams):
  for x in xgrams:
    xgram_phrase = ' '.join(x[0][0])
    for y in ygrams:
      ygram_phrase = ' '.join(y[0][0])
      if xgram_phrase in ygram_phrase:
        return True
  return False
