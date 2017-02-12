import regex
import phrases
from collections import Counter
from result import Result
import parser
import names

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

def get_queries(queries):
  list_optional = ['movie', 'feature','film','tv','televion']
  list_mandatory = [all tokens in queries.tokens if tokens.lower() not in list_optional]
  mandatory_patterns = regex.create_patterns(movie_tokens)
  query_patterns = regex.create

  return None


def get_presenters(tweets, queries,category):
  results_w = []
  results_a = []
  results = []
  winners = get_winners(tweets, queries)
  award_names = []
  print "Finished getting winners"
  winner_queries = parser.parse_result(winners)
  winner_queries = winner_queries +queries
  #is the award_names a list?
  for winner in winner_queries:
    matched_tweets = regex.all_match(tweets, winner.get_patterns())
    matched_tweets = regex.any_match(matched_tweets, category.get_patterns())
    #print category.tokens
    #print winner.tokens
    #print winner.excludewords
    #print "Length of tweets" + str(len(matched_tweets))
    dict_names = names.count_names(matched_tweets)
  #  print names.most_frequent_name(matched_tweets)
    presenter = ' '.join(names.most_frequent_name(matched_tweets))
    if winner in queries:
    	results_a.append(dict_names)
    else:
    	results_w.append(dict_names)
  for i in range(len(results_a)):
    results_w[i].update(results_a[i])
    d = Counter(results_w[i])
    d = d.most_common(3)
    results.append(d)
  import pdb; pdb.set_trace()
  return d


