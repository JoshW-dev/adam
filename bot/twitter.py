import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

# Consumer keys and access tokens, used for OAuth
consumer_key = (os.getenv("Twitter-API-Key"))
consumer_secret = (os.getenv("Twitter-API-Key-Secret"))
access_token = (os.getenv("Twitter-Access-Token"))
access_token_secret = (os.getenv("Twitter-Access-Token-Secret"))
bearer_token = (os.getenv("Twitter-Bearer-Token"))

### Authorization protocol
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

### Providing access to API 
api = tweepy.API(auth)

### Tweeting to the linked twitter account
def tweet():
    api.update_status(status = "hello")

def getPublicTweets():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)