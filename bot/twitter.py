import tweepy
import os
import download
from dotenv import load_dotenv

load_dotenv()

# Consumer keys and access tokens, used for OAuth
consumer_key = (os.getenv("Twitter-API-Key"))
consumer_secret = (os.getenv("Twitter-API-Key-Secret"))
access_token = (os.getenv("Twitter-Access-Token"))
access_token_secret = (os.getenv("Twitter-Access-Token-Secret"))
bearer_token = (os.getenv("Twitter-Bearer-Token"))
imagePath = os.getenv('Local-Download-Location')
### Authorization protocol
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

### Providing access to API 
api = tweepy.API(auth)

### Tweeting to the linked twitter account
def tweet(tweetText):
    print("sending tweet \n" + tweetText)
    api.update_status(status = tweetText)

def tweetPic(tweetText, imageName):
    print("Sending tweet \n" + tweetText)
    print("With image \n" + imageName)
    media = api.media_upload(imagePath+imageName)
    post_result = api.update_status(status=tweetText, media_ids=[media.media_id])
    print(post_result)
    
def getPublicTweets():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

#Loop through n first images and send to twitter with news headline

def sendTweets():
    images = download.parseOutput()
    for image in images:
                try:
                        prompt = image.split("##")[0]
                        jobID = image.split("##")[1].replace("/", "" )
                        caption = image.split("##")[2]

                        print(prompt)
                        print(jobID) 
                        print(caption) 
                        
                        hastags="#News #AI #Art #BBC"
                        tweetMessage = prompt + "-BBC News"+"\n\n"+hastags
                        tweetPic(tweetText=tweetMessage, imageName=jobID + ".png")
                except:
                        print("An exception occurred")