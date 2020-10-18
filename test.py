# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

#api.update_status(status="hello from ultrahacks!")

#tweets = api.search('#oregontrail', count = 100)
#        
#for tweet in tweets: 
#    print(tweet.text)

#ids = api.followers_ids(screen_name = 'lovinsumanime', count = 10)
#for user in api.lookup_users(user_ids=ids):
#    print("https://twitter.com/{}".format(user.screen_name))

