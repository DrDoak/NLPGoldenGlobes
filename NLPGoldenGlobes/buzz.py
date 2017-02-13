import parser
import names
import regex
import phrases
import result
import operator

def run_queries_buzz(tweets, queries):
  patterns = []
  results = []
  for query in queries:
      pattern = regex.create_patterns(query.tokens)
      sub_tweets = regex.all_match(tweets,pattern)
      popular_phrases = names.count_names(sub_tweets)
      #popular_phrases = names.only_bigrams(popular_phrases)
      remove_phrases = ['Twitter','Globes','Live']
      remove_phrases += query.tokens
      phrases.remove_words(popular_phrases,remove_phrases)
      names.no_monograms(popular_phrases)
      common = popular_phrases
      #common = names.n_most_common_names(popular_phrases,4)
      for c in common.keys():
          if len(c.split(' ')) < 2:
              del common[c]
      for t in query.tokens:
          for c in common.keys():
              if t in c:
                  del common[c]
      most_frequent = max(common.iteritems(), key=operator.itemgetter(1))[0]
      results.append(result.Result(query.unparsed,most_frequent))
  return results


