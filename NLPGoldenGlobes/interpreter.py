import regex
import phrases
import names
from result import Result
from collections import Counter

host_tokens = ['host', 'hosts', 'hosting', 'hosted']

ngram_threshold = 0.49
mention_hashtag_weight = 0.15
stopword_threshold = 20
stopword_weight = 0.6

def get_host(tweets):
  host_patterns = regex.create_patterns(host_tokens)
  matched_tweets = regex.any_match(tweets, host_patterns)
  host = names.most_frequent_name(matched_tweets)
  host_result = Result('Host', host)
  return host_result

def get_winners(tweets, queries):
  results = []
  queries_set = create_queries_set(queries)

  for query in queries:
    matched_tweets = regex.all_match(tweets, query.get_patterns())
    other_queries = queries_set.difference(query.tokens)
    other_queries_patterns = regex.create_patterns(other_queries)
    matched_tweets_minus_other_queries = regex.exclude_any_match(matched_tweets, other_queries_patterns)

    max_ngrams = []
    for i in range(1, 6):
      ngrams = phrases.extract_ngrams(matched_tweets_minus_other_queries, i)
      phrases.remove_query(ngrams, query)
      phrases.remove_stopwords(ngrams)
      phrases.remove_twitter_stopwords(ngrams)
      ngrams_count = Counter(ngrams)
      max_ngrams.append(ngrams_count.most_common(20))

    for unigram in max_ngrams[0]:
      for i in range(1, 5):
        phrases.add_mention_hashtag_count(unigram, max_ngrams[i], mention_hashtag_weight)

    if max_ngrams[0][0][1] < stopword_threshold:
      for ngrams in max_ngrams:
        phrases.penalize_stopwords(ngrams, stopword_weight)

    for ngrams in max_ngrams:
      ngrams.sort(key=lambda x: x[1], reverse=True)

    for i in range(0, 5):
      if i < 4 and ngram_threshold * max_ngrams[i][0][1] > max_ngrams[i+1][0][1]:
        winner = ' '.join(max_ngrams[i][0][0])
        break
      else:
        winner = ' '.join(max_ngrams[i][0][0])

    results.append(Result(query.unparsed, winner))

  return results

def create_queries_set(queries):
  queries_set = set()
  for query in queries:
    queries_set.update(query.tokens)
  return queries_set
