import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = (os.getenv("Twitter-API-Key"))
CONSUMER_SECRET = (os.getenv("Twitter-API-Key-Secret"))
ACCESS_KEY = (os.getenv("Twitter-Access-Token"))
ACCESS_SECRET = (os.getenv("Twitter-Access-Token-Secret"))

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status, you can write message whatever you want to post in twitter
api.update_status("Hello World!" + " #artAI" )