import tweepy, time

consumer_key='9DylZjpQIUOuRDVev7BRlShUS'
consumer_secret='WvDaTcYz3c70xgsadKBdi9BrfjpQEiymiOrPsg2KNVnZppnQo6'
access_token='1063915931066261504-FwDnh5XsrB0Hb0dVzsbfW0omgyMrKS'
access_token_secret='BrNAzfPwQGzb1rAuJCBC2EiC6HvFEXpVFBh9AZEWrpoTy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []
just_coords = []

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tweets.append(status)
        
        print(status.author.name, status.text, status.place.full_name, '==========', sep='\n')
        
        if status.coordinates:
            just_coords.append(str(tuple(status.coordinates['coordinates'][::-1])))
        
        #print(status.text)
        #print('==========')
        
        if len(tweets) >= 100:
            myStream.running = False
    
    def on_error(self, status_code):
        print(status_code)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#AB
#myStream.filter(locations=[-119.74,49.16,-110.52,59.85])

#Canada
myStream.filter(locations=[-136.90,43.67,-53.65,60.16])

#NY & LA
#myStream.filter(locations=[-122.75,36.8,-121.75,37.8,-74,40,-73,41], async= True)

#print('BLA BLA BLA')
#time.sleep(3)
#print('HA HA HA')

#myStream.filter(track=['python'])