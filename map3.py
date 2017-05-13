import folium
import pandas

map=folium.Map(location=[40,-120],zoom_start=6)
df=pandas.read_csv("Volcanoes-USA.txt")

def map2(elv):
    minimum=int(min(df['ELEV']))
    step=int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elv in range(minimum,minimum+step):
        col="green"
    elif elv in range(minimum+step,minimum+step*2):
        col="orange"
    else:
        col="red"
    return col

for lat,loc,name,elv in zip(df["LAT"],df["LON"],df["NAME"],df["ELEV"]):
    map.simple_marker(location=[lat,loc],popup=name,marker_color=map2(elv))

map.create_map(path="finalmap3.html")
