import folium
map=folium.Map(location=[45,-120],zoom_start=10,tiles="stamen terrain")
map.simple_marker(location=[45.3288,-121.697],popup="Rahul",marker_color="Red")
map.simple_marker(location=[40.3311,-121.7311],popup="Pritesh",marker_color="Green")
map.create_map(path="map1.html")
