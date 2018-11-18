import folium
import numpy as num
import random
from folium.plugins import HeatMap



#createHeatMap(heatArray)

def createHeatMap(heat_Map_Array, start_lat=53.540996, start_lon=-113.497746, start_zoom = 10):
    # generate the map
    mainMap = folium.Map(
        location=[start_lat, start_lon],
        zoom_start=start_zoom,
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
    createHeatMap(heatArray,53.540996,0-113.497746)