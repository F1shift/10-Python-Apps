from turtle import color, fillcolor
import folium
import pandas
from random import uniform
from pathlib import Path

data_dir=Path("data")
output_dir=Path("output")
html_dir=Path("html")
popup_template = html_dir.joinpath("popup.html").read_text()
datas = pandas.read_csv(data_dir.joinpath("Volcanoes.txt"))
center = [41.795369, -112.692524]

def map_color(elev: float) -> str:
    if elev < 500:
        return "#ccb93f"
    elif elev < 1000:
        return "#96cc3f"
    elif elev < 1500:
        return "#59cc3f"
    elif elev < 2000:
        return "#3fcc86"
    elif elev < 2500:
        return "#3fc5cc"
    elif elev < 3000:
        return "#3f67cc"
    elif elev < 3500:
        return "#693fcc"
    else:
        return "#ab3fcc"

map = folium.Map(location=center, zoom_start=6, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup(name="My Map")
for name, lat, lon, elev in zip(datas["NAME"], datas["LAT"], datas["LON"], datas["ELEV"]):
    point = [ lat, lon ]
    popup = folium.Popup(folium.IFrame(html=popup_template.format(name=name, elev=elev), width=200, height=100))
    feature_group.add_child(folium.CircleMarker(location=point, 
                                                popup=popup, 
                                                radius=6,
                                                color="#111111",
                                                fill=True,
                                                fill_color=map_color(elev),
                                                fill_opacity=0.7))

map.add_child(feature_group)
map.save(output_dir.joinpath("map1.html").__str__())