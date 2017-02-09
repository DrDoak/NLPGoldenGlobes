import regex
import phrases
from collections import Counter
from result import Result
import string

xgram_threshold = 0.49
mention_hashtag_weight = 0.15

def get_winners(tweets, queries):
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
        max_xgrams.append(xgrams_count[ii].most_common(20))

      for unigram in max_xgrams[0]:
        for ii in range(1,5):
          add_mention_hashtag_count(unigram, max_xgrams[ii], mention_hashtag_weight)

      for ii in range(0,5):
        if ii < 4 and xgram_threshold * max_xgrams[ii][0][1] > max_xgrams[ii+1][0][1]:
          winner = ' '.join(max_xgrams[ii][0][0])
          break
        else:
          winner = ' '.join(max_xgrams[ii][0][0])

      results.append(Result(query.unparsed, winner))

  return results

def create_queries_set(queries):
  queries_set = set()
  for query in queries:
    queries_set.update(query.tokens)
  return queries_set

def add_mention_hashtag_count(unigram, ngrams, weight):
  unigram_phrase = unigram[0][0].lower()
  unigram_count = unigram[1]

  for idx, ngram in enumerate(ngrams):
    ngram_phrase = ''.join(ngram[0]).lower().translate(None, string.punctuation)
    ngram_count = ngram[1]
    if unigram_phrase == ngram_phrase:
      updated_count = ngram_count + weight * unigram_count
      updated_ngram = (ngram[0], updated_count)
      ngrams[idx] = updated_ngram
