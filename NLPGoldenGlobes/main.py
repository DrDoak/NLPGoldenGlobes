import parser
import interpreter
import buzz

def run_queries(tweets_file, queries_file, buzz_file):
  tweets = parser.parse_tweets(tweets_file)
  queries = parser.parse_queries(queries_file)
  additional_queries = parser.parse_queries(buzz_file)

  host = interpreter.get_host(tweets)
  winners = interpreter.get_winners(tweets, queries)
  presenters = interpreter.get_presenters(tweets, queries, winners)
  nominees = interpreter.get_nominees(tweets, queries, winners)
  interesting_people = buzz.run_queries_buzz(tweets, additional_queries)

  print 'Host'
  host.prettyprint()

  print '\nWinners'
  for winner in winners:
    winner.prettyprint()

  print '\nPresenters'
  for presenter in presenters:
    presenter.prettyprint()

  print '\nNominees'
  for nominee in nominees:
    nominee.prettyprint()

  print '\nInteresting Stuff!'
  for people in interesting_people:
    people.prettyprint()
