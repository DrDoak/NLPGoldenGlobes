import re

# tweets that match any of the patterns
def any_match(tweets, patterns):
  matched_tweets = []
  for tweet in tweets:
    for pattern in patterns:
      if re.search(pattern, tweet.content):
        matched_tweets.append(tweet)
        break
  return matched_tweets

# tweets that match all of the patterns
def all_match(tweets, patterns):
  matched_tweets = []
  for tweet in tweets:
    no_match = False
    for pattern in patterns:
      if not re.search(pattern, tweet.content):
        no_match = True
        break
    if not no_match:
      matched_tweets.append(tweet)
  return matched_tweets

# tweets that match any of the patterns are removed
# a tweet matching one pattern but not another is removed
def exclude_any_match(tweets, patterns):
  matched_tweets = []
  for tweet in tweets:
    match = False
    for pattern in patterns:
      if re.search(pattern, tweet.content):
        match = True
        break
    if not match:
      matched_tweets.append(tweet)
  return matched_tweets

# tweets that match all of the patterns are removed
# a tweet matching one pattern but not another is not removed
def exclude_all_match(tweets, patterns):
  matched_tweets = []
  for tweet in tweets:
    for pattern in patterns:
      if not re.search(pattern, tweet.content):
        matched_tweets.append(tweet)
        break
  return matched_tweets

def downcase(tweets, strings):
  for tweet in tweets:
    for string in strings:
      tweet.content = re.sub(r'\b'+re.escape(string)+r'\b', string.lower(), tweet.content)
