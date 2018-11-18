import tweepy
from urllib.request import urlopen
from urllib.parse import quote


consumer_key='9DylZjpQIUOuRDVev7BRlShUS'
consumer_secret='WvDaTcYz3c70xgsadKBdi9BrfjpQEiymiOrPsg2KNVnZppnQo6'
access_token='1063915931066261504-FwDnh5XsrB0Hb0dVzsbfW0omgyMrKS'
access_token_secret='BrNAzfPwQGzb1rAuJCBC2EiC6HvFEXpVFBh9AZEWrpoTy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        print(status.coordinates)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())

myStream.filter(locations=[53.457912,-113.617431,53.619420,-113.371607])

## Bounding box coordingates: tweet.place.bounding_box.coordinates[0]

tweets = api.home_timeline()
#tweets = api.user_timeline(351978460, count=5)
