import parser
import interpreter

def run_queries(tweets_file, queries_file):
  tweets = parser.parse_tweets(tweets_file)
  queries = parser.parse_queries(queries_file)
  host = interpreter.get_host(tweets)
  winners = interpreter.get_winners(tweets, queries)
  presenters = interpreter.get_presenters(tweets, queries, winners)

  print 'Host'
  host.prettyprint()

  print '\nWinners'
  for winner in winners:
    winner.prettyprint()

  print '\nPresenters'
  for presenter in presenters:
    presenter.prettyprint()
