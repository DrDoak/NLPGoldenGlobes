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

def get_nominees(tweets, queries):
  for query in queries:
    if 'Actor' in query.tokens or 'Actress' in query.tokens:
      get_actor_nominees(tweets, query)
    elif 'TV' in query.tokens:
      get_tv_nominees(tweets, query)
    elif 'Picture' in query.tokens or 'Film' in query.tokens:
      get_movie_nominees(tweets, query)


def get_movie_nominees(tweets, queries):
  movie_tokens = ['motion', 'picture', 'feature', 'film', 'movie']
  nomin_tokens = ['nominated', 'nominee', 'nominees', 'nomination', 'should', 'snub', 'lost', 'not', 'beat', 'robbed', 'prediction', 'over', 'better', 'would', 'could', 'hope']
  results = []

  queries_set = create_queries_set(queries)

  for query in queries:
    query_tokens = [token for token in query.tokens if token.lower() not in movie_tokens]

    movie_patterns = regex.create_patterns(movie_tokens)
    query_patterns = regex.create_patterns(query_tokens)
    nomin_patterns = regex.create_patterns(nomin_tokens)

    query_tweets = regex.all_match(tweets, query_patterns)
    movie_tweets = query_tweets # regex.any_match(query_tweets, movie_patterns)
    nominee_tweets = regex.any_match(movie_tweets,nomin_patterns)

    # unigrams = phrases.extract_ngrams(nominee_tweets, 1)
    #bigrams = phrases.extract_ngrams(nominee_tweets, 2)
    #trigrams = phrases.extract_ngrams(nominee_tweets, 3)

    # uc = Counter(unigrams)
    # bc = Counter(bigrams)
    # tc = Counter(trigrams)

    ############3
    # matched_tweets = regex.all_match(tweets, query.get_patterns())
    other_queries = queries_set.difference(query.tokens)
    other_queries_patterns = regex.create_patterns(other_queries)
    nominee_tweets = regex.exclude_any_match(nominee_tweets, other_queries_patterns)

    ####
    max_ngrams = []
    for i in range(1, 6):
      ngrams = phrases.extract_ngrams(nominee_tweets, i)
      phrases.remove_query(ngrams, query)
      phrases.remove_stopwords(ngrams)
      phrases.remove_twitter_stopwords(ngrams)
      phrases.remove_punctuation(ngrams)
      phrases.remove_keywords(ngrams,nomin_tokens)
      ngrams_count = Counter(ngrams)
      max_ngrams.append(ngrams_count.most_common(20))

    for unigram in max_ngrams[0]:
      for i in range(1, 5): 
        phrases.add_mention_hashtag_count(unigram, max_ngrams[i], mention_hashtag_weight)

    for ngrams in max_ngrams:
      ngrams.sort(key=lambda x: x[1], reverse=True)

    print "-----"

    finalStr = ' '
    for rank in range(0,10):
      finalStr = '\n' + finalStr + str(rank) + ': '
      winner = 'none'
      for i in range(0, 5):
        if (i+1 >= len(max_ngrams) or len(max_ngrams[i]) <= rank or len(max_ngrams[i+1]) <= rank):
          continue
        if i < 4 and ngram_threshold * max_ngrams[i][rank][1] > max_ngrams[i+1][rank][1]:
          winner = ' '.join(max_ngrams[i][rank][0])
          break
        else:
          winner = ' '.join(max_ngrams[i][rank][0])
      finalStr = finalStr + winner + '\n'
    results.append(Result(query.unparsed, finalStr))
    print finalStr
  return results

def get_tv_nominees(tweets, query):
  tv_tokens = ['tv', 'television', 'series']

def get_actor_nominees(tweets, query):
  actor_tokens = ['actor', 'actress']


def create_queries_set(queries):
  queries_set = set()
  for query in queries:
    queries_set.update(query.tokens)
  return queries_set
