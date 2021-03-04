import json


infile = open("US_fires_9_14.json", "r")
outfile = open("readable_fires_9_14.json", "w")

# json.load() converts data into a format python can work with
# in this case its a dictionary
fire_data = json.load(infile)

# json.dump() takes the data and puts it in a file

json.dump(fire_data, outfile, indent=4)
# print(eq_data["features"][0]["properties"]["mag"])
# condenses above print statement
lons, lats, brights = [], [], []  # list of eq magnitudes

for fires in fire_data:
    lon = fires["longitude"]
    lat = fires["latitude"]
    bright = fires["brightness"]
    if bright > 450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)

print(brights[:10], lons[:10], lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [int(bright) * 0.03 for bright in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Fires"},
        },
    }
]


my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="california_fires_9_1.html")
