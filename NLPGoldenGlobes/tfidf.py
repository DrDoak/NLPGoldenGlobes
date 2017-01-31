import math

def tfidf(t, d, D):
  return tf(t, d) * math.log(1 / df(t, D))

def tf(t, d):
  words = d.content.split(' ')
  count_words = float(count_occurences(t, words))
  return count_words / len(words)

def count_occurences(t, words):
  num_occurs = 0
  for word in words:
    if word == t:
      num_occurs += 1
  return num_occurs

def df(t, D):
  num_docs = 0
  for tweet in D:
    if tf(t, tweet) > 0:
      num_docs += 1
  return  float(num_docs) / len(D)

def cache_tfidf(tweets):
  store_tf(tweets)
  df_dict = calculate_df(tweets)
  store_tfidf(tweets, df_dict)

def store_tf(tweets):
  for tweet in tweets:
    words = tweet.content.split(' ')
    for word in words:
      tweet.tf[word] = tf(word, tweet)

def calculate_df(tweets):
  df_dict = {}
  for tweet in tweets:
    for term in tweet.tf:
      df_count = df_dict.get(term, 0)
      df_dict[term] = df_count + 1

  num_docs = float(len(tweets))
  for term in df_dict:
    df_dict[term] /= num_docs

  return df_dict

def store_tfidf(tweets, df_dict):
  for tweet in tweets:
    for term in tweet.tf:
      tweet.tfidf[term] = tweet.tf[term] * math.log(1 / df_dict[term])
