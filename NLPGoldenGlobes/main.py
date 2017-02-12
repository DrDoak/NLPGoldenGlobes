import parser
import interpreter

def run_queries(tweets_file, queries_file):
  tweets = parser.parse_tweets(tweets_file)
  queries = parser.parse_queries(queries_file)
  # host = interpreter.get_host(tweets)
  # winners = interpreter.get_winners(tweets, queries)
  print "Getting Nominees:"
  nominees = interpreter.get_movie_nominees(tweets,queries)

  # host.prettyprint()
  # for winner in winners:
  #   winner.prettyprint()
  for nominee in nominees:
  	nominee.prettyprint()
