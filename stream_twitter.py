import tweepy, time, sqlite3
from pprint import pprint

consumer_key='9DylZjpQIUOuRDVev7BRlShUS'
consumer_secret='WvDaTcYz3c70xgsadKBdi9BrfjpQEiymiOrPsg2KNVnZppnQo6'
access_token='1063915931066261504-FwDnh5XsrB0Hb0dVzsbfW0omgyMrKS'
access_token_secret='BrNAzfPwQGzb1rAuJCBC2EiC6HvFEXpVFBh9AZEWrpoTy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []
ids = []
just_coords = []
all_coords = []
loc_centres = {}

#connection = None
#cursor = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return

def define_tables():
    global connection, cursor

    cursor.execute('''drop table if exists tweets''')

    comic_query=   '''
                        CREATE TABLE IF NOT EXISTS tweets (
                                    tweet_id INT,
                                    date INT,
                                    lat TEXT,
                                    lon TEXT,
                                    PRIMARY KEY (tweet_id)
                                    );
                    '''
    
    cursor.execute(comic_query)

def add_tweet(id, date, coords):
    
    query = "INSERT INTO tweets (tweet_id, date, lat, lon) VALUES (?,?,?,?)"
    cursor.execute(query, [id, date] + coords)


def find_center(place):
    if place.id not in loc_centres.keys():
        cor_list = place.bounding_box.coordinates[0]
        lat_list = [x[0] for x in cor_list]
        lon_list = [x[1] for x in cor_list]
        
        c_x = (max(lat_list) + min(lat_list))/2.0
        c_y = (max(lon_list) + min(lon_list))/2.0
        
        
        loc_centres[place.id] = [c_y, c_x]
    
    return loc_centres[place.id]


class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        self.api = api or API()
        path="./All_tweets.db"
        self.connect(path)    
        self.define_tables()
    
    def connect(self,path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        self.cursor.execute(' PRAGMA foreign_keys=ON; ')
        self.connection.commit()
        return
    
    def define_tables(self):
        self.cursor.execute('''drop table if exists tweets''')
    
        comic_query=   '''
                            CREATE TABLE IF NOT EXISTS tweets (
                                        tweet_id INT,
                                        date INT,
                                        lat REAL,
                                        lon REAL,
                                        PRIMARY KEY (tweet_id)
                                        );
                        '''
        
        self.cursor.execute(comic_query)
    
    def add_tweet(self, id, date, coords):
        
        query = "INSERT INTO tweets (tweet_id, date, lat, lon) VALUES (?,?,?,?)"
        self.cursor.execute(query, [id, date] + coords)    
    
    def on_status(self, status):
        

        if status.place:
            tweets.append(status)
            
            if status.id not in ids:
                ids.append(status.id)
            
                print(status.author.name, status.text, status.place.full_name, '==========', sep='\n')
                
                if status.coordinates:
                    just_coords.append(tuple(status.coordinates['coordinates'][::-1]))
                    all_coords.append(tuple(status.coordinates['coordinates'][::-1]))
                    
                    #self.add_tweet(status.id, int(status.created_at.timestamp()), status.coordinates['coordinates'][::-1])
                    self.add_tweet(status.id, int(status.created_at.timestamp()), find_center(status.place))
                    self.connection.commit()
                else:
                    all_coords.append(tuple(find_center(status.place)))
                    
                    self.add_tweet(status.id, int(status.created_at.timestamp()), find_center(status.place))
                    self.connection.commit()
                
                
                if len(ids) >= 100:
                    self.connection.close()
                    return False
    
    def on_error(self, status_code):
        print(status_code)


def start_stream():
    
    
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    
    
    #North America
    myStream.filter(locations=[-168.12,25.78,-51.54,71.61])
    
    #Canada
    #myStream.filter(locations=[-136.90,43.67,-53.65,60.16], async= True)
    
    #AB
    #myStream.filter(locations=[-119.74,49.16,-110.52,59.85], async= True)
    
    #NY & LA
    #myStream.filter(locations=[-122.75,36.8,-121.75,37.8,-74,40,-73,41], async= True)
    
    #print('BLA BLA BLA')
    #time.sleep(3)
    #print('HA HA HA')


if __name__ == "__main__":
    start_stream()