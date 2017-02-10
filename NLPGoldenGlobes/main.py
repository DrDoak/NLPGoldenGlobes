import parser
import interpreter
from query import Query

def run_queries(tweets_file, queries_file):
  tweets = parser.parse_tweets(tweets_file)
  queries = parser.parse_queries(queries_file)
  # winners = interpreter.get_winners(tweets, queries)
  category = Query(".", ["present","introduce"])

  winners = interpreter.get_presenters(tweets,queries,category)
  print "Finished getting presenters"

  for winner in winners:
    winner.prettyprint()