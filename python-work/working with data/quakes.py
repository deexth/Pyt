import requests
import pandas as pd
import plotly.graph_objects as go
from plotly import offline
import plotly.express as px
import json

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
r = requests.get(url)
# print(f"Status code: {r.status_code}")
readable_file = json.loads(r.content.decode())
filename = "data/eq_data.json"
with open(filename, "w") as f:
    json.dump(readable_file, f, indent=4)

readable_file_dicts = readable_file["features"]
# len(readable_file_dicts)
mags, lons, lats, places = [], [], [], []
for quake in readable_file_dicts:
    try:
        mags.append(quake["properties"]["mag"])
        places.append(quake["properties"]["place"])
        lons.append(quake["geometry"]["coordinates"][0])
        lats.append(quake["geometry"]["coordinates"][1])
    except KeyError:
        print(f"Data missing for {quake['properties']['place']}")
        continue

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=[
        mag if mag is not None and mag > 0 else 0 for mag in mags
    ],
    color=mags,
    hover_name=places,
    projection="natural earth",
    scope="world",
    title="Earthquakes",
    labels={
        "lat": "Latitude",
        "lon": "Longitude",
        "size": "Magnitude",
        "color": "Magnitude",
    },
    color_continuous_scale=px.colors.sequential.Viridis,
)

# fig.show()
offline.plot(fig, filename="earthquakes.html")