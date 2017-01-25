import re

def regex_search(tweets, patterns):
    matched_tweets = []
    for tweet in tweets:
        for pattern in patterns:
            if re.search(pattern, tweet.content):
                matched_tweets.append(tweet)
                break
    return matched_tweets

"""
import tweet
t1 = tweet.Tweet("", "Jimmy host the Oscars",9,'',9,'2017-01-09 23:59:55')
t2 = tweet.Tweet("", "Jimmy hosted the Oscars",9,'',9,'2017-01-09 23:59:55')

vals = regex_search([t1,t2], [r'\bhost.*\b'])

for v in vals:
    print v.content
    """

