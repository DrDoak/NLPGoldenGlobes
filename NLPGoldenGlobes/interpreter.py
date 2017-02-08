import regex
import phrases
from collections import Counter
from result import Result

ngram_threshold = 0.75
xgram_threshold = 0.75

def get_winners(tweets, queries):
  results = []
  queries_set = create_queries_set(queries)

  for query in queries:
    matched_tweets = regex.all_match(tweets, query.get_patterns())
    other_queries = queries_set.difference(query.tokens)
    other_queries_patterns = regex.create_patterns(other_queries)
    matched_tweets_minus_other_queries = regex.exclude_any_match(matched_tweets, other_queries_patterns)

    unigrams = phrases.extract_unigrams(matched_tweets_minus_other_queries)
    ngrams = phrases.extract_ngrams(matched_tweets_minus_other_queries)

    phrases.remove_query(unigrams, query)
    phrases.remove_query(ngrams, query)

    phrases.remove_stopwords(unigrams)
    phrases.remove_stopwords(ngrams)

    phrases.remove_twitter_stopwords(unigrams)
    phrases.remove_twitter_stopwords(ngrams)

    unigrams_count = Counter(unigrams)
    ngrams_count = Counter(ngrams)

    if unigrams_count and ngrams_count:
      max_unigram = unigrams_count.most_common(1)[0]
      max_ngram = ngrams_count.most_common(1)[0]

      max_unigram_phrase = max_unigram[0][0]
      max_unigram_count = max_unigram[1]

      max_ngram_phrase = max_ngram[0]
      max_ngram_count = max_ngram[1]

      if (max_unigram_phrase in max_ngram_phrase) or (max_ngram_count > ngram_threshold * max_unigram_count):
        winner = ' '.join(max_ngram_phrase)
      else:
        winner = max_unigram_phrase
      results.append(Result(query.unparsed, winner))

  return results

def get_winners_xgrams(tweets, queries):
  results = []
  queries_set = create_queries_set(queries)

  for query in queries:
    matched_tweets = regex.all_match(tweets, query.get_patterns())
    other_queries = queries_set.difference(query.tokens)
    other_queries_patterns = regex.create_patterns(other_queries)
    matched_tweets_minus_other_queries = regex.exclude_any_match(matched_tweets, other_queries_patterns)

    xgrams = []
    xgrams_count = []
    for ii in range(1,6):
      xgrams.append(phrases.extract_xgrams(matched_tweets_minus_other_queries,ii))

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
          winner = ' '.join(max_xgrams[ii][0][0])

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

def create_queries_set(queries):
  queries_set = set()
  for query in queries:
    queries_set.update(query.tokens)
  return queries_set
