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

fg=folium.FeatureGroup(name="Volacano Locations")

for lat,loc,name,elv in zip(df["LAT"],df["LON"],df["NAME"],df["ELEV"]):
    fg.add_child(folium.Marker(location=[lat,loc],popup=name,icon=folium.Icon(map2(elv),icon_color="green")))

map.add_child(fg)
map.add_child(folium.GeoJson(data=open("world_population.json"),
name='world_population',
style_function=lambda x: {'fillcolor':'green' if x['properties']['POP2005']<=1000000 else 'orange' if 1000000<x['properties']['POP2005']<2000000 else 'red'}))

map.add_child(folium.LayerControl())
map.save(outfile="finalmap4.html")
