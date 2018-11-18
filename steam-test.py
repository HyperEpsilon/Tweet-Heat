import tweepy, time
from pprint import pprint

consumer_key='9DylZjpQIUOuRDVev7BRlShUS'
consumer_secret='WvDaTcYz3c70xgsadKBdi9BrfjpQEiymiOrPsg2KNVnZppnQo6'
access_token='1063915931066261504-FwDnh5XsrB0Hb0dVzsbfW0omgyMrKS'
access_token_secret='BrNAzfPwQGzb1rAuJCBC2EiC6HvFEXpVFBh9AZEWrpoTy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []
just_coords = []
all_coords = []
loc_centres = {}

def find_center(place):
    if place.id not in loc_centres.keys():
        cor_list = place.bounding_box.coordinates[0]
        lat_list = [x[0] for x in cor_list]
        lon_list = [x[1] for x in cor_list]
        
        try:
            area = 0
            for i in range(len(cor_list)-1):
                area += lat_list[i]*lon_list[i+1]-lat_list[i+1]*lon_list[i]
            area = 0.5 * (area)
            
            c_x = 0
            for i in range(len(lat_list)-1):
                c_x += (lat_list[i]+lat_list[i+1])*(lat_list[i]*lon_list[i+1]-lat_list[i+1]*lon_list[i])
            c_x = (c_x/(6*area))
            
            c_y = 0
            for i in range(len(lon_list)-1):
                c_y += (lon_list[i]+lon_list[i+1])*(lat_list[i]*lon_list[i+1]-lat_list[i+1]*lon_list[i])
            c_y = (c_y/(6*area))        
        except ZeroDivisionError:
            c_x = lat_list[0]
            c_y = lon_list[0]
        
        
        loc_centres[place.id] = (c_y, c_x)
    
    return loc_centres[place.id]


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        
        if status.place:
            tweets.append(status)
            
            print(status.author.name, status.text, status.place.full_name, '==========', sep='\n')
            
            if status.coordinates:
                just_coords.append(tuple(status.coordinates['coordinates'][::-1]))
                all_coords.append(tuple(status.coordinates['coordinates'][::-1]))
            else:
                all_coords.append(find_center(status.place))
            
            #print(status.text)
            #print('==========')
            
            if len(tweets) >= 100:
                myStream.running = False
    
    def on_error(self, status_code):
        print(status_code)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#North America
myStream.filter(locations=[-168.12,25.78,-51.54,71.61])


#Canada
#myStream.filter(locations=[-136.90,43.67,-53.65,60.16])

#AB
#myStream.filter(locations=[-119.74,49.16,-110.52,59.85])

#NY & LA
#myStream.filter(locations=[-122.75,36.8,-121.75,37.8,-74,40,-73,41], async= True)

#print('BLA BLA BLA')
#time.sleep(3)
#print('HA HA HA')

#myStream.filter(track=['python'])

#x = find_center(api.geo_id('01fbe706f872cb32'))