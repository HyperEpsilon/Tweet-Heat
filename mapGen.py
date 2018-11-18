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

    heat = HeatMap([(53.60100728, -113.49972797),
(43.78865482, -110.9577686),
(44.94727, -93.09707),
(45.5038, -73.5744),
(47.16, -122.51),
(51.1667, -115.567),
(47.2410428, -122.40005186),
(45.5, -73.5167),
(44.0519, -123.087),
(49.35087662, -123.25325915),
(49.25, -123.11),
(44.2167, -114.938),
(43.1388, -77.6909),
(43.7166, -79.3407),
(45.3677, -122.843),
(45.29, -75.78),
(51.19091, -114.46804),
(51.13906229, -113.93970113),
(43.83264, -79.44034),
(45.57353889, -122.69246944),
(42.65073, -73.75325),
(50.6759, -120.33898),
(43.64875, -79.39763),
(43.63845, -79.38504),
(42.91888889, -112.40638889),
(48.82444444, -123.72138889),
(45.583674, -122.543899),
(43.89666667, -78.87388889),
(44.9161, -93.1014),
(43.92055556, -78.68888889),
(47.60864, -122.33769),
(45.5167, -73.65),
(47.5692, -122.6548),
(47.0991, -122.638),
(44.977753, -93.2650108),
(44.97504231, -93.23219554),
(47.68, -122.21),
(46.8667, -71.2667),
(45.52371, -122.674621),
(47.0468, -122.926),
(45.518237, -122.678249),
(48.4287, -123.3645),
(45.04892257, -122.97495467)
],
                   min_opacity=0.2,
                   max_val=1.0,
                   radius=15, blur=15,
                   max_zoom=1,)

    mainMap.add_child(heat)

    # heatMap output
    mainMap.save('heatMap.html')

if __name__ == "__main__":
    creatHeatMap()