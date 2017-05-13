import folium
import pandas

map=folium.Map(location=[40,-120],zoom_start=4)
df=pandas.read_csv("Volcanoes-USA.txt")

for lat,loc,name,elv in zip(df["LAT"],df["LON"],df["NAME"],df["ELEV"]):
    map.simple_marker(location=[lat,loc],popup=name,marker_color="green" if elv in range(0,1000) else "orange" if elv in range(1000,3000) else "red")

map.create_map(path="finalmap2.html")
