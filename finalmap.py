import folium
import pandas

#map=folium.Map(location=[45,-120],zoom_start=10,tiles="stamen terrain")
map=folium.Map(location=[40,-120],zoom_start=4)
df=pandas.read_csv("Volcanoes-USA.txt")

for lat,loc,name in zip(df["LAT"],df["LON"],df["NAME"]):
    map.simple_marker(location=[lat,loc],popup=name,marker_color="Red")

map.create_map(path="finalmap1.html")
