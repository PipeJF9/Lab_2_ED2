import folium
from folium.plugins import MarkerCluster
m = folium.Map()

marker_cluster = MarkerCluster().add_to(m)

def add_markers(graph):
    for dic in graph.nodes:
        __add_marker(dic.Source_Airport_Latitude, dic.Source_Airport_Longitude, dic.Source_Airport_Name, dic.Source_Airport_Code, dic.Source_Airport_City, dic.Source_Airport_Country)
    return m

def __add_marker(lat, lon, name, code, city, country):
    folium.Marker(location=[lat, lon], popup=f"{name}\n{code}\n{city}\n{country}").add_to(marker_cluster)

