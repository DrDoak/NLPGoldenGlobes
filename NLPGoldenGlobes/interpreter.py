import regex
import phrases
from collections import Counter
from result import Result
import parser


ngram_threshold = 0.75

def get_winners(tweets, queries):
  results = []

  for query in queries:
    matched_tweets = regex.all_match(tweets, query.get_patterns())
    unigrams = phrases.extract_unigrams(matched_tweets)
    ngrams = phrases.extract_ngrams(matched_tweets)

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


def get_presenters(tweets, queries,category):
  results = []
  winners = get_winners(tweets, queries)
  print "Finished getting winners"
  winner_queries = parser.parse_result(winners)
  for winner in winner_queries:
    matched_tweets = regex.all_match(tweets, winner.get_patterns())
    matched_tweets = regex.all_match(matched_tweets, category.get_patterns())

    unigrams = phrases.extract_unigrams(matched_tweets)
    ngrams = phrases.extract_ngrams(matched_tweets)

    phrases.remove_query(unigrams, winner)
    phrases.remove_query(ngrams, winner)

    phrases.remove_query(unigrams, category)
    phrases.remove_query(ngrams, category)

    phrases.remove_stopwords(unigrams)
    phrases.remove_stopwords(ngrams)

    phrases.remove_twitter_stopwords(unigrams)
    phrases.remove_twitter_stopwords(ngrams)

    unigrams_count = Counter(unigrams)
    ngrams_count = Counter(ngrams)
    import pdb;pdb.set_trace()
    
    if unigrams_count and ngrams_count:
      max_unigram = unigrams_count.most_common(1)[0]
      max_ngram = ngrams_count.most_common(1)[0]

      max_unigram_phrase = max_unigram[0][0]
      max_unigram_count = max_unigram[1]

      max_ngram_phrase = max_ngram[0]
      max_ngram_count = max_ngram[1]

      if (max_unigram_phrase in max_ngram_phrase) or (max_ngram_count > ngram_threshold * max_unigram_count):
        presenter = ' '.join(max_ngram_phrase)
      else:
        presenter = max_unigram_phrase
      results.append(Result(winner.unparsed, presenter))
  return results
