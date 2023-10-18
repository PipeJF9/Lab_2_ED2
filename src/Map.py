import folium
from folium.plugins import MarkerCluster
m = folium.Map()

marker_cluster = MarkerCluster().add_to(m)

def add_markers(grafh):
    for dic in grafh.nodes:
        __add_marker(dic.Source_Airport_Latitude, dic.Source_Airport_Longitude, dic.Source_Airport_Name)
    return m

def __add_marker(lat, lon, name):
    folium.Marker(location=[lat, lon], popup=name).add_to(marker_cluster)

