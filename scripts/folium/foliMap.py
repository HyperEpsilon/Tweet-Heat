# import the library
import folium

# Make an empty map
m = folium.Map(location=[20, 0], zoom_start=3.5)

# Other tiles:
# OpenStreetMap, Stamen Terrain, Stamen Toner, Mapbox Bright, and Mapbox Control Room
m = folium.Map(location=[48.85, 2.35], tiles="Mapbox Bright", zoom_start=2)
m.save('basic_folium_map2.html')
m = folium.Map(location=[48.85, 2.35], tiles="Mapbox Control Room", zoom_start=2)
m.save('basic_folium_map3.html')
m = folium.Map(location=[48.85, 2.35], tiles="Stamen Toner", zoom_start=2)
m.save('basic_folium_map4.html')
m = folium.Map(location=[48.85, 2.35], tiles="OpenStreetMap", zoom_start=2)
m.save('basic_folium_map5.html')

# Same but with a zoom
m = folium.Map(location=[48.85, 2.35], tiles="Mapbox Bright", zoom_start=10)
m.save('basic_folium_map6.html')
m = folium.Map(location=[48.85, 2.35], tiles="Stamen Toner", zoom_start=10)
m.save('basic_folium_map7.html')
m = folium.Map(location=[48.85, 2.35], tiles="Stamen Terrain", zoom_start=10)
m.save('basic_folium_map8.html')
m = folium.Map(location=[48.85, 2.35], tiles="OpenStreetMap", zoom_start=10)
m.save('basic_folium_map9.html')
