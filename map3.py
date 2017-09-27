import folium
import pandas
import time

start = time.time()

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


map_1 = folium.Map(location=[0, 0], zoom_start=2, tiles="Mapbox Bright")

fg_v = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fg_v.add_child(folium.CircleMarker(location=(lt, ln),
                                     radius=5,
                                     popup=folium.Popup(str(el) + " m", parse_html=True),
                                     fill_color=color_producer(el),
                                     color = color_producer(el),
                                     fill = True,
                                     fill_opacity = 0.7))

fg_p = folium.FeatureGroup(name="Population")

fg_p.add_child(folium.GeoJson(data=open("world.json", 'r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005']
                                                      < 20000000 else 'red'}))

map_1.add_child(fg_v)
map_1.add_child(fg_p)
map_1.add_child(folium.LayerControl())
map_1.save("Map_3.html")

stop = time.time()
finished_in = (stop - start)
print(finished_in)
