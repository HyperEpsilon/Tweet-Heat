import folium
import numpy as num
import pandas as pd
from folium.plugins import HeatMap

# generate the map
mainMap = folium.Map(location=[53.540996, -113.497746], zoom_start=7 )

# add all layers
folium.TileLayer('Mapbox Bright').add_to(mainMap)
folium.TileLayer('Mapbox Control Room').add_to(mainMap)
folium.TileLayer('Stamen Toner').add_to(mainMap)
folium.TileLayer('openstreetmap').add_to(mainMap)
folium.TileLayer('Stamen Terrain').add_to(mainMap)

# add layer controller
folium.LayerControl().add_to(mainMap)

# test save
mainMap.save('vanillaMap.html')

"""""
pingPoints = []

max_amount = 10



hm_wide = HeatMap( list(zip(for_map.lat.values, for_map.lon.values, for_map.Amount.values)),
                   min_opacity=0.2,
                   max_val=max_amount,
                   radius=17, blur=15,
                   max_zoom=1,
                 )

folium.GeoJson(district23).add_to(hmap)
hmap.add_child(hm_wide)
"""
