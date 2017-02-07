import parser
import interpreter

def run_queries(tweets_file, queries_file):
  tweets = parser.parse_tweets(tweets_file)
  queries = parser.parse_queries(queries_file)
  winners = interpreter.get_winners(tweets, queries)

  for winner in winners:
    winner.prettyprint()
