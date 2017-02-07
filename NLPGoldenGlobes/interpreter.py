import regex
import phrases
from collections import Counter
from result import Result

ngram_threshold = 0.75

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

def create_queries_set(queries):
  queries_set = set()
  for query in queries:
    queries_set.update(query.tokens)
  return queries_set
