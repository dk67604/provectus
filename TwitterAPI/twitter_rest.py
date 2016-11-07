#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from requests_oauthlib import OAuth1
import requests
import tweepy
from urllib import urlencode



# Variables that contains the user credentials to access Twitter API
class OAuthHandler:
    def __init__(self):
        self.access_token = ''
        self.access_token_secret = ''
        self.consumer_key = ''
        self.consumer_secret = ''

    def get_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth, retry_count=3, retry_delay=5, retry_errors=set([401, 404, 500, 503]), wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
        return api

    def get_oauth(self):
        oauth = OAuth1(self.consumer_key,
                       client_secret= self.consumer_secret,
                       resource_owner_key=self.access_token,
                       resource_owner_secret=self.access_token_secret)
        return oauth

    def get_tweet_info(self,tweed_id):
        api = self.get_api()
        tweet = api.get_status(tweed_id)
        return tweet


    def get_user_info(self,screen_name):
        oauth = self.get_oauth()
        r = requests.get(url="https://api.twitter.com/1.1/users/show.json?screen_name="+screen_name, auth=oauth)
        return r.json()


if __name__ == '__main__':
    oauth=OAuthHandler()
    api=oauth.get_api()
    tweet = api.get_status("752893403864690688")
    print (tweet.user.lang)
    oauth = oauth.get_oauth()
    r = requests.get(url="https://api.twitter.com/1.1/statuses/show.json?id=752893403864690688", auth=oauth)
    data=r.json()
    user_data=data['user']
    res=requests.get(url="https://api.twitter.com/1.1/users/show.json?screen_name=marisamoore",auth=oauth)








