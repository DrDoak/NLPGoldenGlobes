import parser
import names
import regex
import phrases

def run_queries(tweets_file, queries_file):
  tweets = parser.parse_tweets(tweets_file)
  queries = parser.parse_queries(queries_file)
  patterns = []
  for query in queries:
      pattern = regex.create_patterns(query.tokens)
      sub_tweets = regex.all_match(tweets,pattern)
      popular_phrases = names.count_names(sub_tweets)
      remove_phrases = ['Twitter','Globes','Live']
      remove_phrases += query.tokens
      popular_phrases=phrases.remove_words(popular_phrases,remove_phrases)
      common = names.n_most_common_names(names.count_names(sub_tweets),6)
      for c in common:
          if len(c.split(' ')) < 2:
              common.remove(c)
      for t in query.tokens:
          for c in common:
              if t in c:
                  common.remove(c)
      print common

run_queries('../data/goldenglobes.tab','../data/buzz.txt')
