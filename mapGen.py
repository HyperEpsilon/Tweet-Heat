import folium
import numpy as num
import random
from folium.plugins import HeatMap

def createHeatMap():
    # generate the map
    ed = {'lat': 53.540996, 'lon': 0-113.497746 }
    mainMap = folium.Map(location=[ed['lat'], ed['lon']], zoom_start=10)

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


    for i in range(499):
        pingPoints['lat'].append(ed['lat']+random.randrange(-100,100)*0.01)
        pingPoints['lon'].append(ed['lon']+random.randrange(-100,100)*0.01)

    print(pingPoints)
    print(list(zip(pingPoints['lat'], pingPoints['lon'])))

    heat = HeatMap(list(zip(pingPoints['lat'], pingPoints['lon'])),
                   min_opacity=0.2,
                   max_val=1.0,
                   radius=15, blur=15,
                   max_zoom=1,)

    mainMap.add_child(heat)

    # heatMap output
    mainMap.save('heatMap.html')

if __name__ == "__main__":
    creatHeatMap()