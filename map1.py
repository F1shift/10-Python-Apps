import folium
import pandas
from random import uniform

datas = pandas.read_csv("Volcanoes.txt")
center = [41.795369, -112.692524]
map = folium.Map(location=center, zoom_start=6, tiles="Stamen Terrain")
popup_template = """<h4>Volcano Name:</h4>
<a href="https://www.google.com/search?q=%22{name}%22" target="_blank">{name}</a><br>
{elev}m
"""
feature_group = folium.FeatureGroup(name="My Map")
for name, lat, lon, elev in zip(datas["NAME"], datas["LAT"], datas["LON"], datas["ELEV"]):
    point = [ lat, lon ]
    popup = folium.Popup(folium.IFrame(html=popup_template.format(name=name, elev=elev), width=200, height=100))
    feature_group.add_child(folium.Marker(location=point, popup=popup, icon=folium.Icon(color="green")))

map.add_child(feature_group)
map.save("map1.html")
