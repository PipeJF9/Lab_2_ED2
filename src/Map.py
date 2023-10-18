import folium
from folium.plugins import MarkerCluster
m = folium.Map()

marker_cluster = MarkerCluster().add_to(m)

def add_markers(grafh):
    for dic in grafh.nodes:
        __add_marker(dic.Source_Airport_Latitude, dic.Source_Airport_Longitude, dic.Source_Airport_Name)

def __add_marker(lat, lon, name):
    folium.Marker(location=[lat, lon], popup=name).add_to(marker_cluster)


def aristas(lat1, lon1, lat2, lon2, code1, code2):
    folium.PolyLine(
    smooth_factor=50,
    locations=[[lat1, lon1], [lat2, lon2]],
    color="grey",
    tooltip=code1 + " - " + code2,
    weight=5,
    ).add_to(m)

def show_in_browser():
    m.show_in_browser()


def location(lat, lon):
    radius = 50
    folium.CircleMarker(
        location=[lat, lon],
        radius=radius,
        color="cornflowerblue",
        stroke=False,
        fill=True,
        fill_opacity=0.6,
        opacity=1,
        popup="{} pixels".format(radius),
        tooltip="I am in pixels",
    ).add_to(m)

