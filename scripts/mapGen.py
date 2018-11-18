import folium
import numpy as num
import pandas as pd
import random
from folium.plugins import HeatMap

# generate the map
ed = {'lat': 53.540996, 'lon': -113.497746}
mainMap = folium.Map(location=[ed['lat'], ed['lon']], zoom_start=7)

# add all layers
"""
folium.TileLayer('Mapbox Bright').add_to(mainMap)
folium.TileLayer('Mapbox Control Room').add_to(mainMap)
folium.TileLayer('Stamen Toner').add_to(mainMap)
folium.TileLayer('openstreetmap').add_to(mainMap)
folium.TileLayer('Stamen Terrain').add_to(mainMap)
"""
# vanilla map output
mainMap.save('vanillaMap.html')


# add layer controller
# folium.LayerControl().add_to(mainMap)

pingPoints = {'lat': [], 'lon': []}

for i in range(500):
    pingPoints['lat'].append(ed['lat'])
    pingPoints['lon'].append(ed['lon'])

print(pingPoints)


heat = HeatMap( list(zip(pingPoints['lat'], pingPoints['lon'])),
                   min_opacity=0.2,
                   radius=17, blur=15,
                   max_zoom=1,
                 )

mainMap.add_child(heat)

# heatMap output
mainMap.save('heatMap.html')

