import folium
import numpy as num
import random
import sqlite3, time
from folium.plugins import HeatMap


connection = None
cursor = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    return

def get_data_points():
    path="./All_tweets.db"
    connect(path)      
    
    query = "SELECT lat, lon FROM tweets"
    tweets = cursor.execute(query)
    all_tweets = [tweet for tweet in tweets]
    
    print(len(all_tweets))
    print(all_tweets)
    #print(type(all_tweets[0][0]))
    
    connection.close()
    
    return all_tweets



#createHeatMap(heatArray)

def createHeatMap(heat_Map_Array, start_lat=53.540996, start_lon=-113.497746):
    # generate the map
    mainMap = folium.Map(
        location=[start_lat, start_lon],
        zoom_start=10,
        no_wrap=True,
        world_copy_jump=True,

    )

    # add all layers
    """
    folium.TileLayer('Mapbox Bright').add_to(mainMap)
    folium.TileLayer('Mapbox Control Room').add_to(mainMap)
    folium.TileLayer('Stamen Toner').add_to(mainMap)
    folium.TileLayer('openstreetmap').add_to(mainMap)
    folium.TileLayer('Stamen Terrain').add_to(mainMap)
    """

    # add layer controller
    # folium.LayerControl().add_to(mainMap)

    pingPoints = {'lat': [], 'lon': []}

    #print(pingPoints)
    #print(list(zip(pingPoints['lat'], pingPoints['lon'])))

    heat = HeatMap(
            heat_Map_Array,
            min_opacity=0.2,
            max_val=1.0,
            radius=15, blur=15,
            max_zoom=1,)

    mainMap.add_child(heat)

    # heatMap output
    mainMap.save('static/heatMap.html')

if __name__ == "__main__":
    #createHeatMap()
    for i in range(10):
        heatArray = get_data_points()
        createHeatMap(heatArray,53.540996,-113.497746)
        time.sleep(2)
    input()