import tweepy
import os

# def Send a tweet
def send_tweet(tweet_text):
    auth = tweepy.OauthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(tweet_text)