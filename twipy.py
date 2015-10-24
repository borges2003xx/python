import tweepy
import portachiavi

auth = tweepy.OAuthHandler(portachiavi.tw_consumer_key, portachiavi.tw_consumer_secret)
auth.set_access_token(portachiavi.tw_access_token, portachiavi.tw_access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline(count=2000)
for tweet in public_tweets:
    print tweet.text


