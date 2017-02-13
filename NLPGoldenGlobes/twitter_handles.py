import twitter
import os
import re
import copy

def authenticate():
    #need twitter auth keys
    #you will need a twitter account for this
    #make app at apps.twitter.com
    #then create access token under keys and access tokens
    api = twitter.Api(consumer_key=os.environ.get('TW_CONSUMER_KEY'),
                      consumer_secret=os.environ.get('TW_CONSUMER_SECRET'),
                      access_token_key=os.environ.get('TW_GGNLP_ACCESS_TOKEN'),
                      access_token_secret=os.environ.get('TW_GGNLP_ACCESS_TOKEN_SECRET'))
    try:
        api.VerifyCredentials()
    except twitter.error.TwitterError:
        print 'Could not authenticate user. Verify that the proper env variables are set.'
        print 'TW_CONSUMER_KEY\nTW_CONSUMER_SECRET\nTW_GGNLP_ACCESS_TOKEN\nTW_GGNLP_ACCESS_TOKEN_SECRET'
        return 0
    return api

#print(api.GetUser(screen_name='@rkrkrklyly'))
api = authenticate()

def get_user_info(handle, api):
    if not api:
        return '',0
    try:
        user_prof = api.GetUser(screen_name=handle)
    except twitter.error.TwitterError:
        return '', 0
    user_prof = user_prof.AsDict()
    name = user_prof[u'name']
    followers = user_prof[u'followers_count']
    return name, followers

def amplify_voice(tweets):
    new_list = copy.deepcopy(tweets)
    for tweet in tweets:
        try:
            name, followers = get_user_info(tweet.authorName, api)
            repetitions = followers/500
            for ii in range(0,repetitions):
                new_list.append(tweet)
        except:
            print tweet.authorName
    return new_list

def remove_movie(name):
    name = re.sub(r'(?i)\Wmovie','',name)
    name = re.sub("\s+"," ",name)
    return name

def correct_capitalization(name):
    return name.title()

#movie_name, movie_followers = get_user_info('@moonlightmov')
#print remove_movie(movie_name)
#print correct_capitalization(movie_name)