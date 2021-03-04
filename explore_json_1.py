import json


infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")


# json.load() converts data into a format python can work with
# in this case its a dictionary
eq_data = json.load(infile)


# json.dump() takes the data and puts it in a file

json.dump(eq_data, outfile, indent=4)
# print(eq_data["features"][0]["properties"]["mag"])
list_of_eqs = eq_data["features"]  # condenses above print statement
places, mags, lons, lats = [], [], [], []  # list of eq magnitudes

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    place = eq["properties"]["place"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    places.append(place)

# print(mags[:10], lons[:10], lats[:10], places[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": places,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]


my_layout = Layout(title="global eathquakes")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")
