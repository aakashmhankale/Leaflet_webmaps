import folium
map_osm = folium.Map(location=[45.5236, -122.6750])
map_osm.save('osm.html')
import folium

# Coordinates are 10 points on the great circle from Boston to
# San Francisco.
# Reference: http://williams.best.vwh.net/avform.htm#Intermediate
coordinates = [
    [42.3581, -71.0636],
    [42.82995815, -74.78991444],
    [43.17929819, -78.56603306],
    [43.40320216, -82.37774519],
    [43.49975489, -86.20965845],
    [41.4338549, -108.74485069],
    [40.67471747, -112.29609954],
    [39.8093434, -115.76190821],
    [38.84352776, -119.13665678],
    [37.7833, -122.4167]]

# Create the map and add the line
m = folium.Map(location=[41.9, -97.3], zoom_start=4)
my_PolyLine=folium.PolyLine(locations=coordinates,weight=5)
m.add_children(my_PolyLine)
m.save('line_example_newer.html')
