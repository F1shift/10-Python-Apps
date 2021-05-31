import folium
import pandas
from random import uniform

datas = pandas.read_csv("Volcanoes.txt")
center = [datas["LAT"][0], datas["LON"][0]]
map = folium.Map(location=center, zoom_start=6, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup(name="My Map")
for name, lat, lon in zip(datas["NAME"], datas["LAT"], datas["LON"]):
    point = [ lat, lon ]
    feature_group.add_child(folium.Marker(location=point, popup=name, icon=folium.Icon(color="green")))
map.add_child(feature_group)
map.save("map1.html")
