import twitter
import os
import re

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

def get_user_info(handle):
    api = authenticate()
    if not api:
        return ''
    try:
        user_prof = api.GetUser(screen_name=handle)
    except twitter.error.TwitterError:
        return ''
    user_prof = user_prof.AsDict()
    name = user_prof[u'name']
    followers = user_prof[u'followers_count']
    return name, followers

def remove_movie(name):
    name = re.sub(r'(?i)\Wmovie','',name)
    name = re.sub("\s+"," ",name)
    return name

def correct_capitalization(name):
    return name.title()

#movie_name, movie_followers = get_user_info('@moonlightmov')
#print remove_movie(movie_name)
#print correct_capitalization(movie_name)