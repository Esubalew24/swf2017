import os
import folium
from folium import plugins
Uni_map = os.path.join('', 'Uni_map.png')

map_osm = folium.Map(location=[65.0593, 25.4663], zoom_start=17, tiles='Stamen Terrain')
folium.Marker([65.0593, 25.4663], popup='Central Station').add_to(map_osm)
folium.Marker([65.0593, 25.4669], popup='Tellus Library').add_to(map_osm)
folium.CircleMarker(location=[65.0599, 25.4699], radius=50,
                    popup='You are in University area', color='#3186cc',
                    fill_color='#3186cc').add_to(map_osm)

plugins.ImageOverlay(
    image=open(Uni_map, 'r'),
    bounds=[[65.0540, 25.4585], [65.0640, 25.4765]],
    opacity=0.8,
).add_to(map_osm)

folium.LayerControl().add_to(map_osm)

map_osm.save(os.path.join('', 'map2.html'))